# ROS2: custom-msg-pub-sub

Target: noetic
## Build
```
colcon build
```

## Usage
Both terminals must be sourced!

1. Terminal
```
ros2 run custom_msg_pub_sub custom_pub.py
```

2. Terminal
```
ros2 topic echo /topic
```

## Sources
https://index.ros.org/doc/ros2/Tutorials/Writing-A-Simple-Py-Publisher-And-Subscriber/
https://index.ros.org/doc/ros2/Tutorials/Custom-ROS2-Interfaces/
https://answers.ros.org/question/314724/ros2-embedding-a-msg-as-a-field-in-a-custom-msg/