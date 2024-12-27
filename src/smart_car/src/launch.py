import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    package_name = 'smart_car'
    urdf_file = 'smartcar.urdf'
    
    # Full path to the URDF file
    urdf_path = os.path.join(
        get_package_share_directory(package_name),
        'urdf',
        urdf_file
    )

    return LaunchDescription([
        # Run RViz2
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen',
            arguments=['-d', urdf_path]
        ),

        # Publish robot_state
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            output='screen',
            parameters=[{'robot_description': open(urdf_path).read()}]
        ),
    ])
