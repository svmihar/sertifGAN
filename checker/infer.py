from fastai.vision import *
import pandas as pd
from pathlib import Path
from tqdm import tqdm
import time
from concurrent.futures import ThreadPoolExecutor

model = load_learner("./models/")
raw_images_path = [a for a in Path("./dataset/").iterdir()]


def labeler(s):
    if s == "0":
        return "sertifikat"
    else:
        return "nope"


def oke(img):
    hasil = model.predict(open_image(str(img)))
    label = labeler(str(hasil[0]))
    score = max(hasil[-1].cpu().detach().numpy())
    return (str(img), label, score)


hasil_prediction = []
# with ThreadPoolExecutor(max_workers=4) as tpe:
#     hasil_prediction = tpe.map(oke, raw_images_path)

for img in tqdm(raw_images_path):
    hasil_prediction.append(oke(img))

df = pd.DataFrame(hasil_prediction)
df.columns = ["image", "pred_label", "score"]
df.to_csv("hasil.csv", index=False)
