"""
Frame Extraction Script
======================
Extract JPEG frames from MP4 video for use with EdgeTAM.
"""

import cv2
import os
from pathlib import Path

def extract_frames(video_path, output_dir, frame_prefix="frame"):
    """
    Extract frames from video and save as JPEG files.
    
    Args:
        video_path: Path to the input video file
        output_dir: Directory to save extracted frames
        frame_prefix: Prefix for frame filenames (default: "frame")
    """
    # Create output directory if it doesn't exist
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    # Open video
    cap = cv2.VideoCapture(str(video_path))
    
    if not cap.isOpened():
        raise ValueError(f"Could not open video file: {video_path}")
    
    # Get video properties
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    print(f"Video: {video_path}")
    print(f"Properties: {width}x{height}, {fps} FPS, {total_frames} frames")
    print(f"Output directory: {output_dir}")
    print(f"Extracting frames...")
    
    frame_count = 0
    extracted_count = 0
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        # Save frame as JPEG
        frame_filename = f"{frame_count:05d}.jpg"
        frame_path = output_path / frame_filename
        
        # Save with high quality
        cv2.imwrite(str(frame_path), frame, [cv2.IMWRITE_JPEG_QUALITY, 95])
        
        extracted_count += 1
        frame_count += 1
        
        # Progress indicator
        if frame_count % 30 == 0:
            print(f"Extracted {frame_count}/{total_frames} frames ({frame_count/total_frames*100:.1f}%)")
    
    cap.release()
    
    print(f"\n✅ Successfully extracted {extracted_count} frames!")
    print(f"📁 Frames saved in: {output_dir}")
    print(f"📄 Frame naming: {frame_prefix}_00000.jpg, {frame_prefix}_00001.jpg, ...")
    
    return extracted_count

def main():
    # Configuration
    video_path = "/Users/nandinilreddy/Desktop/edgeTam/EdgeTAM/notebooks/videos/pedestrain.mp4"
    output_dir = "/Users/nandinilreddy/Desktop/edgeTam/EdgeTAM/notebooks/videos/pedestrain-frames"
    
    try:
        # Extract frames
        extracted_count = extract_frames(video_path, output_dir, frame_prefix="frame")
        
        print(f"\n🎯 Usage with EdgeTAM:")
        print(f"   Update your wildlife.py script to use:")
        print(f"   video_path = \"{output_dir}\"")
        print(f"   # Instead of the MP4 file path")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        print("Make sure:")
        print("1. The video file exists at the specified path")
        print("2. You have write permissions to the output directory")
        print("3. OpenCV is properly installed")

if __name__ == "__main__":
    
    main()