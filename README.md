# PNG to JPG Image Converter

A Python project to convert PNG images to JPG format.

## Features
- Batch conversion of PNG images.
- Saves converted images in a separate folder.

## Requirements
- Python 3.x
- Install dependencies:

## How to Use
1. Clone or download the repository.
2. Navigate to the project folder:
3. Create an `images/` folder if it doesn't already exist.
4. Place PNG images in the `images/` folder.
5. Run the script:
6. Find the converted JPG images in the `converted_images/` folder.

## Folder Structure

image-converter/ ├── converter.py # Main script ├── images/ # Folder to store input images ├── converted_images/ # Folder to save converted images └── README.md # Project description and instructions


## Notes
- Ensure all PNG files are placed in the `images/` folder before running the script.
- Converted images are saved with the same name but with a `.jpg` extension.

Enhancements
GUI Interface: Use Tkinter or PyQt to create a drag-and-drop interface for image uploads.
Format Flexibility: Add options to convert between other formats like BMP, GIF, and TIFF.
Error Handling: Notify the user about corrupted files or unsupported formats.
Batch Conversion Progress: Show a progress bar during the batch conversion process.
