from flask import Flask, request, Response
from gtts import gTTS
import base64
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def synthesize_text():
    text = request.args.get('text', '')  # URLクエリパラメータからテキストを取得

    # Google Text-to-Speechを使用して音声を生成
    tts = gTTS(text=text, lang='ja')
    tts.save('/tmp/output.mp3')

    # 生成された音声ファイルをbase64エンコード
    with open('/tmp/output.mp3', 'rb') as f:
        audio_bytes = base64.b64encode(f.read()).decode('utf-8')

    # base64エンコードされた音声データをdata URL形式にしてレスポンスとして返す
    response_data = f"data:audio/mp3;base64,{audio_bytes}"
    return Response(response=response_data, status=200)
    
@app.route('/e', methods=['GET'])
def synthesize_text():
    text = request.args.get('text', '')  # URLクエリパラメータからテキストを取得

    # Google Text-to-Speechを使用して音声を生成
    tts = gTTS(text=text, lang='ja')
    tts.save('output.mp3')

    # 生成された音声ファイルをbase64エンコード
    with open('output.mp3', 'rb') as f:
        audio_bytes = base64.b64encode(f.read()).decode('utf-8')

    # base64エンコードされた音声データをdata URL形式にしてレスポンスとして返す
    audio_data_uri = f"data:audio/mp3;base64,{audio_bytes}"
    audio_tag = f"<audio controls src='{audio_data_uri}'></audio>"
    return audio_tag

if __name__ == '__main__':
    app.run()
