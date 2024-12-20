import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32MultiArray

class SubscriberNode(Node):
    def __init__(self):
        super().__init__('subscriber_node')
        self.subscription = self.create_subscription(
            Int32MultiArray, 
            'comparison_values', 
            self.listener_callback, 
            10
        )
        self.get_logger().info('Subscriber Node is running...')

    def listener_callback(self, msg):
        a, b = msg.data  # Menerima nilai a dan b dari pesan
        if a == b:
            result = "nilai sama besar"
        elif a > b:
            result = "a lebih besar"
        else:
            result = "b lebih besar"

        self.get_logger().info(f'Received: a={a}, b={b}, Result: {result}')
        print(f"Comparison result: {result}")

def main(args=None):
    rclpy.init(args=args)
    node = SubscriberNode()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
    