/**
 * @file background_substraction.cpp
 * @author Y.C. Long (axoford@icloud.com)
 * @brief
 * @version 0.1
 * @date 2022-06-02
 *
 * @copyright Copyright (c) 2022
 *
 * Dynamic objects detection using background subtraction
 * 用背景减方法对动态物体进行检测
 *
 */

#include "avi_fourcc.h"

#include <iostream>
#include <sstream>

#include <opencv2/highgui.hpp>
#include <opencv2/imgcodecs.hpp>
#include <opencv2/imgproc.hpp>
#include <opencv2/video.hpp>
#include <opencv2/videoio.hpp>

using namespace cv;
using namespace std;

int main(int argc, const char **argv) {
  Ptr<BackgroundSubtractor> pBackSubMOG2, pBackSubKNN;
  pBackSubMOG2 = createBackgroundSubtractorMOG2();
  pBackSubKNN = createBackgroundSubtractorKNN();
  string video_path("assets/dormitory1.mp4");
  VideoCapture capture(video_path);
  auto fourcc = get_fourcc();
  VideoWriter KNNWriter("result/background_substraction/KNN.avi", fourcc, 20,
                        Size(1080, 1920), false);
  VideoWriter MOG2Writer("result/background_substraction/MOG2.avi", fourcc, 20,
                         Size(1080, 1920), false);

  if (!capture.isOpened()) {
    cerr << "Unable to open file." << endl;
    return 0;
  }

  Mat frame, fgMaskMOG2, fgMaskKNN;
  while (true) {
    capture >> frame;
    if (frame.empty()) {
      break;
    }
    cv::flip(frame, frame, -1);
    pBackSubMOG2->apply(frame, fgMaskMOG2);
    pBackSubKNN->apply(frame, fgMaskKNN);
    KNNWriter << fgMaskKNN;
    MOG2Writer << fgMaskMOG2;
  }
  KNNWriter.release();
  MOG2Writer.release();
  return 0;
}