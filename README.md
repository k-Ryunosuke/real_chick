# real_chick
おもちゃのひよこを判別しPIYOPIYOと表記させます。  
# 動作環境
  - Ubuntu 18.04.5 LTS
  - ROS Melodic
  - OpenCV 3.2.0
  - webカメラ
    - [使用したカメラ](https://www.amazon.co.jp/-/en/Microphone-Connection-Recording-Meetings-Computer/dp/B08GY7S8F4)
# インストール方法
```bash
$ cd ~/catkin_ws/src
$ git clone https://github.com/k-Ryunosuke/real_chick.git
```
# 実行方法
```bash
$ cd real_chick
```
- roscoreを立ち上げる
```bash
$ roscore
```
- 新しく端末を開く
```bash
$ rosrun usb_cam usb_cam_node
```
- もう一つ端末を開く
```bash
$ rosrun real_chick piyo.py
```
- もう一つ端末を開く
```bash
$ rosrun image_view image_view image:=/piyopiyo_image
```
# 実行動画
[![LED](https://img.youtube.com/vi/s91JeVQiqtY/maxresdefault.jpg)](https://youtu.be/s91JeVQiqtY)
# ライセンス
[BSD 3-Clause License](https://github.com/k-Ryunosuke/real_chick/blob/master/LICENSE)
