from moviepy.editor import VideoFileClip
from PathConstants import *
# 读取视频
clip = VideoFileClip(clip_video_path)

# 计算视频总时长和要分割的段数
total_duration = clip.duration
num_segments = int(total_duration / segment_duration) + 1

# 分割视频并保存每一段
for i in range(num_segments):
    start_time = i * segment_duration
    end_time = min((i + 1) * segment_duration, total_duration)
    segment = clip.subclip(start_time, end_time)
    segment_path = generate_output_filename(i + 1)
    segment.write_videofile(segment_path, codec='libx264')

    # 输出分割进度
    progress = (i + 1) / num_segments * 100
    print(f'分割进度：{progress:.2f}%')

# 释放资源
clip.reader.close()
