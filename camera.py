import cv2
import numpy as np


class VideoCamera(object):
    def __init__(self):
        # Using OpenCV to capture from device 0. If you have trouble capturing
        # from a webcam, comment the line below out and use a video file
        # instead.
        self.video = cv2.VideoCapture(0)
        # If you decide to use video.mp4, you must have this file in the folder
        # as the main.py.
        # self.video = cv2.VideoCapture('video.mp4')

    def __del__(self):
        self.video.release()

    def get_frame(self):
        success, image = self.video.read()
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        hsv[:, :, 2] = (255 - hsv[:, :, 2]) * 0.5
        lighter_image = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
        combined_image = np.concatenate((image, lighter_image), axis=1)

        ret, jpeg = cv2.imencode('.jpg', combined_image)
        return jpeg.tobytes()
