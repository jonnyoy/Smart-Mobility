# motion_detector_node.py
import rclpy
from rclpy.node import Node

class MotionDetectorNode(Node):
    def __init__(self):
        super().__init__('motion_detector_node')
        # Your node implementation here

def main(args=None):
    rclpy.init(args=args)
    node = MotionDetectorNode()
    try:
        rclpy.spin(node)
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()

