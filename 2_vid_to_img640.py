import cv2
import os

def extract_frames(video_path, fps, target_size=(640, 640)):
    """Extracts frames from a video at a specified frame rate, resizing them to the
    target size.

    Args:
        video_path: The path to the video file.
        fps: The desired frame rate.
        target_size: A tuple representing the desired width and height (default: (640, 640)).
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
            # Resize the frame to the target size
            resized_frame = cv2.resize(frame, target_size, interpolation=cv2.INTER_AREA)

            # Construct the output path
            output_path = os.path.join(output_dir, f"{video_name}_frame_{frame_count}.jpg")

            # Save the resized frame
            cv2.imwrite(output_path, resized_frame)
            print(f"Frame {frame_count} saved (resized to {target_size}) to {output_path}")

        frame_count += 1

    # Release the video capture object
    cap.release()

if __name__ == "__main__":
    video_path = input("Enter the path to the video file: ")
    fps = 5  # Desired frame rate

    extract_frames(video_path, fps)
    print("Done")