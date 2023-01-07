# Import everything needed to edit video clips
from moviepy.editor import *


# loading video dsa gfg intro video
clip = VideoFileClip("C:\\Users\\stefa\\Downloads\\Bigbang.mp4")


# getting only first 5 seconds
clip = clip.subclip(0, 5)

# displaying video with auto play
clip.ipython_display(autoplay = 1)
