import pandas as pd
from fastai.vision import *
from fastai.metrics import error_rate
import torch

tfms = get_transforms(flip_vert=False, max_rotate=10)
defaults.device = torch.device("cuda")
df = pd.read_csv("cleaned.csv")
data = ImageDataBunch.from_df(Path("."), df=df, ds_tfms=tfms, size=256, bs=3).normalize(
    imagenet_stats
)
learn = cnn_learner(data, models.densenet201, metrics=error_rate)

learn.fit_one_cycle(4)
learn.save("sertifclf-stage1")
learn.load("sertifclf-stage1")

learn.unfreeze()

learn.lr_find()
learn.recorder.plot(suggestion=True)
mgr = learn.recorder.min_grad_lr
learn.fit_one_cycle(4, max_lr=slice(mgr / 10, mgr))
learn.save("sertifclf-stage2")
