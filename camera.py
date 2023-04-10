
import cv2
import base64

cam = cv2.VideoCapture(0)

def get_image():
    ret, image = cam.read()
    ret, buf = cv2.imencode('.jpg', image)
    byts = buf.tobytes()
    return base64.b64encode(byts)

def cleanup():
    cam.release()
