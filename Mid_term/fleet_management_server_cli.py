#!/usr/bin/env python3

import rclpy
from rclpy.action import ActionServer, CancelResponse, GoalResponse
from your_package_name.msg import FleetManagement

class FleetManagementServer:
    def __init__(self):
        self.node = rclpy.create_node('fleet_management_server')
        self.action_server = ActionServer(
            self.node,
            FleetManagement,
            'fleet_management',
            self.execute_callback,
            cancel_callback=self.cancel_callback,
            goal_callback=self.goal_callback
        )

    def execute_callback(self, goal_handle):
        self.node.get_logger().info('Executing fleet management action...')

        # Placeholder logic for fleet management
        fleet_size = goal_handle.request.fleet_size
        routes = self.calculate_routes(fleet_size)

        # Publish feedback (e.g., completion_percentage)
        for i in range(1, 101):
            goal_handle.publish_feedback({'completion_percentage': i})
            self.node.get_logger().info(f'Feedback: {i}%')
            rclpy.spin_once(self.node, timeout_sec=0.01)

        # Set the action result (vehicle routes)
        goal_handle.succeed({'vehicle_routes': routes})

        return FleetManagement.Result()

    def calculate_routes(self, fleet_size):
        # Placeholder logic for route calculation
        return [f'Route for Vehicle {i}' for i in range(1, fleet_size + 1)]

    def cancel_callback(self, goal_handle):
        self.node.get_logger().info('Received request to cancel fleet management action.')
        return CancelResponse.ACCEPT

    def goal_callback(self, goal_request):
        self.node.get_logger().info('Received new fleet management goal request.')
        return GoalResponse.ACCEPT

def main():
    rclpy.init()
    server = FleetManagementServer()
    rclpy.spin(server.node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()

#Remember to replace 'your_package_name' with the actual name of  ROS2 package.

#In this example:

#execute_callback contains the placeholder logic for fleet management, where calculate_routes is a function that should be replaced with your actual fleet management logic.
#cancel_callback handles cancel requests.
#goal_callback handles new goal requests.
