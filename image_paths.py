import os


class get_paths():
  '''return list of iamges from source path
  Parameters
  ----------
  image_types: tuple of image types 
  src_path: string indicating directory to get image paths for 


  Returns
  -------
  list of image paths
  Examples
  from image_paths import get_paths

  image_paths = get_paths(src_path = "in_path").full_paths()

  '''
  def __init__(self, src_path, image_types = (".jpg", ".png", ".JPG", ".PNG", ".JPEG", ".tif", ".tiff", ".TIFF", '.TIF')):
    self.src_path = src_path
    self.image_type = image_types
    

  def full_paths(self):
    self.image_paths = []  
    for root, dirs, files in os.walk(self.src_path):
      self.image_paths.extend([os.path.join(root, f) for f in files if f.endswith(self.image_type)])

    return self.image_paths