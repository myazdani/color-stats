import numpy as np
import cv2
from HSVHistTransformer import *
from sklearn.decomposition import RandomizedPCA
import pandas as pd


def HSV_hists(image_paths, Hue_bins = 180, Sat_bins = 256, Val_bins = 256):
  HueHist = HSVHistTransformer(hist_type = "hue", num_bins = Hue_bins)
  SatHist = HSVHistTransformer(hist_type = "sat", num_bins = Sat_bins)
  ValHist = HSVHistTransformer(hist_type = "val", num_bins = Val_bins)

  hues = HueHist.transform(image_paths) + 1
  sats = SatHist.transform(image_paths) + 1
  vals = ValHist.transform(image_paths) + 1

  return hues, sats, vals

def HSV_PCA(image_paths, Hue_bins = 180, Sat_bins = 256, Val_bins = 256):

  hsv_hists = HSV_hists(image_paths, Hue_bins, Sat_bins, Val_bins)

  pca = RandomizedPCA(n_components=3)

  hue_pca = pca.fit_transform(np.log(hsv_hists[0]))
  sat_pca = pca.fit_transform(np.log(hsv_hists[1]))
  val_pca = pca.fit_transform(np.log(hsv_hists[2]))

  hsv_df = pd.DataFrame(data = np.hstack((hue_pca, sat_pca, val_pca)))
  h_cols = ["HuePC" + str(i) for i in range(1,4)]
  s_cols = ["SatPC" + str(i) for i in range(1,4)]
  v_cols = ["ValPC" + str(i) for i in range(1,4)]
  hsv_df.columns = h_cols + s_cols + v_cols

  df_res = pd.concat([pd.DataFrame({'image_paths': image_paths}), hsv_df], axis = 1)

  return df_res