
from flask import Flask, jsonify, make_response, request
from IR_model import ir_model
from feedback import update
from keywords_extraction import keywords_extracted_tfidf
import requests
import json
app = Flask(__name__)


#
# headers = {'content-type':'application/json'}
# url="http://127.0.0.1:5050/register"

l1=['comp9444','Monday 6-9pm, Weeks 1-9,11-13 ','Central Lecture Block 7 ',' http://www.cse.unsw.edu.au/~cs9444']
l2=['comp9414','Wed 10:00 - 13:00 (Weeks:11), Fri 10:00 - 13:00 (Weeks:1-8,10)','Sir John Clancy Auditorium (K-C24-G17)',' http://www.cse.unsw.edu.au/~cs9414']
l3=['comp1531','Tue 16:00 - 18:00 (Weeks:1-10), Wed 14:00 - 16:00 (Weeks:1-10)','Keith Burrows Theatre (K-J14-G5)',' http://www.cse.unsw.edu.au/~cs1531']
obj_1=[l1,l2,l3]

intent_1={}
save=[None,None]
def int():
    for i in obj_1:
        for j in i:
            intent_1[j]='obj'
    intent_1['time'] = 'int'
    intent_1['place'] = 'int'
    intent_1['web'] = 'int'


@app.route('/webhook', methods=['POST'])
def webhook():
    """This method handles the http requests for the Dialogflow webhook
    This is meant to be used in conjunction with the translate Dialogflow agent
    """

    # Get request parameters
    req = request.get_json(force=True)
    action = req.get('queryResult').get('action')
    query = req.get('queryResult').get('queryText')
    # context=req.get('queryResult').get('outputContexts')
    para=req.get('queryResult').get('parameters')

    intent= req.get('queryResult').get('intent').get('displayName')


    if intent == 'Default Fallback Intent':

        ans1=ir_model(query)
        ans1 = {'fulfillmentText': ans1}
        return make_response(jsonify(ans1))



    if intent == 'feedback':
        ans3 = update(query)
        ans3 = {'fulfillmentText': ans3}
        return make_response(jsonify(ans3))

    if intent == 'Default Welcome Intent':
        ans4 = keywords_extracted_tfidf()
        ans4 = {'fulfillmentText': ans4}
        return make_response(jsonify(ans4))

    if intent == 'place' or 'timetable' or 'course web site':
        ans2 = context(query)
        ans2 = {'fulfillmentText': ans2}
        return make_response(jsonify(ans2))




    print(query)
    # print(context)
    print(para)


    # Check if the request is for the translate action
    # if action == 'translate.text':
    #     # Get the parameters for the translation
    #     text = req['queryResult']['parameters'].get('text')
    #     source_lang = req['queryResult']['parameters'].get('lang-from')
    #     target_lang = req['queryResult']['parameters'].get('lang-to')
    #
    #     # Fulfill the translation and get a response
    #     output = translate(text, source_lang, target_lang)
    #
    #     # Compose the response to Dialogflow
    ans = {'fulfillmentText': ans}
               # 'outputContexts': req['queryResult']['outputContexts']}
    # else:
    #     # If the request is not to the translate.text action throw an error
    #     log.error('Unexpected action requested: %s', json.dumps(req))
    #     res = {'speech': 'error', 'displayText': 'error'}


    # return make_response(jsonify(ans))
# @app.route('/')
# def hello_world():
#     return 'hello world'

# @app.route('/register', methods=['POST'])
# def register():
#     # print(request.headers)
#     # print(request.form)
#     # print(request.form['name'])
#     # print(request.form.get('name'))
#     # print(request.form.getlist('name'))
#     # print(request.form.get('nickname', default='little apple'))
#     # #do something else
#     # #
#     # #
#     # message ={'fullfilment':''}
#     return 'okk'

def context(query):
    int()
    for key in intent_1:
        if  key in query:
            if intent_1[key] == 'int':
                save[0] = key
            else:
                save[1] = key
    if save[0] is None:
        return 'what do you want to know about it'
    if save[1] is None:
        return 'what course do you ask'
    for i in obj_1:
        for j in i:
            if j == save[1]:
                if save[0] == 'time':
                    return i[1]
                elif save[0] == 'place':
                    return i[2]
                elif save[0] == 'web':
                    return i[3]





if __name__ == '__main__':
    app.run(port=8080,debug=True)
