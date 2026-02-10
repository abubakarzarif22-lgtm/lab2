import rclpy
from rclpy.node import Node

from std_msgs.msg import String, Int8


class NumericTalker(Node):

    def __init__(self):
        super().__init__('numeric_talker')

        # Keep original String publisher
        self.string_publisher = self.create_publisher(String, 'chatter', 10)

        # New Int8 publisher
        self.numeric_publisher = self.create_publisher(Int8, 'numeric_chatter', 10)

        timer_in_seconds = 0.5
        self.timer = self.create_timer(timer_in_seconds, self.talker_callback)

        self.counter = 0

    def talker_callback(self):
        # Publish String message (same idea as original)
        msg = String()
        msg.data = f'Hello World, {self.counter}'
        self.string_publisher.publish(msg)
        self.get_logger().info(f'Publishing: {msg.data}')

        # Publish Int8 message on /numeric_chatter
        num_msg = Int8()
        num_msg.data = self.counter
        self.numeric_publisher.publish(num_msg)
        self.get_logger().info(f'Publishing numeric: {num_msg.data}')

        # Increment and wrap at 127
        self.counter += 1
        if self.counter > 127:
            self.counter = 0


def main(args=None):
    rclpy.init(args=args)

    talker = NumericTalker()
    rclpy.spin(talker)


if __name__ == '__main__':
    main()
