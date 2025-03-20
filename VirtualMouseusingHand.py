import cv2
import mediapipe as mp
import pyautogui

# Initialize Mediapipe Hand module
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# Capture video from webcam
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
screen_width, screen_height = pyautogui.size()

clicking = False  # To track dragging state

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break
    
    frame = cv2.flip(frame, 1)  # Flip for mirror effect
    h, w, c = frame.shape  # Get frame dimensions
    
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Get finger landmark positions
            index_finger = hand_landmarks.landmark[8]  # Index finger tip
            middle_finger = hand_landmarks.landmark[12]  # Middle finger tip
            thumb = hand_landmarks.landmark[4]  # Thumb tip

            x, y = int(index_finger.x * w), int(index_finger.y * h)
            thumb_x, thumb_y = int(thumb.x * w), int(thumb.y * h)
            middle_x, middle_y = int(middle_finger.x * w), int(middle_finger.y * h)

            # Move cursor to index finger position
            pyautogui.moveTo(x * screen_width // w, y * screen_height // h)

            # Left-Click: When Index and Thumb are close
            if abs(thumb_x - x) < 20 and abs(thumb_y - y) < 20:
                pyautogui.click()

            # Right-Click: When Middle finger and Thumb are close
            elif abs(thumb_x - middle_x) < 20 and abs(thumb_y - middle_y) < 20:
                pyautogui.rightClick()

            # Drag and Drop: When Index and Middle fingers are close
            elif abs(index_finger.x - middle_finger.x) < 0.05 and abs(index_finger.y - middle_finger.y) < 0.05:
                if not clicking:
                    pyautogui.mouseDown()
                    clicking = True
                else:
                 if clicking:
                    pyautogui.mouseUp()
                    clicking = False

            # Scrolling: Moving Index and Middle Fingers up/down together
            elif abs(index_finger.y - middle_finger.y) < 0.05:  # Fingers aligned
                if middle_y < y:  # Move fingers up
                    pyautogui.scroll(5)  # Scroll up
                elif middle_y > y:  # Move fingers down
                    pyautogui.scroll(-5)  # Scroll down

            # Draw hand landmarks
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    cv2.imshow("Virtual Mouse", frame)
    
    if cv2.waitKey(1) & 0xFF == 27:  # Press 'Esc' to exit
        break

cap.release()
cv2.destroyAllWindows()
