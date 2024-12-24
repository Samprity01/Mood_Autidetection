import numpy as np
import cv2
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
from flask import Flask, render_template, jsonify
import threading

app = Flask(__name__)

# Load pre-trained emotion model
emotion_model = load_model('fer2013_mini_XCEPTION.102-0.66.hdf5')
emotion_dict = {0: 'Angry', 1: 'Disgust', 2: 'Fear', 3: 'Happy', 4: 'Sad', 5: 'Surprise', 6: 'Neutral'}

# Haarcascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

class EmotionProcessor:
    def __init__(self):
        self.smile_detected = False

    def process_frame(self, img):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(
            gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE
        )
        for (x, y, w, h) in faces:
            face = gray[y:y + h, x:x + w]
            face = cv2.resize(face, (48, 48))
            face = face.astype("float") / 255.0
            face = img_to_array(face)
            face = np.expand_dims(face, axis=0)

            prediction = emotion_model.predict(face)
            emotion_label = np.argmax(prediction)
            emotion = emotion_dict[emotion_label]

            if emotion == "Happy":
                self.smile_detected = True

        return img

# Function to start video processing (run in a separate thread)
def start_video_processing():
    video_capture = cv2.VideoCapture(0)
    processor = EmotionProcessor()

    while True:
        ret, frame = video_capture.read()
        if not ret:
            break

        processed_frame = processor.process_frame(frame)
        
        # To handle camera feed processing
        cv2.imshow('Emotion Detection', processed_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()

    # Output result
    if processor.smile_detected:
        return "Smile Detected: The child is likely not autistic."
    else:
        return "No Smile Detected: Autism might be present."

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/start_detection", methods=["GET"])
def start_detection():
    # Start the emotion detection process in a separate thread
    detection_thread = threading.Thread(target=start_video_processing)
    detection_thread.start()
    return jsonify({"message": "Emotion Detection Started. Please open the Python backend to process the webcam feed."})

if __name__ == "__main__":
    app.run(debug=True)
