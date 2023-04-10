
import cv2
import base64
import config
from importlib import reload
import numpy as np

cam = cv2.VideoCapture(0)

def get_image():
    ret, image = cam.read()
    image = overlay_cone(image)
    ret, buf = cv2.imencode('.jpg', image)
    byts = buf.tobytes()
    return base64.b64encode(byts)

def overlay_cone(image):
    reload(config)

    x_offset = config.OFFSET_LEFT
    y_offset = config.OFFSET_TOP

    # image blending from https://stackoverflow.com/a/14102014/10372825
    s_img = cv2.imread("/home/ubuntu/psychmem/cone_image.png", -1)

    y1, y2 = y_offset, y_offset + s_img.shape[0]
    x1, x2 = x_offset, x_offset + s_img.shape[1]

    alpha_s = s_img[:, :, 3] / 255.0
    alpha_l = 1.0 - alpha_s

    for c in range(0, 3):
        image[y1:y2, x1:x2, c] = (alpha_s * s_img[:, :, c] +
                                  alpha_l * image[y1:y2, x1:x2, c])

    return image

def cleanup():
    cam.release()
