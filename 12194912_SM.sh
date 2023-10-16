# Create ROS2 workspace and package
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws
ros2 pkg create --build-type ament_python your_security_package

# Navigate to the package directory
cd ~/ros2_ws/src/your_security_package

# Create and edit user_interface_node.py
nano user_interface_node.py
# Paste the Python code, save, and exit Nano

# Create and edit motion_detector_node.py
nano motion_detector_node.py
# Paste the Python code, save, and exit Nano

# Build the workspace
cd ~/ros2_ws
colcon build

# Source the workspace
. install/setup.bash

# Run the nodes
ros2 run your_security_package user_interface_node
ros2 run your_security_package motion_detector_node

# In separate terminals, you can run the following commands for testing
ros2 service call /user_interface_node/arm_system std_srvs/srv/Trigger
ros2 topic echo /motion_data
ros2 service call /user_interface_node/disarm_system std_srvs/srv/Trigger
ros2 topic echo /motion_data

# Visualize the graph
ros2 run rqt_graph rqt_graph

