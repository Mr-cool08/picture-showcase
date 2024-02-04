import os

photo_folder = 'static/photos'
absolute_path = os.path.abspath(photo_folder)
print(f"Absolute path to photos: {absolute_path}")