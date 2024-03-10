# t1_arm
# AERO62520 Group Design Project

## Overview
This project focuses on designing control files for the Interbotix PincherX 150 Manipulator. It aims to provide a comprehensive control scheme that enhances the functionality and usability of the PincherX 150 robotic arm for various applications. This repository contains custom control files and is designed to be used alongside the Interbotix ROS packages.

## Dependencies
This project relies on the following Interbotix ROS packages:
- `interbotix_xs_sdk`
- `interbotix_xs_modules`
- `interbotix_xsarm_descriptions`

Please ensure these are installed and properly configured in your ROS environment before proceeding.

## Installation and Usage
To set up your environment for this project, follow the steps below:

1. Clone this repository into your catkin workspace or a similar ROS workspace.
2. Navigate to your workspace directory and use `colcon build` to build the working environment.
3. Source the `setup.bash` script to ensure your environment is correctly configured.


## Features
This repository includes custom control files designed specifically for the PincherX 150 Manipulator. These files are meant to enhance the default functionalities provided by the Interbotix demos included in the `interbotix_xsarm_control` package.

## Target Audience
This project is intended for students and academics who are working on robotics projects, specifically those involving the Interbotix PincherX 150 Manipulator. It provides a solid base for developing more advanced control schemes and applications.

## License
Copyright 2022 Trossen Robotics

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

- Redistributions of source code must retain the above copyright notice, this list of conditions, and the following disclaimer.
- Redistributions in binary form must reproduce the above copyright notice, this list of conditions, and the following disclaimer in the documentation and/or other materials provided with the distribution.
- Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

## Contributing
We welcome contributions from the community. If you wish to contribute to this project, please fork the repository and submit a pull request with your proposed changes.

For any questions or issues, please open an issue on this repository, and we will aim to address it as soon as possible.

---

For detailed documentation on the Interbotix PincherX 150 Manipulator and the associated ROS packages, please refer to the [official Interbotix documentation](https://www.trossenrobotics.com/).
