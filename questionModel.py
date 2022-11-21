
#For the side by side, matrix question
{
    "QuestionText": "Click to write the question text",
    "DefaultChoices": False,
    "DataExportTag": "Q4",
    "QuestionType": "SBS",
    "Selector": "SBSMatrix",
    "Configuration": {
        "QuestionDescriptionOption": "UseText",
        "RepeatHeaders": "none"
    },
    "QuestionDescription": "Click to write the question text",
    "Choices": {
        "1": {
            "Display": "Statement 1"
        },
        "2": {
            "Display": "Statement 2"
        },
        "3": {
            "Display": "Click to write Statement 3"
        }
    },
    "ChoiceOrder": [
        "1",
        "2",
        "3"
    ],
    "Validation": {
        "Settings": {
            "ForceResponse": "OFF",
            "Type": "None"
        }
    },
    "GradingData": [],
    "Language": [],
    "NextChoiceId": 4,
    "NextAnswerId": 3,
    "NumberOfQuestions": 2,
    "AdditionalQuestions": {
        "1": {
            "Answers": {
                "1": {
                    "Display": "Answer 1"
                },
                "2": {
                    "Display": "Answer 2"
                }
            },
            "QuestionText": "Col 1",
            "RecodeValues": [],
            "VariableNaming": [],
            "AnalyzeChoices": [],
            "QuestionType": "Matrix",
            "Selector": "Likert",
            "SubSelector": "SingleAnswer",
            "ChoiceColumnWidthPixels": None,
            "DataExportTag": "Q4#1",
            "QuestionID": "QID7#1",
            "Choices": {
                "1": {
                    "Display": "Statement 1"
                },
                "2": {
                    "Display": "Statement 2"
                },
                "3": {
                    "Display": "Click to write Statement 3"
                }
            },
            "ChoiceDataExportTags": False,
            "QuestionDescription": "Col 1",
            "Configuration": {
                "QuestionDescriptionOption": "UseText"
            }
        },
        "2": {
            "Answers": {
                "1": {
                    "Display": "Answer 1"
                },
                "2": {
                    "Display": "Answer 2"
                }
            },
            "QuestionText": "Col 2",
            "RecodeValues": [],
            "VariableNaming": [],
            "AnalyzeChoices": [],
            "QuestionType": "Matrix",
            "Selector": "Likert",
            "SubSelector": "SingleAnswer",
            "ChoiceColumnWidthPixels": None,
            "DataExportTag": "Q4#2",
            "QuestionID": "QID7#2",
            "Choices": {
                "1": {
                    "Display": "Statement 1"
                },
                "2": {
                    "Display": "Statement 2"
                },
                "3": {
                    "Display": "Click to write Statement 3"
                }
            },
            "ChoiceDataExportTags": False,
            "QuestionDescription": "Col 2",
            "Configuration": {
                "QuestionDescriptionOption": "UseText"
            }
        }
    },
    "ChoiceDataExportTags": False,
    "QuestionID": "QID7",
    "QuestionText_Unsafe": "Click to write the question text"
},

#For a simple multiple choice
{
    "ChoiceOrder": [
        "1",
        "2"
    ],
    "Choices": {
        "1": {
            "Display": "Yes"
        },
        "2": {
            "Display": "No"
        }
    },
    "Configuration": {
        "TextPosition": "inline",
        "QuestionDescriptionOption": "UseText"
    },
    "Language": [],
    "QuestionDescription": "Do you like coffee?",
    "QuestionText": "Do you like coffee?",
    "QuestionType": "MC",
    "Selector": "SAVR",
    "Validation": {
        "Settings": {
            "ForceResponse": "OFF",
            "ForceResponseType": "ON",
            "Type": "None"
        }
    },
    "DataExportTag": "Q1",
    "QuestionID": "QID2",
    "DataVisibility": {
        "Private": False,
        "Hidden": False
    },
    "NextChoiceId": 3,
    "NextAnswerId": 1,
    "SubSelector": "TX",
    "QuestionText_Unsafe": "Do you like coffee?"
},
#For a form field question
{
    "QuestionText": "Form field<br>",
    "DefaultChoices": False,
    "DataExportTag": "Q2",
    "QuestionType": "TE",
    "Selector": "FORM",
    "Configuration": {
        "QuestionDescriptionOption": "UseText"
    },
    "QuestionDescription": "Form field",
    "Choices": {
        "1": {
            "Display": "Choice 1"
        },
        "2": {
            "Display": "Choice 2"
        },
        "3": {
            "Display": "Choice 3"
        }
    },
    "ChoiceOrder": [
        "1",
        "2",
        "3"
    ],
    "Validation": {
        "Settings": {
            "ForceResponse": "OFF",
            "Type": None
        }
    },
    "GradingData": [],
    "Language": [],
    "NextChoiceId": 4,
    "NextAnswerId": 1,
    "SearchSource": {
        "AllowFreeResponse": "False"
    },
    "QuestionID": "QID4",
    "QuestionText_Unsafe": "Form field<br>"
},

