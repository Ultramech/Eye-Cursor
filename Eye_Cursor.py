import pyautogui
import cv2
import mediapipe as mp
import time

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(static_image_mode=False, refine_landmarks=True)
mp_drawing = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
screen_w, screen_h = pyautogui.size()
print(screen_w, screen_h)
pyautogui.FAILSAFE = False

left_eye_closed_time = None
right_eye_closed_time = None

# Threshold for eye closure (vertical distance between landmarks)
eye_threshold = 0.02  # Increase this if it's too sensitive

while True:
    res, img = cap.read()
    img = cv2.flip(img, 1)
    img_RGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    h, w, _ = img.shape

    results = face_mesh.process(img_RGB)

    if results.multi_face_landmarks:
        landmarks = results.multi_face_landmarks[0].landmark
        for id, landmark in enumerate(landmarks[474:478]):
            x = int(landmark.x * w)
            y = int(landmark.y * h)

            cv2.circle(img, (x, y), 3, (255, 255, 0), -1)

            if id == 1:
                screen_x = int(landmark.x * screen_w * 1.5)
                screen_y = int(landmark.y * screen_h * 1.5)
                pyautogui.moveTo(screen_x, screen_y)

            left = [landmarks[145], landmarks[159]]

            for landmark in left:
                x = int(landmark.x * w)
                y = int(landmark.y * h)

                cv2.circle(img, (x, y), 3, (255, 255, 0), -1)
                eye_diff = abs(left[0].y - left[1].y)

                if eye_diff < eye_threshold:
                    if left_eye_closed_time is None:
                        left_eye_closed_time = time.time()
                    elif time.time() - left_eye_closed_time > 1:  # Increased time threshold to avoid rapid clicks
                        pyautogui.click()
                        left_eye_closed_time = None
                else:
                    left_eye_closed_time = None

            right = [landmarks[374], landmarks[378]]

            for landmark in right:
                x = int(landmark.x * w)
                y = int(landmark.y * h)

                eye_diff_right = abs(right[0].y - right[1].y)

                if eye_diff_right < eye_threshold:
                    if right_eye_closed_time is None:
                        right_eye_closed_time = time.time()
                    elif time.time() - right_eye_closed_time > 1:  # Increased time threshold
                        pyautogui.rightClick()
                        right_eye_closed_time = None
                else:
                    right_eye_closed_time = None

        cv2.imshow("Eye Cursor", img)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
