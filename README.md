# real_chick
おもちゃのひよこを判別しPIYOPIYOと表記させます。  
# 動作環境
  - Ubuntu 18.04.5 LTS
  - ROS Melodic
  - OpenCV 3.2.0
  - webカメラ
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
- もう一つ端末を開く
```bash
$ cd ~/piyopiyo/scripts
$ rosrun piyopiyo
```
# ライセンス
BSD 3-Clause License
