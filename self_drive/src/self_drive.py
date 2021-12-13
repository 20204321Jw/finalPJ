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
        if scan.ranges[0] < 0.25 and scan.ranges[0] != 0:
            turtle_vel.linear.x = 0
            turtle_vel.angular.z = 2.5
        else:
            turtle_vel.linear.x = 0.15
        if scan.ranges[45] < 0.2828 and scan.ranges[45] != 0:
            turtle_vel.linear.x = 0
            turtle_vel.angular.z = 2.5
        if scan.ranges[0] > 0.25 and scan.ranges[0] != 0 and scan.ranges[45] > 0.14:
            turtle_vel.linear.x = 0.15
            turtle_vel.angular.z = 0
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
