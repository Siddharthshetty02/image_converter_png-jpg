from PIL import Image
import os

def convert_png_to_jpg(input_path, output_path):
    """
    Converts a PNG image to JPG format.

    Args:
        input_path (str): Path to the input PNG image.
        output_path (str): Path to save the converted JPG image.
    """
    try:
        # Open the PNG image
        with Image.open(input_path) as img:
            # Ensure the image has an RGB mode
            if img.mode != 'RGB':
                img = img.convert('RGB')
            
            # Save as JPG
            img.save(output_path, "JPEG")
            print(f"Image converted and saved to: {output_path}")
    except Exception as e:
        print(f"Error: {e}")

def main():
    print("PNG to JPG Image Converter")
    input_folder = "images"
    output_folder = "converted_images"
    
    # Create folders if they don't exist
    if not os.path.exists(input_folder):
        os.makedirs(input_folder)
        print(f"Created folder: {input_folder}. Place your PNG images here.")
        return

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # List all PNG files in the input folder
    png_files = [f for f in os.listdir(input_folder) if f.lower().endswith('.png')]

    if not png_files:
        print(f"No PNG files found in the folder: {input_folder}")
        return

    # Convert each PNG to JPG
    for png_file in png_files:
        input_path = os.path.join(input_folder, png_file)
        output_file = os.path.splitext(png_file)[0] + ".jpg"
        output_path = os.path.join(output_folder, output_file)
        convert_png_to_jpg(input_path, output_path)

if __name__ == "__main__":
    main()
