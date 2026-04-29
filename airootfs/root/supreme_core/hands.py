import cv2
import mediapipe as mp
import subprocess
import pyautogui # NEW
import numpy as np # NEW

class SovereignHands:
    def __init__(self):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
        self.mp_draw = mp.solutions.drawing_utils
        self.frame_skip = 0 # i3 Optimization
        self.screen_w, self.screen_h = pyautogui.size() # NEW

    def process_gestures(self, frame):
        # i3 processor optimization: har 3rd frame process karega
        self.frame_skip += 1
        if self.frame_skip % 3 != 0: return

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(rgb_frame)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Logic for Scroll, Pinch & Zoom
                # --- NEW FEATURE ADDED BELOW ---
                index_tip = hand_landmarks.landmark[8]
                thumb_tip = hand_landmarks.landmark[4]
                
                # Mouse move
                mx = np.interp(index_tip.x, [0.1, 0.9], [0, self.screen_w])
                my = np.interp(index_tip.y, [0.1, 0.9], [0, self.screen_h])
                pyautogui.moveTo(self.screen_w - mx, my)
                
                # Pinch click
                h, w, _ = frame.shape
                dist = np.hypot((index_tip.x - thumb_tip.x)*w, (index_tip.y - thumb_tip.y)*h)
                if dist < 30:
                    pyautogui.click()
                    pyautogui.sleep(0.2)
                # --- END OF NEW FEATURE ---
                
                self.mp_draw.draw_landmarks(frame, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)
                print("HANDS: Gesture Detected. Executing OS Command.")

    def overdrive(self):
        """Hardware Level Tuning for i3 8th Gen"""
        print("HANDS: Triggering Peak Performance Mode.")
        subprocess.run(["renice", "-n", "-20", "-p", "1"])
