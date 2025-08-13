"""
Flask server for Emotion Detection app.
Handles routing, input, and response.
"""
from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector", methods=["GET", "POST"])
def emotion_detector_route():
    """
    Recieves user text, calls emotion_detector, 
    and returns response or error message.
    """
    text_to_analyze = request.values.get('text')
    result = emotion_detector(text_to_analyze)

    if result is None or result.get("dominant_emotion") is None:
        return "Invalid text! Please try again!"

    dominant_emotion = result.get("dominant_emotion", "unknown")
    score = result.get(dominant_emotion, 0)

    response = (
        f"For the given statement, you are feeling {dominant_emotion} "
        f"with a score of {score:.2f}"
    )

    return response

@app.route("/")
def home():
    """
    Renders main HTML page for user interface.
    """
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
