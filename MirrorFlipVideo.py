from moviepy.editor import VideoFileClip, clips_array, vfx
from PathConstants import *
import os

# 确保输出文件夹存在
if not os.path.exists(mirror_output_folder):
    os.makedirs(mirror_output_folder)

video_files = [f for f in os.listdir(mirror_input_folder) if f.endswith('.mp4')]

for idx, video_file in enumerate(video_files, start=1):
    input_file_path = os.path.join(mirror_input_folder, video_file)
    output_file_path = os.path.join(mirror_output_folder, video_file.replace('.mp4', '_MIRROR.mp4'))

    # 打开视频文件
    video_clip = VideoFileClip(input_file_path)

    # 进行左右镜像翻转
    mirrored_clip = video_clip.fx(vfx.mirror_x)

    # 保存翻转后的视频
    mirrored_clip.write_videofile(output_file_path)
    print(f'进度：{idx}/{len(video_files)}')

print('所有视频镜像翻转完成！')







# # 读取视频
# clip = VideoFileClip(mirror_flip_video_path)
#
# # 反转视频并保存
# flipped_clip = clip.fx(vfx.mirror_x)
#
#
# # 保存反转后的视频（包括音频）
# flipped_clip.write_videofile(output_path, codec='libx264', audio_codec='aac')
#
# # 释放资源
# clip.reader.close()
# flipped_clip.reader.close()