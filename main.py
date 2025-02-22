import cv2
import numpy as np

cap = cv2.VideoCapture(0)
last_mean = 0
detected_motion = False
frame_rec_count = 0
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

while (True):
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    result = np.abs(np.mean(gray) - last_mean)
    print(result)
    last_mean = np.mean(gray)

    if result > 0.3:
        print("Motion detected!")
        print("Started recording.")
        detected_motion = True

    if detected_motion:
        out.write(frame)
        frame_rec_count = frame_rec_count + 1

    if (cv2.waitKey(1) & 0xFF == ord('q')) or frame_rec_count == 240:
        break

cap.release()
cv2.destroyAllWindows()
