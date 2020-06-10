from PIL import Image
from tqdm import tqdm
from pathlib import Path

images = [str(a) for a in Path('./images').iterdir()]

R = 512

for img in tqdm(images):
    try:
        im = Image.open(img)
        new = im.resize((R,R), Image.ANTIALIAS)
        new.save(img.split('/')[-1].lower())
    except Exception as e:
        print(img)
        print(e)
        pass

