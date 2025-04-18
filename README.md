# Eye-Cursor
Overview
The Eye-Tracking Mouse Control project leverages computer vision and facial landmark detection to create a hands-free interface for controlling the mouse pointer and performing click actions using only eye movements. This system utilizes the MediaPipe Face Mesh model to track facial landmarks and detect eye closures in real-time. Using PyAutoGUI, the system translates eye movements into mouse cursor control and triggers left or right clicks based on eye gestures.

Features
Real-time Eye Tracking: Detects the position of the user's eyes using MediaPipe's Face Mesh solution.

Mouse Movement Control: Moves the on-screen mouse cursor based on the position of the user's eye landmarks.

Left & Right Clicks: Detects eye closure to perform left or right clicks.

Left Eye Closure: Triggers a left-click when the left eye is closed for a sustained period.

Right Eye Closure: Triggers a right-click when the right eye is closed for a sustained period.

Hands-Free Interface: This project enables users to control the computer without needing a physical mouse or keyboard.

Technologies Used
Python: The primary programming language.

MediaPipe: For detecting facial landmarks and tracking eye movements.

OpenCV: For capturing video feed and processing frames.

PyAutoGUI: For controlling the mouse cursor and simulating mouse clicks.

How It Works
Face Mesh Detection: The MediaPipe Face Mesh model detects and tracks facial landmarks in real-time.

Eye Movement Detection: By analyzing the vertical distance between specific eye landmarks, the program determines whether the user's eye is closed.

Mouse Control: The system maps the eye's position to the screen and moves the cursor accordingly. A click event (left or right) is triggered if the eye closure lasts for a predefined threshold time (1 second).

Threshold Adjustments: Parameters such as eye closure sensitivity and time delay before triggering a click can be adjusted for different user needs.
