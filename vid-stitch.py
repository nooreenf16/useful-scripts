from moviepy.editor import *

# loading video dsa gfg intro video
video = VideoFileClip(r"C:\Users\noore\Downloads\zendaya-vid.mp4")

#a = 5.7
#b = 11
a = 3.1
b = 6.2

# getting subclip as video is large
clip = VideoFileClip(r"C:\Users\noore\Downloads\zen-vid2.mp4").volumex(2.4)

clip1 = video.subclip(t_start=0, t_end=a)
clip2 = video.subclip(t_start=b, t_end=None)

result = concatenate_videoclips([clip1, clip, clip2])
#result = concatenate_videoclips([clip, clip2])

# showing clip
result.ipython_display(width=480)
