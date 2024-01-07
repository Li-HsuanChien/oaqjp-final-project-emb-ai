"""_summary_: Detects emotion with text, made to import to """
import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    Headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_text = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = input_text, headers = Headers)
    formatted_response = json.loads(response.text)
    
    if response.status_code == 200:
        anger_score = formatted_response["emotionPredictions"][0]["emotion"]["anger"]
        disgust_score = formatted_response["emotionPredictions"][0]["emotion"]["disgust"]
        fear_score = formatted_response["emotionPredictions"][0]["emotion"]["fear"]
        joy_score = formatted_response["emotionPredictions"][0]["emotion"]["joy"]
        sadness_score = formatted_response["emotionPredictions"][0]["emotion"]["sadness"]
        score_list = [anger_score, disgust_score, fear_score, joy_score, sadness_score]
        if anger_score == max(score_list):
            dominant_emotion = "anger"
        elif disgust_score == max(score_list):
            dominant_emotion = "disgust"
        elif fear_score == max(score_list):
            dominant_emotion = "fear"
        elif joy_score == max(score_list):
            dominant_emotion = "joy"
        elif sadness_score == max(score_list):
            dominant_emotion = 'sadness'
    elif response.status_code == 400:
        anger_score = None
        disgust_score = None
        fear_score = None
        joy_score = None
        sadness_score = None
        dominant_emotion = None
    return {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,                
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion
            }
            
"""
from EmotionDetection.emotion_detection import emotion_detector
emotion_detector("I hate working long hours.")
"""
    