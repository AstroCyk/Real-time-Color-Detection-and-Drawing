# Real-time Color Detection and Drawing

This Python application uses OpenCV to perform real-time color detection with a webcam. It draws a fading line on the detected object within a specified color range,
creating dynamic and interactive visual effects.

## Features
- Live color detection using HSV format
- Smoothed line drawing on the detected object
- Fading effect for a visually appealing experience

## How to Use
1. Install the required dependencies:
   ```bash
   pip install opencv-python numpy
   ```

2. Run the application:
   ```bash
   python color_detection_and_drawing.py
   ```

3. Press 'q' to exit the application.

## Customization
- Adjust the color range (`lower_color` and `upper_color` variables) for different detection scenarios.
- Modify line drawing settings, such as thickness and color, according to your preferences.

Feel free to integrate this code into your computer vision projects for an engaging visual experience!
