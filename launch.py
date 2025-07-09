from launch import LaunchDescription  # ROS object that embeds a launch configuration
from launch_ros.actions import Node  # ROS object that represents a Node to start
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    return LaunchDescription(
        [
            Node(package="rxjoy_pkg", executable="rxjoy_node"),
            IncludeLaunchDescription(
                PythonLaunchDescriptionSource(
                    PathJoinSubstitution(
                        [
                            FindPackageShare(
                                "livox_ros_driver2"
                            ),  # Name of the package where the launch file exists
                            "launch_ROS2",  # Subdirectory containing the launch file
                            "msg_MID360_launch.py",  # Name of the launch file
                        ]
                    )
                )
            ),
        ]
    )
