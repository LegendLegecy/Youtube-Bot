from moviepy.video.io.VideoFileClip import VideoFileClip
import os

def split_video_into_chunks(video_path, output_dir, chunk_duration=59):
    try:
        # Load the video file
        video = VideoFileClip(video_path)
        video_duration = int(video.duration)
        video_name = os.path.basename(video_path).rsplit('.', 1)[0]

        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)
        
        # Split video into chunks
        for start_time in range(0, video_duration, chunk_duration):
            end_time = min(start_time + chunk_duration, video_duration)
            chunk = video.subclipped(start_time, end_time)
            chunk_filename = os.path.join(output_dir, f"{video_name}_part_{start_time // chunk_duration + 1}.mp4")
            
            print(f"Creating: {chunk_filename}")
            chunk.write_videofile(chunk_filename, codec="libx264", audio_codec="aac")
        
        print("Video splitting completed!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Input video file path
    # video_path = input("Enter the path to the video file: ").strip()
    
    # Output directory
    # output_dir = input("Enter the output directory for the chunks: ").strip()
    
    # Split the video
    split_video_into_chunks('Bean.mp4', 'Splitted Videos')
