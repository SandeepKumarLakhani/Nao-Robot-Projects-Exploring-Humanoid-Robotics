
from naoqi import ALProxy

def main():
    # IP address and port of the Nao robot
    robot_ip = "192.168.221.192"
    port = 9559

    # Create proxy for ALTextToSpeech module
    tts = ALProxy("ALTextToSpeech", robot_ip, port)

    # Say "Hello"
    tts.say("Hello Sandeep Lakhani ")

if __name__ == "__main__":
    main()

