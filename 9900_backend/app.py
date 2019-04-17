
from flask import Flask, jsonify, make_response, request
from IR_model import ir_model
from feedback import update
from keywords_extraction import keywords_extracted_tfidf
import string
import requests
import json
import numpy as np
app = Flask(__name__)


#
# headers = {'content-type':'application/json'}
# url="http://127.0.0.1:5050/register"

l1=[['comp9444','9444','neural networks and deep learning'],'Monday 6-9pm, Weeks 1-9,11-13 ','Central Lecture Block 7 ',' http://www.cse.unsw.edu.au/~cs9444']
l2=[['comp9414','9414','artificial intelligence'],'Wed 10:00 - 13:00 (Weeks:11), Fri 10:00 - 13:00 (Weeks:1-8,10)','Sir John Clancy Auditorium (K-C24-G17)',' http://www.cse.unsw.edu.au/~cs9414']
l3=[['comp1531','1531','software engineering fundamentals'],'Tue 16:00 - 18:00 (Weeks:1-10), Wed 14:00 - 16:00 (Weeks:1-10)','Keith Burrows Theatre (K-J14-G5)',' http://www.cse.unsw.edu.au/~cs1531']
obj_1=[l1,l2,l3]

intent_1={}
save=[None,None]
def int():
    for i in obj_1:
        for j in i[0]:
            intent_1[j]='obj'
        for k in range(1,len(i)):
            intent_1[j]='obj'
    intent_1['time'] = 'int'
    intent_1['where'] = 'int'
    intent_1['web'] = 'int'
    intent_1['when']='int'
    intent_1['location']='int'
    intent_1['place']='int'
    # intent_1['website']='int'


@app.route('/webhook', methods=['POST'])
def webhook():
    """This method handles the http requests for the Dialogflow webhook
    This is meant to be used in conjunction with the translate Dialogflow agent
    """

    # Get request parameters
    req = request.get_json(force=True)
    action = req.get('queryResult')
    query = req.get('queryResult').get('queryText')
    context1=req.get('queryResult').get('outputContexts')
    para=req.get('queryResult').get('parameters')

    intent= req.get('queryResult').get('intent').get('displayName')

    print(intent)





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

    if intent == 'place' or intent =='timetable' or intent =='course_web_site' or intent == 'what_about':
        query=query.translate(str.maketrans('','',string.punctuation))
        check=query.split()
        for i in range(0 ,len(check)):
            if 'comp' in check[i]:
                if check[i] != 'comp9444' and  check[i] !='comp9414' and check[i] !='comp1531':
                    ans5='Sorry, we do not have information about this course'
                    ans5={'fulfillmentText': ans5}
                    return make_response(jsonify(ans5))
                else:
                    break
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
    query=query.lower()
    int()
    global save1
    for key in intent_1:
        if key in query:
            if intent_1[key] == 'int':
                save1[0] = key
            else:
                save1[1] = key
    if save1[0] is None:
        return 'what do you want to know about it'
    if save1[1] is None:
        return 'what course do you want to know about?'

    for i in obj_1:
        for j in i[0]:
            if j == save1[1]:
                if save1[0] == 'time' or save1[0] == 'when':
                    return i[1]
                elif save1[0] == 'where' or save1[0] == 'place' or save1[0] == 'location':
                    return i[2]
                elif save1[0] == 'web':
                    return i[3]
    save1 = np.array(save1)
    np.save('save2.npy', save1)
    save1 = np.load('save2.npy')
    save1 = list(save1)





if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

    # app.run(port=8080,debug=True)
