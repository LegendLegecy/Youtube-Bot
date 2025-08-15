import os
import subprocess

def split_video(video_path, output_dir, chunk_duration=59):
    # try:
    os.makedirs(output_dir, exist_ok=True)
    video_name = os.path.splitext(os.path.basename(video_path))[0]

    # Get video duration using ffprobe
    result = subprocess.run(
        ['ffprobe', '-v', 'error', '-show_entries', 'format=duration',
            '-of', 'default=noprint_wrappers=1:nokey=1', video_path],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    total_duration = int(float(result.stdout))

    for start in range(0, total_duration, chunk_duration):
        part_num = start // chunk_duration + 1
        output_file = os.path.join(output_dir, f"{video_name}_part_{part_num}.mp4")
        print(f"Creating: {output_file}")

        subprocess.run([
            'ffmpeg',
            '-ss', str(start),
            '-i', video_path,
            '-t', str(min(chunk_duration, total_duration - start)),
            '-c', 'copy',
            output_file
        ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    print("Video splitting completed!")

    # except Exception as e:
    #     print(f"An error occurred: {e}")


video_path= 'bean.mp4'
output_dir= 'Splitted Videos'

split_video(video_path , output_dir)