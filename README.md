# 新概念成像与制导信息处理技术

本项目主要包含动态目标跟踪检测，基于OpenCV实现背景减、CamShift、MeanShift、光流法(Optical Flow)。


## 目录层次

```
.
├── assets -- 不在仓库中，在Release中下载
│   ├── dormitory1.mp4
│   └── slow_traffic_small.mp4
├── doc -- 报告文档
│   ├──
│   └── present
├── README.md
├── result -- 不在仓库中，结果视频文件，由程序读写
│   └── background_substraction
│       ├── KNN.avi
│       └── MOG2.avi
├── src -- 源代码
│   ├── background_substraction
│   │   └── main.cpp
│   ├── camshift
│   │   └── camshift.cpp
│   ├── include
│   ├── meanshift
│   │   └── main.cpp
│   └── optical_flow
│       └── main.cpp
└── xmake.lua -- 构建描述文件
```


## 构建本项目

在系统中安装OpenCV和xmake，在项目根目录下执行 `xmake`