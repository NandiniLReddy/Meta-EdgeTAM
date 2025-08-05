#!/usr/bin/env python3
"""
Rename frames from frame_XXXXX.jpg to XXXXX.jpg format
for EdgeTAM compatibility
"""

import os
from pathlib import Path

def rename_frames(frames_dir):
    """
    Rename frames from frame_XXXXX.jpg to XXXXX.jpg format
    
    Args:
        frames_dir: Directory containing the frame files
    """
    frames_path = Path(frames_dir)
    
    if not frames_path.exists():
        raise ValueError(f"Directory does not exist: {frames_dir}")
    
    # Find all frame files
    frame_files = [f for f in frames_path.glob("frame_*.jpg")]
    
    if not frame_files:
        print("No frame_*.jpg files found to rename")
        return
    
    print(f"Found {len(frame_files)} frames to rename")
    
    renamed_count = 0
    
    for frame_file in sorted(frame_files):
        # Extract the number part from frame_00123.jpg -> 00123
        old_name = frame_file.name
        number_part = old_name.replace("frame_", "").replace(".jpg", "")
        new_name = f"{number_part}.jpg"
        
        old_path = frame_file
        new_path = frames_path / new_name
        
        # Rename the file
        old_path.rename(new_path)
        renamed_count += 1
        
        if renamed_count % 100 == 0:
            print(f"Renamed {renamed_count}/{len(frame_files)} files...")
    
    print(f"✅ Successfully renamed {renamed_count} frames!")
    print(f"   From: frame_00000.jpg, frame_00001.jpg, ...")
    print(f"   To:   00000.jpg, 00001.jpg, ...")
    
    return renamed_count

def main():
    frames_dir = "/Users/nandinilreddy/Desktop/edgeTam/EdgeTAM/notebooks/videos/wild-life-frames"
    
    try:
        rename_frames(frames_dir)
        
        print(f"\n🎯 Now you can use EdgeTAM with:")
        print(f"   video_dir = \"{frames_dir}\"")
        print(f"   # EdgeTAM will find files: 00000.jpg, 00001.jpg, etc.")
        
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()