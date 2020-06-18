"""
THIS IS A BASE MODEL TO FIND OUT THE BAD IMAGES ON THE TRAINING PROCESS
"""

from fastai.vision import *
import pandas as pd
from sklearn.model_selection import train_test_split

tfms = get_transforms(flip_vert=True)

classes = ['sertifikat', 'nope']
dataset_path = Path('.')
df = pd.read_csv(dataset_path/'labels.csv')
train, test = train_test_split(df, test_size=.2)

data = ImageDataBunch.from_df(dataset_path,df = df, ds_tfms=tfms, size=128, bs=12).normalize(imagenet_stats)
learn = cnn_learner(data, models.resnet34, metrics=error_rate)