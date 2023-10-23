#!/usr/bin/env python3

import rclpy
from rclpy.action import ActionClient
from your_package_name.action import FleetManagement

class FleetManagementClient:
    def __init__(self):
        self.node = rclpy.create_node('fleet_management_client')
        self.action_client = ActionClient(self.node, FleetManagement, 'fleet_management')

    def send_goal(self, fleet_size):
        self.node.get_logger().info(f'Requesting fleet management for fleet size: {fleet_size}')

        # Create goal request
        goal_msg = FleetManagement.Goal()
        goal_msg.fleet_size = fleet_size

        # Send goal to server
        self.action_client.wait_for_server()
        future = self.action_client.send_goal_async(goal_msg, feedback_callback=self.feedback_callback)

        # Wait for the result
        rclpy.spin_until_future_complete(self.node, future)
        result = future.result()

        if result:
            self.node.get_logger().info('Fleet management request completed successfully!')
            self.display_routes(result.result.vehicle_routes)
        else:
            self.node.get_logger().warn('Fleet management request failed!')

    def feedback_callback(self, feedback_msg):
        self.node.get_logger().info(f'Received feedback: {feedback_msg.completion_percentage}%')

    def display_routes(self, routes):
        self.node.get_logger().info('Received routes:')
        for i, route in enumerate(routes, start=1):
            self.node.get_logger().info(f'  Vehicle {i}: {route}')

def main():
    rclpy.init()
    client = FleetManagementClient()

    # Example: Request fleet management for a fleet size of 5
    fleet_size = 5
    client.send_goal(fleet_size)

    rclpy.shutdown()

if __name__ == '__main__':
    main()
