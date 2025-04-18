# Eye-Cursor

The Eye-Tracking Mouse Control project leverages computer vision and facial landmark detection to create a hands-free interface for controlling the mouse pointer and performing click actions using only eye movements. This system utilizes the MediaPipe Face Mesh model to track facial landmarks and detect eye closures in real-time. Using PyAutoGUI, the system translates eye movements into mouse cursor control and triggers left or right clicks based on eye gestures.

Features:

Real-time Eye Tracking: Detects the position of the user's eyes using MediaPipe's Face Mesh solution.

Mouse Movement Control: Moves the on-screen mouse cursor based on the position of the user's eye landmarks.

Left & Right Clicks: Detects eye closure to perform left or right clicks.

Left Eye Closure: Triggers a left-click when the left eye is closed for a sustained period.

Right Eye Closure: Triggers a right-click when the right eye is closed for a sustained period.

Hands-Free Interface: This project enables users to control the computer without needing a physical mouse or keyboard.

Technologies Used

Python,MediaPipe,OpenCV,PyAutoGUI
