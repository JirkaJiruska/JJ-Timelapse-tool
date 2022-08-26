import cv2, os, sys
import numpy as np

# define paths
home_dir = os.path.abspath(os.path.dirname(sys.argv[0])) + '\\'
img_stock_dir = home_dir + "stock\\"
video_out_path = home_dir + "video.avi"

print(video_out_path)

img_names_list = [img_stock_dir + f for f in os.listdir(img_stock_dir)]

fourcc = cv2.VideoWriter_fourcc(*'MJPG')
videowriter = cv2.VideoWriter(home_dir + 'video.avi',fourcc,5,(2592,1728))

frames_number = len(img_names_list)
counter = 1
for img_name in img_names_list:
    
    img = cv2.imread(img_name)
    videowriter.write(img)
    print("Progress: {a:2.1f}%".format(a=(counter / frames_number * 100)))
    counter += 1
videowriter.release()






