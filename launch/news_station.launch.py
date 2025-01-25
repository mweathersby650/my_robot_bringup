from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():

    ld = LaunchDescription()

    robot_name_array = ["giskard", "bb8", "daneel", "lander", "c3po"]
    for robot_name in robot_name_array:
        robot_news_station1 = Node(
            package="my_cpp_pkg",
            executable="robot_news_station",
            name="robot_news_station_" + robot_name,
            parameters=[{"robot_name": robot_name}],
        )
        ld.add_action(robot_news_station1)

    smartphone = Node(package="my_cpp_pkg", executable="smartphone", name="smartphone")

    ld.add_action(smartphone)
    return ld
