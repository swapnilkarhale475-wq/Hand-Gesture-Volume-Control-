import cv2
import mediapipe as mp
import numpy as np
import pyautogui

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)

    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    if result.multi_hand_landmarks:
        for handLms in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(img, handLms, mp_hands.HAND_CONNECTIONS)

            h, w, _ = img.shape

            x1, y1 = int(handLms.landmark[4].x * w), int(handLms.landmark[4].y * h)
            x2, y2 = int(handLms.landmark[8].x * w), int(handLms.landmark[8].y * h)

            length = np.hypot(x2 - x1, y2 - y1)

            # 🎧 Volume control using keyboard
            if length > 150:
                pyautogui.press("volumeup")
            elif length < 50:
                pyautogui.press("volumedown")

    cv2.imshow("YouTube Volume Control", img)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
