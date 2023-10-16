# user_interface_node.py
import rclpy
from rclpy.node import Node

class UserInterfaceNode(Node):
    def __init__(self):
        super().__init__('user_interface_node')
        # Your node implementation here

def main(args=None):
    rclpy.init(args=args)
    node = UserInterfaceNode()
    try:
        rclpy.spin(node)
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()

