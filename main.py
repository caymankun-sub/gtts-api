from flask import Flask, request, Response
from gtts import gTTS
import base64

app = Flask(__name__)

@app.route('/synthesize', methods=['POST'])
def synthesize_text():
    text = request.json.get('text', '')  # POSTリクエストからテキストを取得

    # Google Text-to-Speechを使用して音声を生成
    tts = gTTS(text=text, lang='ja')
    tts.save('output.mp3')

    # 生成された音声ファイルをbase64エンコード
    with open('output.mp3', 'rb') as f:
        audio_bytes = base64.b64encode(f.read()).decode('utf-8')

    # base64エンコードされた音声データをdata URL形式にしてレスポンスとして返す
    response_data = f"data:audio/mp3;base64,{audio_bytes}"
    return Response(response=response_data, status=200)

if __name__ == '__main__':
    app.run()
