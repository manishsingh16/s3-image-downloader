# 📦 S3 Bucket Image Downloader

Simple Python script to download images from AWS S3 buckets with progress tracking and error handling.

![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

## ✨ Features

- 📥 Download images from S3 buckets
- 📊 Progress bar with tqdm
- ⏭️ Auto-skip already downloaded files
- 🎯 Filter by image extensions
- 🔒 Secure credential handling
- 🛡️ Error handling and recovery
- 💨 Simple and easy to use

## 📋 Requirements

- Python 3.7 or higher
- AWS account with S3 access
- boto3 library
- tqdm library

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/s3-bucket-image-downloader.git
cd s3-bucket-image-downloader
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure AWS Credentials

**Option A: Using AWS CLI (Recommended)**
```bash
aws configure
```

**Option B: Edit the Script**

Open `download_s3.py` and update these values:
```python
BUCKET_NAME = 'your-bucket-name'
S3_FOLDER = 'images/'  # or '' for root
LOCAL_FOLDER = './downloads'

# Optional: Add credentials directly
AWS_ACCESS_KEY_ID = 'your-access-key'
AWS_SECRET_ACCESS_KEY = 'your-secret-key'
AWS_REGION = 'ap-south-1'
```

### 4. Run the Script

```bash
python download_s3.py
```

## 📖 Configuration

Edit these variables in `download_s3.py`:

| Variable | Description | Example |
|----------|-------------|---------|
| `BUCKET_NAME` | Your S3 bucket name | `'my-images-bucket'` |
| `S3_FOLDER` | Folder path in S3 | `'products/images/'` or `''` |
| `LOCAL_FOLDER` | Local download directory | `'./downloads'` |
| `AWS_ACCESS_KEY_ID` | AWS access key (optional) | Leave empty to use AWS CLI |
| `AWS_SECRET_ACCESS_KEY` | AWS secret key (optional) | Leave empty to use AWS CLI |
| `AWS_REGION` | AWS region | `'ap-south-1'`, `'us-east-1'`, etc. |

## 🎯 Supported Image Formats

- `.jpg` / `.jpeg`
- `.png`
- `.webp`
- `.gif`
- `.bmp`

## 💡 Usage Examples

### Example 1: Download from Root Bucket
```python
BUCKET_NAME = 'my-bucket'
S3_FOLDER = ''  # Empty for root
LOCAL_FOLDER = './all-images'
```

### Example 2: Download from Specific Folder
```python
BUCKET_NAME = 'ecommerce-bucket'
S3_FOLDER = 'products/thumbnails/'
LOCAL_FOLDER = './thumbnails'
```

### Example 3: Using AWS CLI Credentials
```python
# Leave these empty to use AWS CLI credentials
AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY = ''
```

Then run:
```bash
aws configure  # Set up credentials once
python download_s3.py
```

## 🔒 Security Best Practices

1. **Use AWS CLI credentials** instead of hardcoding keys
   ```bash
   aws configure
   ```

2. **Use environment variables** for credentials
   ```bash
   export AWS_ACCESS_KEY_ID=your-key
   export AWS_SECRET_ACCESS_KEY=your-secret
   ```

3. **Never commit credentials** to Git (already in .gitignore)

4. **Use IAM roles** when running on EC2/ECS

5. **Grant minimal permissions** (only `s3:GetObject`, `s3:ListBucket`)

### Example IAM Policy

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

## 🐛 Troubleshooting

### Error: "No credentials found"

**Solution:**
```bash
aws configure
# Then enter your AWS credentials
```

### Error: "Access Denied"

**Solution:**
- Verify bucket name is correct
- Check IAM permissions (need `s3:GetObject` and `s3:ListBucket`)
- Ensure credentials are valid

### Error: "No images found"

**Solution:**
- Check `S3_FOLDER` path is correct (case-sensitive)
- Verify files exist in that location
- Check `IMAGE_EXTENSIONS` includes your file types

### Downloads are Slow

**Solution:**
- Check your internet connection
- AWS region closer to you = faster downloads
- Consider using the advanced multi-threaded version

## 📊 Output Example

```
🚀 S3 Bucket Image Downloader
==================================================
📦 Bucket: my-images-bucket
📁 S3 Folder: products/
💾 Local Folder: ./downloads
==================================================
🔑 Using AWS CLI credentials

📋 Listing images from S3...
✅ Found 150 images

📥 Downloading images...
Progress: 100%|████████████████| 150/150 [00:45<00:00, 3.33file/s]

==================================================
✨ Download Complete!
✅ Successful: 148
⏭️  Skipped (already exists): 2
❌ Failed: 0
📁 Files saved to: ./downloads
==================================================
```

## 🔄 Update Configuration

To update settings, simply edit `download_s3.py`:

```python
# Update these values
BUCKET_NAME = 'new-bucket-name'
S3_FOLDER = 'new-folder/'
LOCAL_FOLDER = './new-downloads'
```

Then run again:
```bash
python download_s3.py
```

## 📁 Project Structure

```
s3-bucket-image-downloader/
├── download_s3.py          # Main script
├── requirements.txt        # Python dependencies
├── .gitignore             # Git ignore rules
├── README.md              # This file
└── LICENSE                # MIT License
```

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest features
- Submit pull requests

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with [boto3](https://boto3.amazonaws.com/) - AWS SDK for Python
- Progress bars by [tqdm](https://github.com/tqdm/tqdm)

## 📧 Support

If you encounter issues:
1. Check the troubleshooting section above
2. Open an issue on GitHub
3. Review AWS S3 documentation

## 🌟 Show Your Support

If this project helped you, please give it a ⭐️!

---

**Made with ❤️ for easy S3 downloads**
