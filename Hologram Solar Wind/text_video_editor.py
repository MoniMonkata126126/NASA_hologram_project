from moviepy.editor import *
from api_request import read_api
from datetime import date

def creating_text_video():
    # Load the black background video
    background_video = VideoFileClip('Untitled.mp4').subclip(0, 40)
    
    # Get the latest info for solar flare
    latest_event = read_api()
    
    # Create the lines for the variables
    video_lines = []
    
    # Make the text lines for the text clips
    with open('api_info.txt', 'r') as file:
        for index, line in enumerate(file):
            if index == 0:
                if date.today() == latest_event[1][0:10]:
                    video_lines.append(line.replace('\n', ' ') + 'today at ' + latest_event[index][11:16] + '.')
                else:
                    video_lines.append(line.replace('\n', ' ') + 'yesterday at ' + latest_event[index][11:16] + '.')
            
            if index > 0 and index < 3:
                video_lines.append(line.replace('\n', ' ') + latest_event[index][11:16])
            
            if index == 3:
                    video_lines.append(line + latest_event[index])
                
    # Make a list of the text clips
    t = 4
    txt_clips = []
    
    for line in video_lines:
        txt_clip = TextClip(line, fontsize = 100, color = 'GhostWhite', stroke_width = 3, stroke_color = 'white')
        txt_clip = txt_clip.set_start(t)
        txt_clip = txt_clip.set_position('center')
        txt_clip = txt_clip.set_duration(8)
        txt_clips.append(txt_clip)
        t = t + 9
        
    #print(txt_clips)
        
    # Combine everything into the video
    final_video = CompositeVideoClip([background_video, txt_clips[0], txt_clips[1], txt_clips[2], txt_clips[3]])
    
    # Write the video
    final_video.write_videofile('text_video.mp4')
    