#For a drop list question
{
    "ChoiceOrder": [
        "1",
        "2"
    ],
    "Choices": {
        "1": {
            "Display": "Yes"
        },
        "2": {
            "Display": "No"
        }
    },
    "Configuration": {
        "TextPosition": "inline"
    },
    "Language": [],
    "QuestionDescription": "testQ",
    "QuestionText": "What's your name?",
    "QuestionType": "MC",
    "Selector": "DL",
    "SubSelector": "TX",
    "Validation": {
        "Settings": {
            "ForceResponse": "OFF",
            "ForceResponseType": "ON",
            "Type": "None"
        }
    },
    "DataExportTag": "Q8",
    "QuestionID": "QID8",
    "QuestionText_Unsafe": "What's your name?"
},

#
{
    "QuestionText": "Text question<br><br>",
    "DefaultChoices": False,
    "DataExportTag": "Q3",
    "QuestionType": "DB",
    "Selector": "TB",
    "Configuration": {
        "QuestionDescriptionOption": "UseText"
    },
    "QuestionDescription": "Text question",
    "ChoiceOrder": [],
    "Validation": {
        "Settings": {
            "Type": "None"
        }
    },
    "GradingData": [],
    "Language": [],
    "NextChoiceId": 4,
    "NextAnswerId": 1,
    "QuestionID": "QID5",
    "QuestionText_Unsafe": "Text question<br><br>"
}

MatrixQuestion = {
    "QuestionText": "Matrix question",
    "DefaultChoices": False,
    "QuestionType": "Matrix",
    "Selector": "Likert",
    "Configuration": {
        "QuestionDescriptionOption": "UseText",
        "TextPosition": "inline",
        "ChoiceColumnWidth": 25,
        "RepeatHeaders": "none",
        "MobileFirst": True,
        "WhiteSpace": "OFF"
    },
    "QuestionDescription": "Matrix question",
    "Choices": {
        "1": {
            "Display": "Click to write Statement 1:Right",
            "ExclusiveAnswer": True
        },
        "2": {
            "Display": "Click to write Statement 2:Right",
            "ExclusiveAnswer": True
        }
    },
    "ChoiceOrder": [
        1,
        2
    ],
    "Validation": {
        "Settings": {
            "ForceResponse": "OFF",
            "Type": "None"
        }
    },
    "GradingData": [],
    "Language": [],
    "NextChoiceId": 3,
    "NextAnswerId": 4,
    "Answers": {
        "1": {
            "Display": "Answer 1",
            "ExclusiveAnswer": True
        },
        "2": {
            "Display": "Answer 2",
            "ExclusiveAnswer": True
        },
        "3": {
            "Display": "Answer 3",
            "ExclusiveAnswer": True
        }
    },
    "AnswerOrder": [
        1,
        2,
        3
    ],
    "ChoiceDataExportTags": False,
    "AnswerColumns": 3,
    "SubSelector": "MultipleAnswer",
    "ChoiceGroups": {
        "cg_1": {
            "ChoiceGroupOrder": None,
            "GroupLabel": "Group",
            "Options": []
        }
    },
    "ChoiceGroupOrder": [
        1,
        2,
        "cg_1"
    ],
    "QuestionText_Unsafe": "Matrix question"
}

tableQuestion = {
    "QuestionText": "What's your name?<br>",
    "DefaultChoices": False,
    "DataExportTag": "Q2",
    "QuestionType": "TE",
    "Selector": "SL",
    "Configuration": {
        "QuestionDescriptionOption": "UseText"
    },
    "QuestionDescription": "What's your score?",
    "Validation": {
        "Settings": {
            "ForceResponse": "OFF",
            "Type": "None"
        }
    },
    "GradingData": [],
    "Language": [],
    "NextChoiceId": 4,
    "NextAnswerId": 1,
    "QuestionText_Unsafe": "What's your score?<br>"
}