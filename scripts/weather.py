#!/usr/bin/env python
## coding: UTF-8

import rospy
import cv2
import numpy as np
from PIL import ImageFont
from sensor_msgs.msg import Image
from geometry_msgs.msg import Twist
from cv_bridge import CvBridge, CvBridgeError


class PiyoPiyo(object):
    def __init__(self):
        self._image_sub = rospy.Subscriber('/usb_cam/image_raw', Image, self.callback)
        self._piyopiyo_pub = rospy.Publisher('piyopiyo_image', Image, queue_size=1)
        self._bridge = CvBridge()
        self._vel = Twist()

    def get_colored_area(self, cv_image, lower, upper):
        hsv_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2HSV)
        mask_image = cv2.inRange(hsv_image, lower, upper)
        extracted_image = cv2.bitwise_and(cv_image, cv_image, mask=mask_image)
        area = cv2.countNonZero(mask_image)
        return (area, extracted_image)

    def callback(self, data):
        cv_image = self._bridge.imgmsg_to_cv2(data, 'bgr8')        

        #lower_blue = np.array([0,120,120])
        #upper_blue = np.array([80,230,255])
        lower_blue = np.array([80,155,150])
        upper_blue = np.array([80,180,180])

        mask = cv2.inRange(cv_image, lower_blue, upper_blue)
        ret,thresh = cv2.threshold(mask, 40, 255, 0)
        im2,contours,hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        #print(contours)
        if len(contours) >= 70:
            cv2.putText(cv_image,"PIYOPIYO",(10,20) ,cv2.FONT_HERSHEY_PLAIN, 1.5,(80,230,255),1,cv2.LINE_AA)        

        #piyopiyo_area, piyopiyo_image = self.get_colored_area(cv_image, np.array([0,120,120]), np.array([80,230,255]))
        #piyopiyo_area, piyopiyo_image = self.get_colored_area(cv_image, np.array([0,155,155]), np.array([80,180,180]))
   


        #self._piyopiyo_pub.publish(self._bridge.cv2_to_imgmsg(piyopiyo_image, 'bgr8'))
        self._piyopiyo_pub.publish(self._bridge.cv2_to_imgmsg(cv_image, 'bgr8'))
        #rospy.loginfo('piyopiyo=%d' % (piyopiyo_area))   

if __name__ == '__main__':
    rospy.init_node('PiyoPiyo')
    color = PiyoPiyo()

    try:
        rospy.spin()
    except KeyboardInterrupt:
        pass
