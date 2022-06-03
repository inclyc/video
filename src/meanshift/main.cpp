#include "avi_fourcc.h"
#include <iostream>
#include <opencv2/highgui.hpp>
#include <opencv2/imgcodecs.hpp>
#include <opencv2/imgproc.hpp>
#include <opencv2/video.hpp>
#include <opencv2/videoio.hpp>
using namespace cv;
using namespace std;
int main(int argc, char **argv) {
  string filename = "assets/slow_traffic_small.mp4";
  VideoCapture capture(filename);
  VideoWriter writer("result/meanshift/meanshift.avi", get_fourcc(), 20,
                     Size(640, 360));
  if (!capture.isOpened()) {
    // error in opening the video input
    cerr << "Unable to open file!" << endl;
    return 0;
  }
  Mat frame, roi, hsv_roi, mask;
  capture >> frame; // 360 x 640
  Rect track_window(300, 200, 100, 50);
  roi = frame(track_window);
  cvtColor(roi, hsv_roi, COLOR_BGR2HSV);
  inRange(hsv_roi, Scalar(0, 60, 32), Scalar(180, 255, 255), mask);
  float range_[] = {0, 180};
  const float *range[] = {range_};
  Mat roi_hist;
  int histSize[] = {180};
  int channels[] = {0};
  calcHist(&hsv_roi, 1, channels, mask, roi_hist, 1, histSize, range);
  normalize(roi_hist, roi_hist, 0, 255, NORM_MINMAX);
  TermCriteria term_crit(TermCriteria::EPS | TermCriteria::COUNT, 10, 1);
  while (true) {
    Mat hsv, dst;
    capture >> frame;
    if (frame.empty())
      break;
    cvtColor(frame, hsv, COLOR_BGR2HSV);
    calcBackProject(&hsv, 1, channels, roi_hist, dst, range);
    meanShift(dst, track_window, term_crit);
    rectangle(frame, track_window, 255, 2);
    writer << frame;
  }
}