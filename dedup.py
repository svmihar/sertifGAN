from PIL import Image
import imagehash
from collections import ChainMap
from pathlib import Path
from joblib import dump, load
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm
from itertools import combinations

"""
def hasher(image_path): 
    img = Image.open(image_path)
    img_hash = imagehash.phash(img)
    return {'image':str(image_path), 'hash': img_hash}

with ThreadPoolExecutor(max_workers=20) as sp: 
    result = sp.map(hasher, images)

ha = []
for a in result: 
    try: 
        ha.append(a)
    except: 
        pass

breakpoint()
dump(ha, 'sertif_hashes.pkl')
breakpoint()
"""
images = [str(a) for a in Path("./images").iterdir()]
images_hash = load("sertif_sama_fix.pkl")
hasil = {}
for img in images_hash:
    hasil.update(img)


def persamaan(comb):
    img1, img2 = comb
    score = hasil[img1] - hasil[img2]
    return score


gambar_sama = []
for comb in combinations(images, 2):
    score = persamaan(comb)
    if score < 2:
        gambar_sama.append((comb, score))


dump(gambar_sama, "image_sama1.pkl")
