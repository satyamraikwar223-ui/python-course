import cv2
import numpy as np
import pyautogui

# Set the resolution and frame rate
SCREEN_SIZE = (1920, 1080)
FPS = 20.0

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter("output.avi", fourcc, FPS, SCREEN_SIZE)

print("Recording started. Press 'q' to stop.")

try:
    while True:
        # Take a screenshot
        img = pyautogui.screenshot()

        # Convert the screenshot to a numpy array
        frame = np.array(img)

        # Convert colors from BGR to RGB
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Write the frame to the file
        out.write(frame)

        # Stop recording when 'q' is pressed
        if cv2.waitKey(1) == ord("q"):
            break
finally:
    # Release everything when finished
    out.release()
    cv2.destroyAllWindows()
    print("Recording saved as output.avi")
