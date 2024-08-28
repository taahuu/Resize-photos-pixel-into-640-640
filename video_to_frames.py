import cv2
import os

def extract_frames(video_path, fps):
    """Extracts frames from a video at a specified frame rate.

    Args:
        video_path: The path to the video file.
        fps: The desired frame rate.
    """

    # Create a directory to store the extracted frames
    output_dir = os.path.splitext(video_path)[0] + "_frames"
    os.makedirs(output_dir, exist_ok=True)

    # Open the video file
    cap = cv2.VideoCapture(video_path)

    # Get the video's frame rate
    video_fps = cap.get(cv2.CAP_PROP_FPS)

    # Calculate the number of frames to skip between each extracted frame
    skip_frames = int(video_fps / fps)

    frame_count = 0
    video_name = os.path.splitext(os.path.basename(video_path))[0]

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Skip frames as needed
        if frame_count % skip_frames == 0:
            # output_path = os.path.join(output_dir, f"frame_{frame_count}.jpg")
            output_path = os.path.join(output_dir, f"{video_name}_frame_{frame_count}.jpg")
            cv2.imwrite(output_path, frame)
            print(f"Frame {frame_count} saved to {output_path}")

        frame_count += 1

    # Release the video capture object
    cap.release()

if __name__ == "__main__":
    video_path = input("Enter the path to the video file: ")
    fps = 2  # Desired frame rate

    extract_frames(video_path, fps)
    print("Done")
