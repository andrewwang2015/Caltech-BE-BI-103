import glob
import os

import numpy as np
import pandas as pd
import scipy.signal

# Image processing tools
import skimage
import skimage.io

import bebi103

import matplotlib.pyplot as plt
import seaborn as sns
rc={'lines.linewidth': 2, 'axes.labelsize': 14, 'axes.titlesize': 14}
sns.set(rc=rc)


# Import Bokeh modules for interactive plotting
import bokeh
bokeh.io.output_notebook()

data_dir = '../data/iyer_biswas_et_al/'


# Glob string for images
im_glob = data_dir + "bacterium_1.tif"

ic = skimage.io.ImageCollection(im_glob, conserve_memory=True)

im = ic[0] / ic[0].max()

#im = im[:,:,0]

skimage.io.imshow(im);

verts = plt.ginput(4)
print (verts)