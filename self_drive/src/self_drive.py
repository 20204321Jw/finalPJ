#!/home/pi/.pyenv/versions/py37/bin/python3

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

class SelfDrive:
    def __init__(self, publisher):
        self.publisher = publisher

    def lds_callback(self, scan):
        print("scan[0]:", scan.ranges[0], scan.ranges[315])
        turtle_vel = Twist()
        if scan.ranges[315] < 0.2828:
            turtle_vel.angular.z = 0.5
        elif scan.ranges[0] > 0.2 or scan.ranges == 0:
            turtle_vel.linear.x = 0.15
        self.publisher.publish(turtle_vel)

def main():
    rospy.init_node('self_drive')
    publisher = rospy.Publisher('cmd_vel', Twist, queue_size=1)
    driver = SelfDrive(publisher)
    subscriber = rospy.Subscriber('scan', LaserScan,
                                  lambda scan: driver.lds_callback(scan))
    rospy.spin()

if __name__ == "__main__":
    main()
