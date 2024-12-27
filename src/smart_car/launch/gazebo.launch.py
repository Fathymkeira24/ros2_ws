from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    # Paths
    smartcar_pkg = FindPackageShare('smartcar')
    gazebo_ros_pkg = FindPackageShare('gazebo_ros')
    world_path = PathJoinSubstitution([smartcar_pkg, 'worlds', 'smartcar_world.world'])
    urdf_path = PathJoinSubstitution([smartcar_pkg, 'urdf', 'smartcar.urdf.xacro'])

    # Include Gazebo launch file
    gazebo_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            PathJoinSubstitution([gazebo_ros_pkg, 'launch', 'gazebo.launch.py'])
        ),
        launch_arguments={'world': world_path}.items()
    )

    # Spawn robot
    spawn_robot = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=['-entity', 'smartcar', '-file', urdf_path],
        output='screen'
    )

    return LaunchDescription([
        gazebo_launch,
        spawn_robot
    ])
