import config
import requests
import json
import questionModel
import zipfile
import io, os

header = {'X-API-TOKEN': config.TOKEN, 'Content-Type': 'application/json', 'accept': "application/json"}

class API:
    

    def create_survey(surveyInfo:tuple):
        #header = {'X-API-TOKEN': config.TOKEN, 'Content-Type': 'application/json'}
        url = config.BASE_URL + 'survey-definitions'

        data = { 'SurveyName': surveyInfo[0], "Language": surveyInfo[1], "ProjectCategory": surveyInfo[2]}
        print(data)

        #serialize the dictionary to a JSON obj
        payload = json.dumps(data, indent=4)
        
        res = requests.post(url, data = payload, headers=header)
        print(json.dumps(res.json(), indent=3))
        return(res.json()['result']['SurveyID'])

    def create_question(surveyID, qText, qType='MC'):
        url = config.BASE_URL + 'survey-definitions/{}/questions'.format(surveyID)

        #Probably need to create a user input here for the params, or not?

        data = {'ChoiceOrder': ['1', '2'], 'Choices': {} , 'Configuration': {}, 'Language' : [], 
                'QuestionDescription': 'testQ', 'QuestionText': qText, 'QuestionType': qType, 'Selector': 'DL', 
                'SubSelector': 'TX', 
                'Validation': {'Settings': {'ForceResponse': 'OFF', 'ForceResponseType': 'ON', 'Type': 'None'} }
                }

        data['Choices']['1'] = {'Display': 'Yes'}
        data['Choices']['2'] = {'Display': 'No'}

        data['Configuration'] = {'TextPosition': 'inline'}

        payload = json.dumps(data, indent=4)
        print(payload)

        res = requests.post(url, data=payload, headers=header)

        print(json.dumps(res.json(), indent=4))

    def fetch_all_questions(surveyID):
        res = requests.get(url = config.BASE_URL + 'survey-definitions/{}/questions'.format(surveyID), headers=header)
        
        return res.json()
        
    def create_questions(surveyID):
        url = config.BASE_URL + 'survey-definitions/{}/questions'.format(surveyID)

        #Probably need to create a user input here for the params, or not?
        data = questionModel.MatrixQuestion
        payload = json.dumps(data, indent=4)
        #print(payload)

        res = requests.post(url, data=payload, headers=header)
        #print(json.dumps(res.json(), indent=4))

        data = questionModel.tableQuestion
        res = requests.post(url, data=json.dumps(data, indent=4), headers=header)
        print(json.dumps(res.json(), indent=4))

    def publish_survey(surveyID):
        activatePayload ={
                        "isActive": True,
                        "expiration": {
                            "startDate": "2022-12-10T12:00:00Z",
                            "endDate": "2022-12-14T14:00:00Z"}
                        }
        urlActivate = config.BASE_URL + 'surveys/{}'.format(surveyID)

        url = config.BASE_URL + 'survey-definitions/{}/versions'.format(surveyID)
        data = {
            "Description": "Prototype survey",
            "Published": True
            }

        requests.put(urlActivate, json=activatePayload, headers=header)
        res = requests.post(url, json=data, headers=header)
        return res.json()

    def retrieve_response(surveyID):
        url = config.BASE_URL + 'surveys/{}/export-responses/'.format(surveyID)
        fileFormat ='csv'
        requestCheckProgress = 0.0
        progressStatus = "inProgress"

        # Step 1: Creating Data Export
        payload = '{"format":"' + fileFormat + '"}'
        res = requests.post(url, data=payload, headers=header)

        progressId = res.json()["result"]["progressId"]
        print(json.dumps(res.json()))

        # Step 2: Checking on Data Export Progress and waiting until export is ready
        while progressStatus != "complete" and progressStatus != "failed":
            print ("progressStatus=", progressStatus)
            requestCheckUrl = url + progressId
            requestCheckResponse = requests.get(requestCheckUrl, headers=header)

            requestCheckProgress = requestCheckResponse.json()["result"]["percentComplete"]
            print(json.dumps(requestCheckResponse.json()))

            print("Download is " + str(requestCheckProgress) + " complete")
            progressStatus = requestCheckResponse.json()["result"]["status"]

        #step 2.1: Check for error

        if progressStatus is "failed":

            raise Exception("export failed")

        fileId = requestCheckResponse.json()["result"]["fileId"]

        # Step 3: Downloading file
        requestDownloadUrl = url + fileId + '/file'
        requestDownload = requests.get(requestDownloadUrl, headers=header, stream=True)
        
        # Step 4: Unzipping the file
        zipfile.ZipFile(io.BytesIO(requestDownload.content)).extractall("QualtricsResponses")
        print('Complete')