from flask import Flask, request
import openai
import os

api_key = os.getenv('OPENAI_KEY')
openai.api_key = api_key

app = Flask(__name__)
#print(openai.Model.list())

@app.route('/')
def index():
    return "hello"

@app.route('/check', methods=['POST', 'GET'])
def check():
    q = request.args.get('q')
    if q is None:
      q = request.data.decode()
    if q is None or q == '':
      result = 'No prompt given'
    
    print(q)
    prompt = "As an impressionable yet polite person, state JUST Yes or No (and why) whether you are OK with the following up until ##: " + q + " ##"
    print(prompt)
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[{"role":"user", "content": prompt}])
    return response.choices[0].message.content

app.run(host='0.0.0.0', port=8080)

