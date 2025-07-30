import os
import shutil

# Base directories
base_source_dir = os.path.join('assets', 'media')
destination_dir = os.path.join('assets', 'media', 'agency_imgs')

# Ensure destination directory exists
os.makedirs(destination_dir, exist_ok=True)

# List of relative image paths
image_paths = [
    'web_imgs/Landscaping Pics/IMG-20250414-WA0061.jpg',
    'web_imgs/Landscaping Pics/IMG-20250414-WA0060.jpg',
    'web_imgs/Landscaping Pics/IMG-20250414-WA0061.jpg',  # Duplicate
    'web_imgs/Landscaping Pics/IMG-20250312-WA0044.jpg',
    'web_imgs/Landscaping Pics/IMG-20250312-WA0046.jpg',
    'web_imgs/Landscaping Pics/IMG-20250312-WA0047.jpg',
    'web_imgs/Landscaping Pics/Residential Projects/20240630_095813.jpg',
    'web_imgs/Water Resource Engineering/IMG5659jpeg5e6f6a4a243e8jpeg_5f3690a4633fc.jpg',
    'web_imgs/Landscaping Pics/Earth Works/IMG-20250322-WA0059.jpg',
    'web_imgs/Landscaping Pics/IMG-20250205-WA0041.jpg',
    'web_imgs/Landscaping Pics/IMG-20250312-WA0049.jpg',
    'web_imgs/Landscaping Pics/8d183363b2cbfc4c21708af1fb61ed92.jpg',
    'web_imgs/Landscaping Pics/sv.png',
    'web_imgs/Landscaping Pics/IMG-20241019-WA0068.jpg',
    'web_imgs/Landscaping Pics/IMG-20241019-WA0084.jpg',
    'web_imgs/Landscaping Pics/IMG-20241019-WA0004.jpg',
    'web_imgs/Landscaping Pics/surveyor.webp',
    'web_imgs/Clientale/IMG-20250512-WA0031.jpg',
    'web_imgs/Clientale/IMG-20250512-WA0032.jpg',
    'web_imgs/Clientale/IMG-20250512-WA0033.jpg'
]

# Track already copied files to avoid duplicates
copied_files = set()

for relative_path in image_paths:
    source_path = os.path.join(base_source_dir, relative_path)

    # Remove 'web_imgs/' prefix to reconstruct the subpath
    relative_subpath = os.path.relpath(relative_path, start='web_imgs')
    target_path = os.path.join(destination_dir, relative_subpath)

    # Skip if already copied
    if target_path in copied_files:
        print(f"Skipping duplicate: {target_path}")
        continue

    # Ensure destination directory exists
    os.makedirs(os.path.dirname(target_path), exist_ok=True)

    try:
        shutil.copy2(source_path, target_path)
        print(f"Copied: {source_path} -> {target_path}")
        copied_files.add(target_path)
    except FileNotFoundError:
        print(f"File not found: {source_path}")
    except Exception as e:
        print(f"Error copying {source_path}: {e}")
