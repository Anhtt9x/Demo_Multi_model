import matplotlib.pyplot as plt 
import os
from PIL import Image
from pathlib import Path

def plot_images(images_path):
    image_shown = 0
    plt.figure(figsize=(16,9))

    for img_path in images_path:
        if os.path.isfile(Path(img_path)):
            image = Image.open(img_path)

            plt.subplot(2,3,image_shown+1)
            plt.imshow(image)
            plt.axis('off')

            image_shown += 1 
            if image_shown >= 6:
                break
    plt.show()

if __name__ == "__main__":
    imgs_path = ['/home/tuananh/Demo_Multi_model/mixed_data/frame_0003.jpg', '/home/tuananh/Demo_Multi_model/mixed_data/frame_0038.jpg']
    plot_images(imgs_path)
