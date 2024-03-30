from naoqi import ALProxy
import time
import math
def main():
	robot_ip = "192.168.221.192"
	port = 9559
	
	# Create proxy for ALTextToSpeech module
        tts = ALProxy("ALTextToSpeech", robot_ip, port)

    # Say "Hello"
        tts.say("i am moving in x for 20 second and then i turn 0.9 angle")
    # Create proxy for ALMotion module
	motion_proxy = ALProxy("ALMotion",robot_ip, port)
    # Set stiffness on for all joints
	motion_proxy.stiffnessInterpolation("Body", 1.0, 1.0)
    # Set walking parameters
	x_speed = 0.5 # Forward velocity (m/s)
	y_speed = 0.0 # Sideways velocity (m/s)
	theta_speed = 0.0 # Angular velocity (rad/s)
	frequency=3.0
    # Make the robot walk
	motion_proxy.moveToward(x_speed, y_speed, theta_speed,[["Frequency",frequency]])
    # Sleep to allow the robot to walk for a while
	time.sleep(20)  # Adjust as needed
	
    # Stop the robot
	motion_proxy.stopMove()
    # Release stiffness on all joints
	#motion_proxy.stiffnessInterpolation("Body", 0.0, 1.0)
	motion_proxy.moveToward(0.0,0.0,0.8)
	time.sleep(10);
	motion_proxy.stopMove()
if __name__ == "__main__":
    main()
