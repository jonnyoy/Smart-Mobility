# ROS2 Fleet Management Application

## Overview

This ROS2 application allows users to allocate and route vehicles in a fleet. It uses an Action Server for fleet management and includes a professional Command Line Interface (CLI) for user interaction.

## Setup

### 1. Prerequisites

- ROS2 Foxy Fitzroy installed. Follow the [ROS2 installation guide](https://docs.ros.org/en/foxy/Installation.html) for instructions.

### 2. Clone the Repository

```bash
git clone https://github.com/<your_username>/<your_repository>.git
cd <your_repository>

Build the ROS2 Package
colcon build --packages-select <your_package_name>


Source the Workspace

source install/setup.bash

Running the Application
1. Launch the ROS2 Master

ros2 run ros2 run master_discovery_fkie master_discovery

Run the Professional CLI


./fleet_management_cli.py --fleet-size=<your_fleet_size>

Configuration
The configuration file config.ini allows customization of application settings. Modify this file as needed.

[General]
log_file = /path/to/fleet_management.log

Testing
The application has been tested under the following scenarios:

Allocating and routing a small fleet (e.g., fleet size 5).
Allocating and routing a large fleet (e.g., fleet size 20).
Canceling fleet management action mid-execution.
Troubleshooting
If you encounter issues, ensure that ROS2 is correctly installed and that all dependencies are satisfied.
Check the logs for more information. The log file location is specified in the configuration file.
Contributing
Contributions are welcome! If you find a bug or have suggestions for improvements, please open an issue or create a pull request.

License
This project is licensed under the MIT License - see the LICENSE.md file for details.


This README.md template provides clear instructions on setting up and running the ROS2 application, including building the package, launching the ROS2 master, and using the professional CLI. It also covers testing scenarios, troubleshooting tips, and information for contributors. Customize it according to your specific application and requirements.
