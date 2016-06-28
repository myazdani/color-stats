import numpy as np
from skimage.feature import hog
from sklearn.base import BaseEstimator, TransformerMixin
from ObjectDetector import ObjectRotateDetector
import cv2

class BWTransformer(BaseEstimator, TransformerMixin):
  '''Input list of image arrays and return list of equalized histogram grayscale images
  Parameters and Attributes
  ----------
  None
  Examples
  --------
  from feature_util import BWTransformer
  bw = BWTransformer()
  im = cv2.imread(image_path)
  image_bw = bw.transform(im)
  '''
  def fit(self, x, y = None):
    return self

  def transform(self, images):
    ''' Reutrn equalized grayscale image from image_path
    Parameters
    ----------
    images: list of image arrays
    Returns
    -------
    bw_images: list of images that are grayscaled with equalized histograms
    '''
    bw_images = []
    for image in images:
      imbw = cv2.equalizeHist(cv2.cvtColor(image, cv2.COLOR_BGR2GRAY))
      bw_images.append(imbw)

    return bw_images