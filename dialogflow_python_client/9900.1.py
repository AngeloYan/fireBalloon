
from flask import Flask, jsonify, make_response, request
from IR_model import ir_model
import requests
import json
app = Flask(__name__)


#
# headers = {'content-type':'application/json'}
# url="http://127.0.0.1:5050/register"

l1=['comp9444','time1','place1','web1']
l2=['comp9414','time2','place2','web2']
l3=['comp1531','time3','place3','web3']
obj_1=[l1,l2,l3]

intent_1={}
save=[None,None]
def int():
    for i in obj_1:
        for j in i:
            intent_1[j]='obj'
    intent_1['Time'] = 'int'
    intent_1['Place'] = 'int'
    intent_1['Web'] = 'int'


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


    # if intent=='Default Fallback Intent':
    #
    #     ans=ir_model(query)
    #


    # print(ans)
    print(query)
    # print(context)
    print(para)
    ans = context(query)

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
    print(ans)

    return make_response(jsonify(ans))
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
                if save[0] == 'Time':
                    return i[1]
                elif save[0] == 'Place':
                    return i[2]
                elif save[0] == 'Web':
                    return i[3]





if __name__ == '__main__':
    app.run(port=8080,debug=True)
