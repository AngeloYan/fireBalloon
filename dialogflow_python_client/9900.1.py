
from flask import Flask, jsonify, make_response, request
import json
app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    """This method handles the http requests for the Dialogflow webhook
    This is meant to be used in conjunction with the translate Dialogflow agent
    """

    # Get request parameters
    req = request.get_json(force=True)
    action = req.get('queryResult').get('action')
    query = req.get('queryResult').get('queryText')

    intent= req.get('queryResult').get('intent').get('displayName')
    if intent=='what is v2':
        intent='ok'

    print(intent)
    print(query)

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
    res = {'fulfillmentText': intent}
               # 'outputContexts': req['queryResult']['outputContexts']}
    # else:
    #     # If the request is not to the translate.text action throw an error
    #     log.error('Unexpected action requested: %s', json.dumps(req))
    #     res = {'speech': 'error', 'displayText': 'error'}

    return make_response(jsonify(res))
# @app.route('/')
# def hello_world():
#     return 'hello world'

@app.route('/register', methods=['POST'])
def register():
    # print(request.headers)
    # print(request.form)
    # print(request.form['name'])
    # print(request.form.get('name'))
    # print(request.form.getlist('name'))
    # print(request.form.get('nickname', default='little apple'))
    # #do something else
    # #
    # #
    message ={'fullfilment':''}
    return message

if __name__ == '__main__':
    app.run(port=8080,debug=True)
