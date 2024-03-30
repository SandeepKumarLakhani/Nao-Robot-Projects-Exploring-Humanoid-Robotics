from naoqi import ALProxy
import cv2
import numpy as np

# IP address and port of the NAO robot
nao_ip = "192.168.221.80"
nao_port = 9559

# Connect to the ALVideoDevice proxy
video_proxy = ALProxy("ALVideoDevice", nao_ip, nao_port)

# Set camera parameters
resolution = 2  # VGA resolution
color_space = 11  # RGB color space
fps = 30  # Frame rate
camera_id = 1 # Camera ID (0 for top camera, 1 for bottom camera)

# Subscribe to the camera
camera_name = "python_camera"
camera_id = video_proxy.subscribeCamera(camera_name, camera_id, resolution, color_space, fps)

try:
    while True:
        # Get image from the camera
        image = video_proxy.getImageRemote(camera_id)
        if image is None:
            continue

        # Parse image data
        width = image[0]
        height = image[1]
        image_data = np.frombuffer(image[6], dtype=np.uint8)
        image_data = image_data.reshape((height, width, 3))

        # Display the image using OpenCV
        cv2.imshow("NAO Camera", image_data)
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break

finally:
    # Unsubscribe from the camera
    video_proxy.unsubscribe(camera_name)
    cv2.destroyAllWindows()
