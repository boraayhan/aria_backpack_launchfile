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
                    PathJoinSubstitution([
                        FindPackageShare("another_pkg"),  # Name of the package where the launch file exists
                        "launch",                         # Subdirectory containing the launch file
                        "another_launch_file.py"          # Name of the launch file
                    ])
                )
            )
            """
            EXAMPLE:
            
            Node(
                package="package_name",
                executable="node_name",
                remappings=[
                    ("/topic/remap1", "othertopic/remap1"),
                    ("/topic/remap2", "othertopic/remap2"),
                    ("/topic/remap3", "othertopic/remap3"),

                ]
            )
            """,
        ]
    )
