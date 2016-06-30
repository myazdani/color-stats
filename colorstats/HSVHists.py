import numpy as np
import cv2
from HSVHistTransformer import *
from sklearn.decomposition import RandomizedPCA
import pandas as pd


def HSV_hist(image_paths, hue_bins = 180, sat_bins = 256, val_bins = 256):

  hsv_hists = HSV_hists(image_paths,hue_bins, sat_bins, val_bins)


  hsv_df = pd.DataFrame(data = np.hstack((hsv_hists[0], hsv_hists[1], hsv_hists[2])))
  h_cols = ["Hue" + str(i) for i in range(hue_bins)]
  s_cols = ["Sat" + str(i) for i in range(sat_bins)]
  v_cols = ["Val" + str(i) for i in range(val_bins)]  
  hsv_df.columns = h_cols + s_cols + v_cols

  df_res = pd.concat([pd.DataFrame({'image_paths': image_paths}), hsv_df], axis = 1)

  return df_res