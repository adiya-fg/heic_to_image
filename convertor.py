import os
from PIL import Image
import pillow_heif

# Register HEIC/HEIF support
pillow_heif.register_heif_opener()

input_dir = "heic_images"   # folder with HEIC files
output_dir = "jpg_images"   # folder to save JPG files

os.makedirs(output_dir, exist_ok=True)

for file_name in os.listdir(input_dir):
    if file_name.lower().endswith((".heic", ".heif")):
        input_path = os.path.join(input_dir, file_name)
        output_path = os.path.join(
            output_dir,
            os.path.splitext(file_name)[0] + ".jpg"
        )

        with Image.open(input_path) as img:
            img = img.convert("RGB")  # JPG does not support alpha
            img.save(output_path, "JPEG", quality=95)

        print(f"Converted: {file_name} → JPG")