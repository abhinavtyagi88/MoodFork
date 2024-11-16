from flask import Flask, render_template, jsonify, Response
from emotion_detector import detect_emotion
import cv2

app = Flask(__name__)
cap = cv2.VideoCapture(0)

@app.route('/get_live_preview')
def get_live_preview():
    if not cap.isOpened():
        return Response("Camera not available", status=503)
    ret, frame = cap.read()
    if not ret:
        return Response("Unable to read frame", status=500)

    _, buffer = cv2.imencode('.jpg', frame)
    response= Response(buffer.tobytes(), mimetype='image/jpeg')
    response.headers["Cache-Control"] = "no-store"
    return response

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/allrecipe')
def allrecipe():
    return render_template('allrecipe.html')

@app.route('/detect_emotion', methods=['GET'])
def detect_emotion_route():
    emotion, food_item = detect_emotion()
    return jsonify({'emotion': emotion, 'food': food_item})

if __name__ == '__main__':
    # print(app.url_map)
    app.run(debug=True)