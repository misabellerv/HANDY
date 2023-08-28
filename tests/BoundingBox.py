import cv2
import mediapipe as mp

# mediapipe init
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# webcam init
cap = cv2.VideoCapture(0)

with mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # BGR to RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        results = hands.process(rgb_frame)
        
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                
                # hands coordinates
                landmarks = []
                for landmark in hand_landmarks.landmark:
                    h, w, _ = frame.shape
                    x, y = int(landmark.x * w), int(landmark.y * h)
                    landmarks.append((x, y))
                
                # Bounding box
                x_min = min(landmarks, key=lambda x: x[0])[0]
                x_max = max(landmarks, key=lambda x: x[0])[0]
                y_min = min(landmarks, key=lambda x: x[1])[1]
                y_max = max(landmarks, key=lambda x: x[1])[1]

                # Resize bounding box 
                scale = 1.2
                width = (x_max - x_min)* 3.5
                height = y_max - y_min
                x_min = max(0, x_min - int(width * (scale - 1) / 2))
                x_max = min(frame.shape[1], x_max + int(width * (scale - 1) / 2))
                y_min = max(0, y_min - int(height * (scale - 1) / 2))
                y_max = min(frame.shape[0], y_max + int(height * (scale - 1) / 2))
                
                # draw bounding box
                cv2.rectangle(frame, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)
        
        # Show resulting image
        cv2.imshow('Hand Detection', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
