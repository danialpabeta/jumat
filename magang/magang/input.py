import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32MultiArray

class PublisherNode(Node):
    def __init__(self):
        super().__init__('publisher_node')
        self.publisher_ = self.create_publisher(Int32MultiArray, 'comparison_values', 10)
        self.timer = self.create_timer(2.0, self.publish_input)
        self.get_logger().info('Publisher Node is running...')

    def publish_input(self):
        try:
            a = int(input("Enter value for a: "))
            b = int(input("Enter value for b: "))
            msg = Int32MultiArray()
            msg.data = [a, b]  # Mengirim nilai a dan b sebagai array
            self.publisher_.publish(msg)
            self.get_logger().info(f'Published values: a={a}, b={b}')
        except ValueError:
            self.get_logger().warn('Invalid input! Please enter integers.')

def main(args=None):
    rclpy.init(args=args)
    node = PublisherNode()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
