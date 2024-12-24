const videoSelect = document.getElementById("videoSelect") as HTMLSelectElement;
const videoPlayer = document.getElementById("videoPlayer") as HTMLIFrameElement;
const startDetectionButton = document.getElementById("startDetection") as HTMLButtonElement;

// Update video based on selection
videoSelect.addEventListener("change", () => {
  const selectedVideo = videoSelect.value;
  videoPlayer.src = selectedVideo;
});

// Start Emotion Detection
startDetectionButton.addEventListener("click", () => {
  alert(
    "Starting Emotion Detection. Please open the Python backend to process the webcam feed. Press 'q' to stop detection."
  );

  // Make the request to the backend
  fetch("/start_detection")
    .then((response) => response.json())
    .then((data) => {
      console.log(data.message);
    })
    .catch((error) => {
      console.error("Error starting detection:", error);
    });
});
