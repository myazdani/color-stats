import numpy as np
from skimage.feature import hog
from sklearn.base import BaseEstimator, TransformerMixin
from scipy.stats import entropy
import cv2
import colorsys
import pandas as pd

def avgHSV(image_paths):
  avg_HSV = []
  for image_path in image_paths:
    image = cv2.imread(image_path)
    rgb = np.mean(np.mean(image, axis = 0), axis = 0)    
    avg_HSV.append(colorsys.rgb_to_hsv(rgb[0], rgb[1], rgb[2]))

  res = np.array(avg_HSV)

  d = {'image_paths': image_paths, 'H.avg': res[:,0], 'S.avg': res[:,1], 'V.avg': res[:,2]}

  df = pd.DataFrame(d, columns = ['image_paths', 'H.avg', 'S.avg', 'V.avg'])

  return df


def stdHSV(image_paths):
  std_HSV = []
  for image_path in image_paths:
    image = cv2.imread(image_path)
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    hsv_std = np.std(np.std(hsv, axis = 0), axis = 0)    
    std_HSV.append(hsv_std)

  res = np.array(std_HSV)

  d = {'image_paths': image_paths, 'H.std': res[:,0], 'S.std': res[:,1], 'V.std': res[:,2]}

  df = pd.DataFrame(d, columns = ['image_paths', 'H.std', 'S.std', 'V.std'])

  return df


def HSV_stats(image_paths):
  df_avg = avgHSV(image_paths)
  df_std = stdHSV(image_paths)

  df_res = pd.concat([df_avg, df_std.iloc[:,1:]], axis = 1)

  return df_res