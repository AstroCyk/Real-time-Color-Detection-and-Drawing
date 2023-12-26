import cv2
import numpy as np
import time

# Open a connection to the webcam (usually the default camera)
cap = cv2.VideoCapture(1)

# Color detection settings for green
lower_color = np.array([40, 40, 40])  # Lower bound for color in HSV format
upper_color = np.array([80, 255, 255])  # Upper bound for color in HSV format


# Line drawing settings
line_thickness = 2  # Adjust the thickness of the line
fade_duration = 1.5  # Time in seconds for the line to disappear
line_color = (255, 255, 255)  # Adjust the color of the detected line (BGR format)

# Initialize variables for line drawing
line_points = []

while True:
    # Read a frame from the webcam
    ret, frame = cap.read()

    # Convert the frame to HSV color space
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Create a mask to extract only the color regions within the specified range
    mask = cv2.inRange(hsv_frame, lower_color, upper_color)

    # Find contours in the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw a line from the detected object
    if len(contours) > 0:
        contour = max(contours, key=cv2.contourArea)  # Use the largest detected contour

        # Get the center of the contour
        M = cv2.moments(contour)
        if M["m00"] != 0:
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])

            # Append the center to the list of points
            line_points.append((cx, cy, time.time()))

    # Draw a smoothed line directly on the frame
    if len(line_points) >= 2:
        for i in range(1, len(line_points)):
            cv2.line(frame, line_points[i - 1][:2], line_points[i][:2], line_color, line_thickness)

    # Remove old points to create a fading effect
    if len(line_points) > 0:
        elapsed_time = time.time() - fade_duration
        while len(line_points) > 0 and line_points[0][2] < elapsed_time:
            line_points.pop(0)

    # Show the resulting frame with the drawn line directly
    cv2.imshow('Result', frame)

    # Exit the loop when the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
