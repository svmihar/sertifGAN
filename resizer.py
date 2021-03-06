from PIL import Image, ImageCms
import logging
from tqdm import tqdm
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(name)s -   %(message)s",
    datefmt="%m/%d/%Y %H:%M:%S",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

images = [str(a) for a in Path("./images/sertifikat").iterdir()]
output_path = Path("./images/resized")
output_path.mkdir(parents=True, exist_ok=True)

R = 512
image_bermasalah = []


def resize(img, size=(R, R)):
    new = img.resize(size, Image.ANTIALIAS)
    return new


def convert_to_srgb(img):
    """convert pil image to plain old jpg no transparency"""
    rgb = img.convert("RGB")
    return rgb


def convert(img):
    try:
        image = Image.open(img)
        new = convert_to_srgb(image)
        new = resize(new)
        new.save("./images/resized/" + img.split("/")[-1].lower())
        return img
    except Exception as e:
        logging.info(f"{a} bermasalah")
        logging.info(e)
        image_bermasalah.append(a)


def main():
    with ThreadPoolExecutor(max_workers=4) as mp:
        hasil = mp.map(convert, images)

    logging.info(f"total {len(image_bermasalah)} gambar bermasalah")
    logging.info("saving to bermasalah.txt now")
    with open("bermasalah.txt", "w") as f:
        for a in image_bermasalah:
            f.writelines(f"{a}\n")


if __name__ == "__main__":
    main()
