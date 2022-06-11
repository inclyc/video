import cv2

filename = "C:/Users/admin/Desktop/帧差分/源视频/鸟.mp4"
video = cv2.VideoCapture(filename)

out_fps = 30.0
fourcc = cv2.VideoWriter_fourcc('M', 'P', '4', '2')
out1 = cv2.VideoWriter('C:/Users/admin/Desktop/帧差分/目标视频/v3.avi', fourcc, out_fps, (500, 400))
out2 = cv2.VideoWriter('C:/Users/admin/Desktop/帧差分/目标视频/v4.avi', fourcc, out_fps, (500, 400))

lastFrame1 = None
lastFrame2 = None

while video.isOpened():
    (ret, frame) = video.read()
    if not ret:
        break
    frame = cv2.resize(frame, (500, 400), interpolation=cv2.INTER_CUBIC)
    if lastFrame2 is None:
        if lastFrame1 is None:
            lastFrame1 = frame
        else:
            lastFrame2 = frame
            global frameDelta1
            frameDelta1 = cv2.absdiff(lastFrame1, lastFrame2)
        continue

    frameDelta2 = cv2.absdiff(lastFrame2, frame)
    thresh = cv2.bitwise_and(frameDelta1, frameDelta2)
    thresh2 = thresh.copy()
    lastFrame1 = lastFrame2
    lastFrame2 = frame.copy()
    frameDelta1 = frameDelta2

    thresh = cv2.cvtColor(thresh, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(thresh, 25, 255, cv2.THRESH_BINARY)[1]

    # thresh = cv2.dilate(thresh, None, iterations=3)
    # thresh = cv2.erode(thresh, None, iterations=1)

    cnts, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


    for c in cnts:

        if cv2.contourArea(c) < 300:
            continue

        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow("frame", frame)
    cv2.imshow("thresh", thresh)
    cv2.imshow("threst2", thresh2)

    out1.write(frame)
    out2.write(thresh2)

    if cv2.waitKey(200) & 0xFF == ord('q'):
        break

out1.release()
out2.release()
video.release()
cv2.destroyAllWindows()