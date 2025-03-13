import os
import subprocess
import sys
from pathlib import Path
import winreg  # For Windows registry

def find_imagemagick():
    """Find ImageMagick installation path."""
    if sys.platform == "win32":
        # Try common Windows installation paths
        try:
            # Try to get path from Windows registry
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r'SOFTWARE\ImageMagick\Current') as key:
                install_path = winreg.QueryValue(key, None)
                magick_exe = Path(install_path) / "magick.exe"
                if magick_exe.exists():
                    return magick_exe
        except WindowsError:
            pass

        # Try common Program Files locations
        program_files = [
            os.environ.get('ProgramFiles', 'C:\\Program Files'),
            os.environ.get('ProgramFiles(x86)', 'C:\\Program Files (x86)')
        ]
        
        for pf in program_files:
            # Search for ImageMagick folders
            pf_path = Path(pf)
            if pf_path.exists():
                for item in pf_path.glob("ImageMagick*"):
                    magick_exe = item / "magick.exe"
                    if magick_exe.exists():
                        return magick_exe
    
    else:  # macOS, Linux, etc.
        # Try common Unix-like system paths
        common_paths = [
            "/usr/bin/magick",
            "/usr/local/bin/magick",
            "/opt/homebrew/bin/magick"  # Common macOS Homebrew path
        ]
        
        for path in common_paths:
            if Path(path).exists():
                return Path(path)
        
        # Try finding in PATH
        try:
            result = subprocess.run(['which', 'magick'], 
                                  capture_output=True, 
                                  text=True)
            if result.returncode == 0:
                return Path(result.stdout.strip())
        except:
            pass

    return None

def check_imagemagick_installation():
    """Check if ImageMagick is installed and guide user to install if not found."""
    magick_path = find_imagemagick()
    
    if not magick_path:
        print("ImageMagick not found! Please install ImageMagick:")
        if sys.platform == "win32":
            print("\n1. Visit: https://imagemagick.org/script/download.php")
            print("2. Download and install the Windows version")
            print("3. Run this script again")
        else:
            print("\nInstall using your package manager:")
            print("- macOS (Homebrew): brew install imagemagick")
            print("- Ubuntu/Debian: sudo apt-get install imagemagick")
            print("- Fedora: sudo dnf install imagemagick")
        sys.exit(1)
        
    return magick_path

def convert_heic_to_jpg(heic_file, magick_path):
    try:
        # Create output filename
        output_file = heic_file.with_suffix(".jpg")
        
        # Skip if output already exists
        if output_file.exists():
            print(f"Skipping {heic_file.name} - JPG already exists")
            return True
        
        print(f"Converting {heic_file.name}...")
        result = subprocess.run(
            [magick_path, str(heic_file.absolute()), str(output_file.absolute())],
            capture_output=True,
            text=True
        )
        
        if result.returncode == 0:
            print(f"Successfully converted {heic_file.name}")
            return True
        else:
            print(f"Error converting {heic_file.name}: {result.stderr}")
            return False
    except Exception as e:
        print(f"Error processing {heic_file.name}: {str(e)}")
        return False

def delete_heic_files():
    # Get all HEIC files again to ensure we are working with current state
    current_dir = Path(".")
    heic_files = list(current_dir.glob("*.HEIC")) + list(current_dir.glob("*.heic"))
    deleted_count = 0
    deleted_files = set()  # Keep track of already deleted files
    
    for heic_file in heic_files:
        if heic_file.name not in deleted_files:  # Only process if not already deleted
            jpg_file = heic_file.with_suffix(".jpg")
            if jpg_file.exists():  # Only delete if JPG exists
                try:
                    heic_file.unlink()
                    print(f"Deleted: {heic_file.name}")
                    deleted_count += 1
                    deleted_files.add(heic_file.name)
                except Exception as e:
                    print(f"Error deleting {heic_file.name}: {str(e)}")
        
    return deleted_count

def main():
    print("HEIC to JPG Converter")
    print("--------------------")
    
    # Find ImageMagick installation
    magick_path = check_imagemagick_installation()
    print(f"Found ImageMagick at: {magick_path}\n")
        
    # Get current directory
    current_dir = Path(".")
    
    # Find all HEIC files (case insensitive)
    heic_files = list(current_dir.glob("*.HEIC")) + list(current_dir.glob("*.heic"))
    
    if not heic_files:
        print("No HEIC files found in the current directory.")
        return
        
    print(f"Found {len(heic_files)} HEIC files to process.")
    
    # Convert files
    success_count = 0
    fail_count = 0
    
    for file in heic_files:
        if convert_heic_to_jpg(file, magick_path):
            success_count += 1
        else:
            fail_count += 1
            
    # Print conversion summary
    print("\nConversion complete!")
    print(f"Successfully converted: {success_count}")
    if fail_count > 0:
        print(f"Failed conversions: {fail_count}")

    # Ask if user wants to delete original HEIC files
    if success_count > 0:
        delete_confirmation = input("\nDo you want to delete the original HEIC files? (yes/no): ")
        if delete_confirmation.lower() == "yes":
            deleted = delete_heic_files()
            print(f"\nSuccessfully deleted {deleted} HEIC files.")
        else:
            print("\nOriginal HEIC files have been kept.")

if __name__ == "__main__":
    main()
