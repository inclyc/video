#ifndef AVI_FOURCC_H
#define AVI_FOURCC_H
#include <opencv2/videoio.hpp>

inline int get_fourcc() { return cv::VideoWriter::fourcc('X', 'V', 'I', 'D'); }

#endif // AVI_FOURCC_H