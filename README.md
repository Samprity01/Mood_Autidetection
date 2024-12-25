This project aims to provide a starting point for understanding how emotions, particularly smiling, can be used to assess behavioral traits. While not a medical tool, it demonstrates the potential for machine learning and computer vision in analyzing human behavior, which could assist in preliminary autism detection in children.

Features
Real-Time Video Processing: Captures live video feed from a webcam.
Facial Emotion Recognition: Detects emotions using a pre-trained deep learning model.
Autism Indicator: Infers a heuristic-based conclusion on the presence of autism.
Web Interface: A Flask-based API and simple frontend to start the detection process.
User-Friendly Interaction: Initiates detection via a web route and provides live feedback via OpenCV's GUI.


Technologies Used

Backend
  TensorFlow: For the pre-trained emotion detection model.
  OpenCV: For real-time video capture and face detection.
  Flask: For the web API and simple frontend.
Frontend
  HTML: Basic template for the interface.
  Css: IN css, we use tailwind.css for aggregate styling.
Pre-Trained Model
  fer2013_mini_XCEPTION: A deep learning model trained on the FER-2013 dataset for emotion detection.


How It Works
  Face Detection: Uses Haar Cascades to detect faces in the video feed.
  Emotion Classification: Processes the detected face with the fer2013_mini_XCEPTION model to identify emotions.
  Smile Detection: Monitors if the emotion detected is "Happy".
  Autism Heuristic: If a smile is detected, the application infers that autism is less likely, otherwise, it suggests that autism might be present.
  Web API: Starts the detection process via a Flask route, while OpenCV's GUI displays real-time processing.



Future Enhancements
  Enhanced Model: Incorporate a more robust model for autism detection, possibly leveraging datasets specific to autism behavior analysis.
  Dataset-Free Analysis: Explore methods for generalized inference without relying solely on emotion detection.
  Multi-Emotion Analysis: Consider multi-label outputs for a more comprehensive behavioral assessment.
  Frontend Improvements: Build a more interactive and detailed user interface for better visualization and user feedback.
  Mobile Support: Extend functionality for mobile devices.
