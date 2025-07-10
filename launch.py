from launch import LaunchDescription  # ROS object that embeds a launch configuration
from launch_ros.actions import Node  # ROS object that represents a Node to start
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    return LaunchDescription(
        [
            # Node(package="pkg", executable="node"),
            IncludeLaunchDescription(
                PythonLaunchDescriptionSource(
                    PathJoinSubstitution(
                        [
                            FindPackageShare(
                                "ublox_gps"
                            ),  # Name of the package where the launch file exists
                            "ublox_gps_node_zedf9p",  # Subdirectory containing the launch file
                            "launch.py",  # Name of the launch file
                        ]
                    )
                )
            ),
        ]
    )
