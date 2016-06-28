import numpy as np
from skimage.feature import hog
from sklearn.base import BaseEstimator, TransformerMixin
from ObjectDetector import ObjectRotateDetector
import cv2

class DimTransformer(BaseEstimator, TransformerMixin):
  '''Input list of image paths and return image with specified dimensions
  Parameters and Attributes
  ----------
  w: desired image width
  h: desired image height
  Examples
  --------
  from feature_util import DimTransformer
  DT = DimTransformer(w = 100, h = 100)
  resized_images = DT.transform(image_path)
  '''
  def __init__(self, w=100, h=100):
    self.w = w
    self.h = h

  def fit(self, x, y = None):
    return self

  def transform(self, image_paths):
    ''' Read image from image path and return as size self.w by self.h
    Parameters
    ----------
    image_paths: list of path to a valid images
    Returns
    -------
    resized_images: list of image array with width self.w and heigth self.h
    '''
    if type(image_paths) == type('s'): 
      ## if image_paths is a string, assume its a single item list
      image_paths = [image_paths]
    
    resized_images = []
    for image_path in image_paths:
      im = cv2.imread(image_path)
      resized_im = cv2.resize(im, (self.w, self.h))
      resized_images.append(resized_im)
    
    return resized_images
