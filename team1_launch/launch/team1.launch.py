# Import ROS2 launch modules
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.substitutions import FindPackageShare
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        # Include another launch file from a different package
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([
                FindPackageShare('interbotix_xsarm_control'),
                # Replace 'target_package_name' with the name of your target package
                '/launch/xsarm_control.launch.py'
                # Adjust the path to the launch file within the target package
            ])
        ),
        # You can add more launch actions here if needed

        # Start the Python file as a ROS2 node
        Node(
            package='interbotix_xsarm_control',  # Replace with your package name
            executable='test.py',  # Use the executable name defined in setup.py
            name='test_node',  # Optional: specify a node name
            output='screen',  # Optional: direct the output to the screen
            # Additional parameters can be added here
        ),
        # You can add more nodes or launch actions here if needed
    ])
