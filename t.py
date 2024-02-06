from moviepy.editor import VideoFileClip

# 读取视频
video_path = 'input_video.mp4'
clip = VideoFileClip(video_path)

# 移除视频中的字幕（去除文本轨道）
clip = clip.set_audio(None)

# 保存去除字幕后的视频
output_path = 'output_video_without_subtitles.mp4'
clip.write_videofile(output_path, codec='libx264')

# 释放资源
clip.reader.close()
