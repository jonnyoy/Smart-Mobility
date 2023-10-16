# Smart-Mobility
Smart Mobility lab 

This ROS2 package implements a simple Smart Home Security System with user interface and motion detection nodes.

## Installation

1. Create a ROS2 workspace:

    ```bash
    mkdir -p ~/ros2_ws/src
    cd ~/ros2_ws
    ```

2. Create the package:

    ```bash
    ros2 pkg create --build-type ament_python your_security_package
    ```

3. Navigate to the package directory:

    ```bash
    cd ~/ros2_ws/src/your_security_package
    ```

4. Create and edit Python scripts for nodes (`user_interface_node.py` and `motion_detector_node.py`). Paste the respective code into each file.

5. Build the workspace:

    ```bash
    cd ~/ros2_ws
    colcon build
    ```

6. Source the workspace:

    ```bash
    . install/setup.bash
    ```

## Usage

1. Run the user interface node:

    ```bash
    ros2 run your_security_package user_interface_node
    ```

2. Run the motion detector node:

    ```bash
    ros2 run your_security_package motion_detector_node
    ```

3. Test the system:

    - Arm the system:

        ```bash
        ros2 service call /user_interface_node/arm_system std_srvs/srv/Trigger
        ```

    - View motion data:

        ```bash
        ros2 topic echo /motion_data
        ```

    - Disarm the system:

        ```bash
        ros2 service call /user_interface_node/disarm_system std_srvs/srv/Trigger
        ```

    - View motion data again:

        ```bash
        ros2 topic echo /motion_data
        ```

4. Visualize the system graph:

    ```bash
    ros2 run rqt_graph rqt_graph
    ```

## Additional Notes

- Customize the system behavior by modifying the Python scripts (`user_interface
