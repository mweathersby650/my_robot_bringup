# 3 nodes
# tutrle sim window
# control tutrle
# spawn tutrn
#
#
# main turtle will try to catch every new turtle
#
# after being caught , the non main turtle will disappear


from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():

    ld = LaunchDescription()

    turtle_sim_window = Node(
        package="turtlesim",
        executable="turtlesim_node",
        name="turtle_sim_window",
    )
    ld.add_action(turtle_sim_window)

    turtle_sim_spawner = Node(
        package="my_cpp_pkg",
        executable="turtle_sim_spawner",
        name="turtle_sim_spawner",
        parameters=[{"max_turtles_to_spawn": 0}, {"frequency_to_spawn":3.0}],
    )
    ld.add_action(turtle_sim_spawner)

    turtle_sim_controller = Node(
        package="my_cpp_pkg",
        executable="turtle_sim_controller",
        name="turtle_sim_controller",
        parameters=[{"linear_velocity": 2.0}, {"angular_velocity": 10.7}],
    )
    ld.add_action(turtle_sim_controller)

    return ld
