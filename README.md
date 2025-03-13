# HEIC to JPG Converter

A simple Python script to convert HEIC images to JPG format. The script automatically detects ImageMagick installation and provides a user-friendly way to convert multiple HEIC files at once.

## Features

- Automatically converts all HEIC files in the current directory to JPG format
- Detects ImageMagick installation automatically
- Works on Windows, macOS, and Linux
- Option to delete original HEIC files after conversion
- Handles both uppercase (.HEIC) and lowercase (.heic) extensions
- Skips already converted files

## Prerequisites

1. Python 3.6 or higher
2. ImageMagick

## Installation

### 1. Python Installation

If you don't have Python installed:

- **Windows**: Download and install from [python.org](https://www.python.org/downloads/)
- **macOS**: 
  ```bash
  brew install python
  ```
- **Linux**:
  ```bash
  sudo apt-get update
  sudo apt-get install python3
  ```

### 2. ImageMagick Installation

#### Windows
1. Visit [ImageMagick Download Page](https://imagemagick.org/script/download.php)
2. Download and run the installer for your Windows version
3. During installation, ensure you check "Add to system path" option

#### macOS
Using Homebrew:
```bash
brew install imagemagick
```

#### Linux
- Ubuntu/Debian:
  ```bash
  sudo apt-get update
  sudo apt-get install imagemagick
  ```
- Fedora:
  ```bash
  sudo dnf install imagemagick
  ```

## Usage

1. Download the `HeicToJPG.py` script
2. Place it in the directory containing your HEIC files
3. Open a terminal/command prompt in that directory
4. Run the script:
   ```bash
   python HeicToJPG.py
   ```
5. Follow the prompts

The script will:
- Check for ImageMagick installation
- Find all HEIC files in the current directory
- Convert them to JPG format
- Ask if you want to delete the original HEIC files

## Example Output

```
HEIC to JPG Converter
--------------------
Found ImageMagick at: C:\Program Files\ImageMagick-7.1.1-Q16-HDRI\magick.exe

Found 10 HEIC files to process.
Converting IMG_0001.heic...
Successfully converted IMG_0001.heic
[...]

Conversion complete!
Successfully converted: 10

Do you want to delete the original HEIC files? (yes/no):
```

## Contributing

Feel free to fork this repository and submit pull requests for any improvements.


