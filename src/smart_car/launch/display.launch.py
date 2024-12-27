import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    package_name = 'smart_car'  # Replace with your package name
    urdf_file = 'smartcar.urdf'  # Make sure this is the correct URDF file

    # Full path to the URDF file
    urdf_path = os.path.join(
        get_package_share_directory(package_name),
        'urdf',
        urdf_file
    )

    return LaunchDescription([
        # Publish the robot state (URDF description)
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            output='screen',
            parameters=[{'robot_description': open(urdf_path).read()}]
        ),

        # Launch Rviz2 for visualization
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen'
        ),
    ])


