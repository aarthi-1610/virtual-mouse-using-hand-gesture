
# 🖱️ Virtual Mouse Using Hand Gestures
🚀 A Python-based Virtual Mouse that enables users to control their computer cursor using hand gestures, eliminating the need for a physical mouse. The system detects hand gestures through a webcam using Mediapipe, processes them using OpenCV, and performs mouse actions using PyAutoGUI.


📸 How It Works?
-  Webcam Input: Captures real-time video of the user's hand.
-  Hand Detection: Uses Mediapipe to identify hand landmarks.
-  Gesture Recognition: Identifies finger positions for different actions.
-  Mouse Control: Uses PyAutoGUI to move the cursor and execute actions.

🖥️ Hand Landmarks Used:
- Index Finger (8) – Cursor movement
- Thumb (4) – Used for clicking
- Middle Finger (12) – Used for right-click & scrolling
- Ring Finger (16), Pinky Finger (20) – Can be extended for more gestures


🛠️ Technologies Used

- Python-	Programming language for implementation
- OpenCV-	Real-time image processing and video capture
- Mediapipe-	Hand tracking and gesture recognition
- PyAutoGUI-	Simulates mouse control and automation


## 📌 Features
- ✅ Move Cursor – Move your index finger to control the mouse pointer.
- ✅ Left Click – Tap Index Finger & Thumb together.
- ✅ Right Click – Tap Middle Finger & Thumb together.
- ✅ Drag & Drop – Hold Index & Middle Finger together while moving.
- ✅ Scrolling – Move Index & Middle Finger up/down for scrolling.
- ✅ Real-time Hand Tracking – Uses Mediapipe to track hand movements.
- ✅ No External Hardware Required – Works with just a webcam.
