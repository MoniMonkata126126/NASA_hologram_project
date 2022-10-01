from moviepy.editor import *
from text_video_editor import creating_text_video

def make_pyramid_video():
    # Load the black background video
    background_video = VideoFileClip('Untitled.mp4').subclip(10, 47)
    
    # Call the function to create relevant solar flare video
    creating_text_video()
    
    # Load main animation
    original_clip = VideoFileClip('text_video.mp4')

    # Make a vertical top copy with right size
    vertical_top_clip = original_clip.rotate(180).set_position('top').resize(0.3).margin(top = 90)

    # Make a horizontal left copy with right size
    horizontal_left_clip = original_clip.rotate(270).set_position('left').resize(0.3).margin(left = 380)

    # Make a vertical bottom copy with right size
    vertical_bottom_clip = original_clip.set_position('bottom').resize(0.3).margin(bottom = 90)

    # Make a horizontal right copy with right size
    horizontal_right_clip = original_clip.rotate(90).set_position('right').resize(0.3).margin(right = 380)

    # Conbine the copies with the background
    final_video = CompositeVideoClip([background_video, vertical_top_clip, horizontal_right_clip, vertical_bottom_clip, horizontal_left_clip])

    # Write the result to a file
    final_video.write_videofile("Latest Solar Flare.mp4")
    
make_pyramid_video()
