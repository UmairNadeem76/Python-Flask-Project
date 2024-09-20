"""
Server script for emotion detection using Flask and Watson NLP API.
This module provides an endpoint to analyze emotions in the given text.
"""

from flask import Flask, request, jsonify, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector', methods=['POST'])
def detect_emotion():
    """
    Detect emotions in the given text via POST request.

    Expects:
        JSON body containing 'text' field.

    Returns:
        Response: A JSON response with emotion scores or an error message.
    """
    data = request.json
    text_to_analyze = data.get('text', '')

    # Call the emotion detection function
    result, status_code = emotion_detector(text_to_analyze)

    if status_code == 400:
        # Handle blank or invalid input
        return jsonify({'message': 'Invalid text! Please try again.'}), 400

    # Prepare the formatted response
    formatted_response = (
        f"For the given statement, the system response is 'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, 'fear': {result['fear']}, 'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}."
        )


    # Return the formatted response
    return jsonify({'message': formatted_response}), 200

@app.route('/')
def home():
    """
    Render the homepage with the form to input text for emotion detection.

    Returns:
        HTML page: The index.html file to be rendered.
    """
    return render_template('index.html')

if __name__ == '__main__':
    # Main block to run the Flask app on localhost at port 5000.
    app.run(host='localhost', port=5000)
    