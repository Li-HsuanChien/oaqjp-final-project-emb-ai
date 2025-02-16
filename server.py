"""docstring
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
app = Flask("Emotion Detection")

@app.route("/emotionDetector", )
def emotiondetector():
    """docsting
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    anger_score = response['anger']
    disgust_score = response['disgust']
    fear_score = response['fear']
    joy_score = response['joy']
    sadness_score = response['sadness']
    dominant_emotion = response['dominant_emotion']
    if anger_score is None:
        return "Invalid text! Please try again!"
    return {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,                
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion
            }

@app.route("/")
def render_index_page():
    """docsting
    """
    return render_template("index.html", )
if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5004)
    