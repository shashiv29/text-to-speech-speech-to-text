from flask import Flask, request, jsonify,render_template
import os
from flask_cors import CORS, cross_origin

import textToSPeech
import speechToText
from com_in_ineuron_ai_utils.utils import decodeSound
os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
CORS(app)

@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')

@app.route("/texttospeech.html", methods=['GET'])
@cross_origin()
def homespeech():
    return render_template('texttospeech.html')

@app.route("/speechtotext.html", methods=['GET'])
@cross_origin()
def hometext():
    return render_template('speechtotext.html')

@app.route("/predictspeech", methods=['POST'])
@cross_origin()
def predictRoutespeech():
    data = request.json['data']
    result = textToSPeech.text2Speech(data)
    return {"data" : result.decode("utf-8")}


@app.route("/predicttext", methods=['POST'])
@cross_origin()
def predictRoutetext():
    image = request.json['sound']
    decodeSound(image, "audio123.wav")
    result = speechToText.speech2Text("audio123.wav")
    return jsonify({"Result" : str(result)})



#port = int(os.getenv("PORT"))
if __name__ == "__main__":
    #app.run(host='0.0.0.0', port=port)
    app.run(host='0.0.0.0', port=4000, debug=True)

#My name is John Paul Jones. I live in New York, United States. I love to play baseball.