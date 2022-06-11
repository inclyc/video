import cv2

filename = "C:/Users/admin/Desktop/帧差分/源视频/鸟.mp4"
video = cv2.VideoCapture(filename)


out_fps = 30.0
fourcc = cv2.VideoWriter_fourcc('M', 'P', '4', '2')
out1 = cv2.VideoWriter('C:/Users/admin/Desktop/帧差分/目标视频/v1.avi', fourcc, out_fps, (500, 400))
out2 = cv2.VideoWriter('C:/Users/admin/Desktop/帧差分/目标视频/v2.avi', fourcc, out_fps, (500, 400))

lastFrame = None

while video.isOpened():
    (ret, frame) = video.read()
    if not ret:
        break
    frame = cv2.resize(frame, (500, 400), interpolation=cv2.INTER_CUBIC)
    if lastFrame is None:
        lastFrame = frame
        continue
    frameDelta = cv2.absdiff(lastFrame, frame)
    lastFrame = frame.copy()
    thresh = cv2.cvtColor(frameDelta, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(thresh, 25, 255, cv2.THRESH_BINARY)[1]


    cnts, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for c in cnts:
        if cv2.contourArea(c) < 200:
            continue

        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow("frame", frame)
    cv2.imshow("frameDelta", frameDelta)
    cv2.imshow("thresh", thresh)

    out1.write(frame)
    out2.write(frameDelta)

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

out1.release()
out2.release()
video.release()
cv2.destroyAllWindows()
