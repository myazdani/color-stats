import numpy as np
from skimage.feature import hog
from sklearn.base import BaseEstimator, TransformerMixin
from scipy.stats import entropy
import cv2


class HSVHistTransformer(BaseEstimator, TransformerMixin):
  '''compute the HSV histogram of a list of images
  Parameters
  ----------
  hist_type: string that is either "hue", "sat", or "val" 
             (corresponding to HSV respectively)
  Returns
  -------
  numpy array of normalized histogram (should sum to 1)
  Examples
  from feature_util import HSVHistTransformer
  HueHist = HSVHistTransformer(hist_type = "hue")
  im = cv.imread(image_path)
  hue_hist = HueHist.transform(im)
  '''
  def __init__(self, hist_type = "hue", num_bins = 180):
    self.hist_type = hist_type
    self.num_bins = num_bins

  def fit(self, x, y=None):
    return self

  def transform(self, image_paths):
    '''Compute a normalized color histogram of an image
    Parameters
    ----------
    im: an image array
    Returns:
    --------
    normalized_hists: array of normalized color histograms
    '''
    if self.hist_type == "hue":
      num_bins = [self.num_bins]
      range_bins = [0,self.num_bins]
      channel = [0]
    if self.hist_type == "sat":
      num_bins = [self.num_bins]
      range_bins = [0,self.num_bins]
      channel = [1]
    if self.hist_type == "val":
      num_bins = [self.num_bins]
      range_bins = [0,self.num_bins]
      channel = [2]

    normalized_color_hists = []
    for image_path in image_paths:
      image = cv2.imread(image_path)
      color_hist = cv2.calcHist([image], channel, None, num_bins, range_bins)
      color_hist_normalized = color_hist/(1.0 + sum(color_hist))
      normalized_color_hists.append(np.squeeze(color_hist_normalized))

    self.mode = np.argmax(np.array(normalized_color_hists), axis = 1)
    self.entropy = entropy(np.array(normalized_color_hists).T)
    return np.array(normalized_color_hists)