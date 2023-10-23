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

