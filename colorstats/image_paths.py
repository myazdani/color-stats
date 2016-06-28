import os

def rel_paths(src_path, image_types = (".jpg", ".png", ".JPG", ".PNG", ".JPEG", ".tif", ".tiff", ".TIFF", '.TIF')):
  image_paths = []  
  for root, dirs, files in os.walk(src_path):
    image_paths.extend([os.path.join(root, f) for f in files if f.endswith(image_types)])
  return image_paths
