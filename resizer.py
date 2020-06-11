from PIL import Image, ImageCms
from tqdm import tqdm
from pathlib import Path

images = [str(a) for a in Path('./images/resized').iterdir()]

R = 512

def resize(img, size=(R,R)): 
    new = im.resize(size, Image.ANTIALIAS)
    return new


def convert_to_srgb(img):
    '''convert pil image to plain old jpg no transparency'''
    rgb = img.convert('RGB')
    return rgb

for img in tqdm(images):
    try:
        im = Image.open(img)
        new = convert_to_srgb(im)
        new.save('./images/resized_rgb/'+img.split('/')[-1].lower())
    except Exception as e:
        print(img)
        print(e)
        pass


