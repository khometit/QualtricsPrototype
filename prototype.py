import requests
import json
import config
from api import API, header
import time

class Prototype:


    def run(self):
        surveyID = 'SV_ctED9EvO8ZIHsVM'
        endpoint = 'surveys'
        url = config.BASE_URL + endpoint

        res = requests.get(url, headers = header)
        print(json.dumps(res.json(), indent = 4))
        


        #Create a survey and get its ID

        surveyID = 'SV_6kUMZLLa8UciK5o'#API.create_survey(('Prototype', 'EN', 'CORE'))
        print(surveyID)
        time.sleep(0.5)

        API.retrieve_response(surveyID)
        
        #Create a question
        API.create_questions(surveyID)

        #Fetch all the questions created
        qDict = API.fetch_all_questions(surveyID)
        #print(json.dumps(qDict, indent=4))

        #Publish survey
        res = API.publish_survey(surveyID)
        #print(json.dumps(res, indent=4))

        #Get responses
        
        


if __name__ == '__main__':
    prop = Prototype()

    prop.run()

#Choose question type, answer type and number of choices

#Choose if reponse if required

#Add an end of survey message

#Finally publish the survey