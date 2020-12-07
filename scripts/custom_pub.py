#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from custom_msg_pub_sub.msg import CustomMsg


class CustomPublisher(Node):

    def __init__(self):
        super().__init__('custom_publisher')
        self.publisher_ = self.create_publisher(CustomMsg, 'topic', 10)
        timer_period = 0.5
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = CustomMsg()
        msg.my_field = float(self.i)
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%d"' % msg.my_field)
        self.i += 1


def main(args=None):
    rclpy.init(args=args)

    custom_publisher = CustomPublisher()

    rclpy.spin(custom_publisher)

    custom_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()