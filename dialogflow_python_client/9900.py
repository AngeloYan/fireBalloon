import os
import dialogflow_v2 as dialogflow
from urllib import parse,request
import requests
import json
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:/Users/ltyyu/Downloads/tianyu-a38947071f2f.json"
project_id = 'tianyu-80ba0'
session_id = "1"
audio_file_path = 'my wave file directory name'
texts = 'i like red'
language_code = 'en'


headers = {'content-type':'application/json'}
url="http://127.0.0.1:8888/register"
# data = {
#     'taskId':"11",
#     'shareDir':'sharedir',
#     'url':'url',
#     'name':'Name'
# }
# r = requests.post(url, data=json.dumps(data), headers=headers)
# print(r.text)






def detect_intent_texts(project_id, session_id, texts, language_code):
    """Returns the result of detect intent with texts as inputs.

    Using the same `session_id` between requests allows continuation
    of the conversation."""


    session_client = dialogflow.SessionsClient()

    session = session_client.session_path(project_id, session_id)
    print('Session path: {}\n'.format(session))
    # texts1=texts.split(' ')
    text_input = dialogflow.types.TextInput(
        text=texts, language_code=language_code)

    query_input = dialogflow.types.QueryInput(text=text_input)

    response = session_client.detect_intent(
        session=session, query_input=query_input)

    # for text in texts1:
    #     text_input = dialogflow.types.TextInput(
    #         text=text, language_code=language_code)
    #
    #     query_input = dialogflow.types.QueryInput(text=text_input)
    #
    #     response = session_client.detect_intent(
    #         session=session, query_input=query_input)

    print('=' * 20)
    print('Query text: {}'.format(response.query_result.query_text))
    print('Detected intent: {} (confidence: {})\n'.format(
            response.query_result.intent.display_name,
            response.query_result.intent_detection_confidence))

    if response.query_result.intent.display_name=='what is v2':
        # print('1')
        r = requests.post(url, headers=headers)
        print(r.text)
        response.query_result.fulfillment_text=r.text
    print('Fulfillment text: {}\n'.format(
        response.query_result.fulfillment_text))


detect_intent_texts(project_id, session_id,texts,language_code)