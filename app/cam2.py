import pyvirtualcam
import cv2

cap = cv2.VideoCapture(0)

fmt = pyvirtualcam.PixelFormat.BGR
with pyvirtualcam.Camera(width=720, height=480, fps=20, fmt=fmt) as cam:
    while True:
        ret_val, frame = cap.read()
        frame = cv2.resize(frame, (720, 480), interpolation=cv2.BORDER_DEFAULT)
        # frameFlipH = cv2.flip(frame, 1)
        cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        cv2.imshow("cam2", frame)
        cam.send(frame)
        cam.sleep_until_next_frame()
        if cv2.waitKey(1) == 27:
            break # esc to quit
    cv2.destroyAllWindows()