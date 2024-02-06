mirror_flip_video_path = 'flip_input_video.mp4'
clip_video_path = 'input_video.mp4'

output_path = 'output_video_flipped.mp4'
segment_duration = 120  # 两分钟

mirror_input_folder = 'mirror_input_folder_path'
mirror_output_folder = 'mirror_output_folder_path'

def generate_output_filename(index):
    return f'output_segment_{index}.mp4'