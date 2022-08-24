import os
import numpy as np
from PIL import Image, ImageDraw
from matplotlib import pyplot as plt

# 各種画像の変換
# https://qiita.com/mo256man/items/8912934578025adb5ce5

IMAGES_DIR = os.path.join(os.getcwd(), "images")
IMAGE_FILE_NAME = "space.jpg"

image_file_path = os.path.join(IMAGES_DIR, IMAGE_FILE_NAME)

# PILで画像読み込み
pil_image = Image.open(image_file_path)
print(type(pil_image))  # <class 'PIL.JpegImagePlugin.JpegImageFile'>

# 画像描画の準備
drawer = ImageDraw.Draw(pil_image)

# 矩形の描画
x_min, y_min, x_max, y_max = 100, 50, 300, 200
drawer.rectangle(
    ((x_min, y_min), (x_max, y_max)),
    outline=(255, 0, 0)
)

# 文字の描画
drawer.text(
    (x_min, y_min - 10), "abcABC", (32, 196, 72)
)

# numpy型に変換
np_image = np.asarray(pil_image)
print(type(np_image))  # <class 'numpy.ndarray'>

# 画像表示
plt.imshow(np_image)
plt.show()
