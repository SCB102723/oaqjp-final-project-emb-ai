import requests
import json

def emotion_detector(text_to_analyze):
    if not text_to_analyze or text_to_analyze.strip() == "":
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    headers = {
        "Content-Type": "application/json",
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    payload = {
         "raw_document": {
             "text": text_to_analyze 
                } 
    }

    response = requests.post(url, headers=headers, json=payload)

    #Handle blank input
    if response.status_code == 400:
        return {
            "anger": None,
            "disgust":None,
            "fear": None,
            "joy": None, 
            "sadness": None, 
            "dominant_emotion": None    
        }
        
    result = response.json()

    #Extract emotion scores
    emotions = result["emotionPredictions"][0]["emotion"]
    
    #Find dominant emotion
    dominant_emotion = max(emotions, key=emotions.get)

    #Add dominant emotion to the dictionary
    emotions["dominant_emotion"] = dominant_emotion

    return emotions
