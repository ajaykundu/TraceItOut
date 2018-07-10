
import argparse
import datetime
import imutils
import time
import cv2
import os


start_time = time.time()
start_time 
elapsed_time = time.time() - start_time
elapsed_time

ap = argparse.ArgumentParser()
print(ap)
ap.add_argument("-v", "--video", help="path to the video file")
ap.add_argument("-a", "--min-area", type=int, default=500, help="minimum area size")
args = vars(ap.parse_args())


print(args["video"])
# if the video argument is None, then we are reading from webcam
if args.get("video",None) is None:
    camera = cv2.VideoCapture(0)
    print('hello')
    

# otherwise, we are reading from a video file
else:
    camera = cv2.VideoCapture(args["video"])
         
# initialize the first frame in the video stream
firstFrame = None
# get the loaction and create video folder if not created.


hell=[]
print(hell)
if args["video"]:
    hell = args["video"].split("/")
else:
    hell.append('hello')
    hell.append('output.avi')


location = os.getcwd()
directory = 'video'
if not os.path.exists(directory):   
	os.makedirs(directory)

directory = "/" + directory + "/" + hell[1]
print(directory)
location = location + directory
print(location)

# for setting of every video.
width = camera.get(3)  # float
height = camera.get(4)
width = round(width)
height = round(height)
print("wirth of frame : "+str(width))
print("height of frame : "+str(height))


# count frames
length = int(camera.get(cv2.CAP_PROP_FRAME_COUNT))
print("length of video : " +str(length) )

fps    = camera.get(cv2.CAP_PROP_FPS)
print("length of video : "+ str(fps))


if fps==0:
    fps = 30

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(location,fourcc, fps , (width,height))

numframe = 0

# loop over the frames of the video
while True:
  
    (grabbed, frame) = camera.read()
    numframe = numframe + 1
    thisFrame = frame
    #out.write(thisFrame)
    text = "Unoccupied"
    
    
    if not grabbed:
        break
    
    # resize the frame, convert it to grayscale, and blur it
    frame = imutils.resize(frame, width=500)
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21,21), 0)
    
    
    # if the first frame is None, initialize it
    if firstFrame is None:
        firstFrame = gray
        #out.write(thisFrame)
        continue
    
    elapsed_time = time.time() - start_time
    print(elapsed_time)
    if elapsed_time > 2:
        start_time = time.time()
        firstFrame = gray
    
    
    frameDelta = cv2.absdiff(firstFrame,gray)
    thresh = cv2.threshold(frameDelta, 25, 255,cv2.THRESH_BINARY)[1]
    
    
    thresh = cv2.dilate(thresh,None,iterations = 2)
    _ , cnts, _ = cv2.findContours(thresh.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    
    #just write the frame one time.
    fwr = 1
    
    for c in cnts:
        #  if the contour is too small, ignore it
        if cv2.contourArea(c) < args["min_area"]:
            continue
        
        
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(frame,(x,y),(x + w,y + h), (0, 255, 0),2)
        text = "Occupied"
        #print("hello")
        if fwr==1:
            out.write(thisFrame)
            fwr=0
        
        
    
    
    cv2.putText(frame, "Room Statis: {}".format(text), (10,20),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    cv2.putText(frame, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"),(10,frame.shape[0] - 10),cv2.FONT_HERSHEY_SIMPLEX,0.35,(0,0, 255),1)
    
    # show the frame and record if the user presses a key
    cv2.imshow("Thresh", thresh)
    cv2.imshow("Frame Delta", frameDelta)
    cv2.imshow("Security Feed",frame)
    key = cv2.waitKey(1) & 0xFF
    
    # if the `q` key is pressed, break from the lop
    if key== ord("q"):
        break
    

# cleanup the camera and close any open windows
print(numframe)
camera.release()
out.release()
cv2.destroyAllWindows()
#hellow world