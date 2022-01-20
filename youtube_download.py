# importing the module
from pytube import YouTube

# where to  save
SAVE_PATH = "/home/ahmad/Downloads/"

# link of the video to be downloaded
link = "https://www.youtube.com/watch?v=plnjSuU-vyg"

try:
  # object creation using Youtube
  # which was imported in the beginning
  yt = YouTube(link)
except:
  print("Connection error")

# filters out all the files with "mp4" extension
mp4files = yt.streams.filter(progressive=True, file_extension="mp4")

# to set the name of the file
#yt.set_filename("Test drive")

# get the video with the extension and
# resolution passed in the get() function
d_video = yt.streams.get_by_itag(22)
try:
  # downloading the video
  d_video.download(SAVE_PATH)
except:
  print("Some error!")
print("Task Completed!")
