# AUTONOMOUSCARS_USING_AI
AUTONOMOUS CAR NAVIGATION USING AI AND ML
[reddy.vuppunuthula@gmal.com]


Preparatory Work AIML
• Install Ubuntu 16.04
• Install ROS and Gazebo
• Develop a traffic sign recognizer
• Develop an obstacle sensor
• Integrate the above and run through
and obstacle course

Simulation Environment: ROS - Robotic control , Gazebo - vizualisation

Level 0 – Manual Control
1. Load the map and turtle-bot onto Gazebo
2. Tele-operate/control it using your
keyboard
3. Play around with the Robot in Gazebo !!

Level 1 – Visual Navigation
Tasks -
1. Given the color Image of the first person
view of the robot
2. The Robot needs to recognize sign boards
and takes actions
How –
1. Build a Image Recognition Module.
2. Integrate the module based on the
instructions given for Level 

Data set collection –
1. Data is collected by tele-operating the robot in the map
and taking Images.
2. Dataset will be given to you.
Movement of the bot –
1. The robot will move till it reaches a fixed distance from
the sign and stops(This behavior will be given)
2. The robot will look at the signs and wait for the image
recognition
Image Recognition Module –
1. Use the dataset and train a simple CNN to understand the
traffic sign.
2. Given a first person view of the robot, the model should
predict the sign the Robot is Looking at


Level 2 – Avoid Obstacles
Tasks -
1. Given Color and Depth Image
2. Control the robot and avoid the obstacles
How –
1. Build a Control Module based on the depth
images.
2. Integrate the module based on the
instructions given for Level 2

Level 3:
Tasks –
1. Given the color and depth images
2. The Robot recognizes waits till the signal is
red and moves when it turns green.
How –
1. Use image recognition module and the
control module


