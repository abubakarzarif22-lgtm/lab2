import rclpy
from rclpy.node import Node

from std_msgs.msg import String, Int8


class NumericListener(Node):

    def __init__(self):
        super().__init__('numeric_listener')

        # Keep original String subscriber
        self.string_subscription = self.create_subscription(
            String,
            'chatter',
            self.string_callback,
            10
        )

        # New Int8 subscriber
        self.numeric_subscription = self.create_subscription(
            Int8,
            'numeric_chatter',
            self.numeric_callback,
            10
        )

        # prevent unused variable warning
        self.string_subscription
        self.numeric_subscription

    def string_callback(self, msg):
        self.get_logger().info(f'I heard: {msg.data!r}')

    def numeric_callback(self, msg):
        self.get_logger().info(f'I heard numeric: {msg.data}')


def main(args=None):
    rclpy.init(args=args)

    listener = NumericListener()
    rclpy.spin(listener)


if __name__ == '__main__':
    main()
