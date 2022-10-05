from flask import Flask, url_for
from twilio.twiml.voice_response import VoiceResponse
from app_helpers import twiml

app = Flask(__name__)

@app.route("/")
def hello():
  return "Hello World!"

@app.route('/ivr/welcome', methods=['POST'])
def welcome():
    response = VoiceResponse()
    with response.gather(
        num_digits=1, action=url_for('menu'), method="POST"
    ) as g:
        g.say(message="Thanks for calling Acko" +
              "Please press 1 for auto insurance." +
              "Press 2 for other products.", loop=3)
    return twiml(response)

if __name__ == "__main__":
  app.run()
