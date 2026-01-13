# 📦 S3 Image Downloader - Download Images from AWS S3 Bucket

![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![AWS S3](https://img.shields.io/badge/AWS-S3-orange)

**Simple Python script to download images from AWS S3 bucket with progress tracking.** Perfect for bulk downloading S3 images, backup, and migration. Fast, easy to use, and free!

## 🔍 Keywords

`s3 image downloader` `download images from s3` `aws s3 downloader python` `boto3 download images` `s3 bulk download` `s3 image backup` `python s3 downloader` `download all images from s3 bucket` `s3 batch download` `aws s3 image backup tool`

## ✨ Features

- 📥 **Download images from AWS S3 bucket** - Bulk download all images
- 📊 **Progress bar** - Real-time download progress with tqdm
- ⏭️ **Skip existing files** - Automatically skip already downloaded images
- 📁 **Preserve folder structure** - Keep your S3 folder organization (flat mode optional)
- 🎯 **Image format filtering** - Download only image files (jpg, png, webp, gif, bmp)
- 🔒 **Secure credentials** - Use AWS CLI or environment variables
- 🛡️ **Error handling** - Robust error recovery and retry logic
- 💨 **Easy configuration** - Simple setup in 2 minutes
- 🆓 **Free and open source** - MIT License

## 📋 Requirements

- Python 3.7 or higher
- AWS account with S3 access
- boto3 library (AWS SDK for Python)
- tqdm library (progress bar)

## 🚀 Quick Start - Download S3 Images in 3 Steps

### Step 1: Clone and Install
```bash
# Clone this S3 image downloader repository
git clone https://github.com/YOUR_USERNAME/s3-image-downloader.git
cd s3-image-downloader

# Install dependencies (boto3 and tqdm)
pip install -r requirements.txt
```

### Step 2: Configure AWS Credentials

**Option A: Use AWS CLI (Recommended)**
```bash
aws configure
# Enter your AWS Access Key ID
# Enter your AWS Secret Access Key
# Enter default region (e.g., us-east-1, ap-south-1)
```

**Option B: Edit Script**

Open `download_s3.py` and update these values:
```python
BUCKET_NAME = 'your-s3-bucket-name'
S3_FOLDER = 'images/'  # Folder path in S3 bucket (or '' for root)
LOCAL_FOLDER = './downloads'  # Where to save images locally
```

### Step 3: Download Images from S3
```bash
python download_s3.py
```

That's it! Your S3 images will download with a progress bar! 🎉

## 📖 How to Download Images from AWS S3 Bucket

### Example 1: Download All Images from S3 Bucket Root
```python
BUCKET_NAME = 'my-images-bucket'
S3_FOLDER = ''  # Empty string = download from root
LOCAL_FOLDER = './all-images'
```

### Example 2: Download Images from Specific S3 Folder
```python
BUCKET_NAME = 'ecommerce-bucket'
S3_FOLDER = 'products/thumbnails/'  # Specific folder
LOCAL_FOLDER = './product-images'
```

### Example 3: Bulk Download S3 Images for Backup
```python
BUCKET_NAME = 'backup-bucket'
S3_FOLDER = 'backup/2024/'
LOCAL_FOLDER = './backup-downloads'
```

## 🎯 Supported Image Formats

This S3 image downloader supports:
- `.jpg` / `.jpeg` - JPEG images
- `.png` - PNG images
- `.webp` - WebP images
- `.gif` - GIF images
- `.bmp` - Bitmap images

## 🔧 Configuration Guide

Edit these variables in `download_s3.py`:

| Variable | Description | Example |
|----------|-------------|---------|
| `BUCKET_NAME` | Your AWS S3 bucket name | `'my-images-bucket'` |
| `S3_FOLDER` | Folder path in S3 bucket | `'images/products/'` or `''` for root |
| `LOCAL_FOLDER` | Local directory to save images | `'./downloads'` |
| `AWS_ACCESS_KEY_ID` | AWS access key (optional) | Leave empty to use AWS CLI |
| `AWS_SECRET_ACCESS_KEY` | AWS secret key (optional) | Leave empty to use AWS CLI |
| `AWS_REGION` | AWS region name | `'us-east-1'`, `'ap-south-1'`, etc. |

## 💡 Common Use Cases

### Use Case 1: Backup S3 Images
Download all images from your S3 bucket for backup:
```bash
python download_s3.py
# Downloads all images with progress tracking
```

### Use Case 2: Migrate S3 Images
Transfer images from one S3 bucket to local storage:
- Set `BUCKET_NAME` to source bucket
- Set `LOCAL_FOLDER` to destination
- Run script to download all images

### Use Case 3: Download Product Images
E-commerce sites can bulk download product images:
```python
S3_FOLDER = 'products/images/'
LOCAL_FOLDER = './product-catalog'
```

### Use Case 4: Download User Uploads
Download user-uploaded images from S3:
```python
S3_FOLDER = 'user-uploads/2024/'
LOCAL_FOLDER = './user-images'
```

## 📊 Output Example
```
🚀 S3 Bucket Image Downloader
==================================================
📦 Bucket: my-images-bucket
📁 S3 Folder: products/
💾 Local Folder: ./downloads
==================================================
🔑 Using AWS CLI credentials

📋 Listing images from S3 bucket...
✅ Found 150 images

📥 Downloading images from S3...
Progress: 100%|████████████████| 150/150 [00:45<00:00, 3.33file/s]

==================================================
✨ Download Complete!
✅ Successful: 148
⏭️  Skipped (already exists): 2
❌ Failed: 0
📁 Files saved to: ./downloads
==================================================
```

## 🐛 Troubleshooting - S3 Download Issues

### Error: "No module named 'tqdm'" or "No module named 'boto3'"

**Solution:**
```bash
pip install boto3 tqdm
# or
pip install -r requirements.txt
```

### Error: "No credentials found" / "Unable to locate credentials"

**Solution:**
```bash
# Configure AWS CLI with your credentials
aws configure

# Or set environment variables
export AWS_ACCESS_KEY_ID=your-access-key
export AWS_SECRET_ACCESS_KEY=your-secret-key
```

### Error: "Access Denied" when downloading from S3

**Solution:**
- Verify your S3 bucket name is correct
- Check IAM user has `s3:GetObject` and `s3:ListBucket` permissions
- Ensure AWS credentials are valid and not expired
- Verify bucket policy allows access

### Error: "No images found" in S3 bucket

**Solution:**
- Check `S3_FOLDER` path is correct (case-sensitive!)
- Verify images actually exist in that S3 location
- Try empty string `''` to search entire bucket
- Check `IMAGE_EXTENSIONS` includes your file types

### Downloads are very slow

**Solution:**
- Check your internet connection speed
- Use AWS region closer to your location
- Consider using AWS DataSync for very large transfers
- Check if S3 bucket has transfer acceleration enabled

## 🔒 Security Best Practices for S3 Downloads

### 1. Use AWS CLI Credentials (Best)
```bash
aws configure
# Stores credentials securely in ~/.aws/credentials
```

### 2. Use Environment Variables
```bash
export AWS_ACCESS_KEY_ID=your-key
export AWS_SECRET_ACCESS_KEY=your-secret
python download_s3.py
```

### 3. Use IAM Roles (For EC2/Lambda)
No credentials needed - automatic authentication when running on AWS infrastructure

### 4. Never Commit AWS Credentials
- ✅ Use `.gitignore` to exclude credentials
- ✅ Use AWS CLI or environment variables
- ❌ Never hardcode keys in scripts
- ❌ Never commit credentials to GitHub

### 5. Grant Minimal S3 Permissions

IAM Policy for S3 image downloads (copy this to your IAM policy):
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:ListBucket"
      ],
      "Resource": [
        "arn:aws:s3:::your-bucket-name",
        "arn:aws:s3:::your-bucket-name/*"
      ]
    }
  ]
}
```

## 📈 Performance - S3 Download Speed

Typical download speeds (depends on internet and S3 region):
- **Small images (< 100KB):** ~50-100 images/second
- **Medium images (100KB-1MB):** ~10-30 images/second
- **Large images (> 1MB):** ~5-15 images/second

**Tips for faster S3 downloads:**
1. Use S3 bucket in same region as your location
2. Use AWS Transfer Acceleration for S3
3. Increase bandwidth/internet speed
4. Consider multi-threaded downloads for very large batches

## 🆚 Comparison with Other S3 Download Tools

| Feature | This Tool | AWS CLI | AWS Console | s3cmd |
|---------|-----------|---------|-------------|-------|
| **Easy Setup** | ✅ Very Easy | ⚠️ Medium | ✅ Easy | ⚠️ Medium |
| **Progress Bar** | ✅ Yes | ❌ No | ✅ Yes | ⚠️ Basic |
| **Skip Existing** | ✅ Yes | ⚠️ With flag | ❌ No | ✅ Yes |
| **Image Filter** | ✅ Yes | ⚠️ Manual | ❌ No | ⚠️ Manual |
| **Python Script** | ✅ Yes | ❌ No | ❌ No | ❌ No |
| **Free** | ✅ Yes | ✅ Yes | ✅ Yes | ✅ Yes |
| **Customizable** | ✅ Very | ⚠️ Limited | ❌ No | ⚠️ Some |

## 📁 Project Structure
```
s3-image-downloader/
├── download_s3.py          # Main Python script for S3 downloads
├── requirements.txt        # Dependencies (boto3, tqdm)
├── .gitignore             # Git ignore file
├── README.md              # This documentation
├── LICENSE                # MIT License
└── downloads/             # Downloaded images go here (auto-created)
```

## 🤝 Contributing to S3 Image Downloader

Contributions are welcome! You can help by:
- 🐛 Reporting bugs or S3 download issues
- 💡 Suggesting new features (multi-threading, resume support, etc.)
- 📖 Improving documentation
- 🔧 Submitting pull requests
- ⭐ Starring this repository

## 📄 License

MIT License - free to use, modify, and distribute.

See [LICENSE](LICENSE) file for full details.

## 🙏 Built With

- [boto3](https://boto3.amazonaws.com/) - AWS SDK for Python
- [tqdm](https://github.com/tqdm/tqdm) - Progress bar library
- Python 3.7+

## ⭐ Star This Repository

If this S3 image downloader helped you, please give it a ⭐️ on GitHub!

It helps others discover this tool!

## 📧 Support & Questions

- 🐛 **Report Issues:** [GitHub Issues](https://github.com/YOUR_USERNAME/s3-image-downloader/issues)
- 💬 **Ask Questions:** [GitHub Discussions](https://github.com/YOUR_USERNAME/s3-image-downloader/discussions)
- 📚 **Documentation:** This README

## 🔗 Related Resources

- [AWS S3 Documentation](https://docs.aws.amazon.com/s3/)
- [boto3 Documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
- [AWS CLI S3 Commands](https://docs.aws.amazon.com/cli/latest/reference/s3/)
- [Python AWS Examples](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python)

## 🎯 Popular Searches That Find This Tool

- How to download images from S3 bucket Python
- AWS S3 bulk image downloader
- Download all files from S3 bucket Python script
- boto3 download images from S3
- Python script to download S3 bucket contents
- S3 image backup tool
- Bulk download from AWS S3
- Download entire S3 bucket Python
- S3 to local storage migration
- AWS S3 image transfer script

## 📊 Repository Stats

![GitHub stars](https://img.shields.io/github/stars/YOUR_USERNAME/s3-image-downloader)
![GitHub forks](https://img.shields.io/github/forks/YOUR_USERNAME/s3-image-downloader)
![GitHub issues](https://img.shields.io/github/issues/YOUR_USERNAME/s3-image-downloader)
![GitHub last commit](https://img.shields.io/github/last-commit/YOUR_USERNAME/s3-image-downloader)

---

**Made with ❤️ for easy S3 image downloads | Fast • Simple • Free**

**Keywords:** s3 downloader, aws s3 download, python s3, boto3, image downloader, bulk download s3, s3 backup, aws tools, python script, s3 image backup, download from s3 bucket, s3 migration tool
