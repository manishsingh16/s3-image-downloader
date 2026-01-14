#!/usr/bin/env python3
"""
S3 Bucket Image Downloader
Download images from AWS S3 bucket with progress tracking
"""

import boto3
import os
from tqdm import tqdm

# ============================================
# CONFIGURATION - UPDATE THESE VALUES
# ============================================
BUCKET_NAME = 'your-bucket-name'          # Your S3 bucket name
S3_FOLDER = 'your-folder-path/'           # S3 folder path (e.g., 'images/' or '')
LOCAL_FOLDER = './downloads'              # Local download folder

# AWS Credentials (Optional - leave empty to use AWS CLI config)
AWS_ACCESS_KEY_ID = ''                    # Your AWS access key
AWS_SECRET_ACCESS_KEY = ''                # Your AWS secret key
AWS_REGION = 'ap-south-1'                 # AWS region

# Image file extensions to download
IMAGE_EXTENSIONS = ('.jpg', '.jpeg', '.png', '.webp', '.gif', '.bmp')

# ============================================
# SCRIPT - NO NEED TO EDIT BELOW
# ============================================

def download_images():
    """Download images from S3 bucket with progress bar."""
    
    print("🚀 S3 Bucket Image Downloader")
    print("=" * 50)
    print(f"📦 Bucket: {BUCKET_NAME}")
    print(f"📁 S3 Folder: {S3_FOLDER or '(root)'}")
    print(f"💾 Local Folder: {LOCAL_FOLDER}")
    print("=" * 50)
    
    # Initialize S3 client
    if AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY:
        s3 = boto3.client(
            's3',
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
            region_name=AWS_REGION
        )
        print("🔑 Using provided credentials")
    else:
        s3 = boto3.client('s3', region_name=AWS_REGION)
        print("🔑 Using AWS CLI credentials")
    
    # Create local folder
    os.makedirs(LOCAL_FOLDER, exist_ok=True)
    
    # Get list of all images
    print("\n📋 Listing images from S3...")
    paginator = s3.get_paginator('list_objects_v2')
    image_files = []
    
    try:
        for page in paginator.paginate(Bucket=BUCKET_NAME, Prefix=S3_FOLDER):
            for obj in page.get('Contents', []):
                s3_key = obj['Key']
                if s3_key.lower().endswith(IMAGE_EXTENSIONS):
                    image_files.append(s3_key)
        
        if not image_files:
            print("⚠️  No images found!")
            return
        
        print(f"✅ Found {len(image_files)} images\n")
        
        # Download with progress bar
        print("📥 Downloading images...")
        successful = 0
        skipped = 0
        failed = 0
        
        with tqdm(total=len(image_files), desc="Progress", unit="file") as pbar:
            for s3_key in image_files:
                filename = os.path.basename(s3_key)
                local_path = os.path.join(LOCAL_FOLDER, filename)
                
                # Skip if already exists
                if os.path.exists(local_path):
                    skipped += 1
                    pbar.update(1)
                    continue
                
                try:
                    s3.download_file(BUCKET_NAME, s3_key, local_path)
                    successful += 1
                except Exception as e:
                    print(f"\n❌ Failed: {filename} - {e}")
                    failed += 1
                
                pbar.update(1)
        
        # Summary
        print("\n" + "=" * 50)
        print("✨ Download Complete!")
        print(f"✅ Successful: {successful}")
        print(f"⏭️  Skipped (already exists): {skipped}")
        print(f"❌ Failed: {failed}")
        print(f"📁 Files saved to: {LOCAL_FOLDER}")
        print("=" * 50)
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("\n💡 Tips:")
        print("  - Check your bucket name and folder path")
        print("  - Verify AWS credentials are correct")
        print("  - Ensure you have S3 read permissions")


if __name__ == "__main__":
    download_images()
