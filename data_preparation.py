import glob
import os
import random
from PIL import Image

#уменьшение размера картинок, у которых ширина < 1200
def scale_image(input_image_path,
                output_image_path,
                width=None,
                height=None
                ):
    original_image = Image.open(input_image_path)
    w, h = original_image.size
    print('The original image size is {wide} wide x {height} '
          'high'.format(wide=w, height=h))
    if w <= 1200:
        original_image.save(output_image_path)
    else:
        if width and height:
            max_size = (width, height)
        elif width:
            max_size = (width, h)
        elif height:
            max_size = (w, height)
        else:
            # No width or height specified
            raise RuntimeError('Width or height required!')

        original_image.thumbnail(max_size, Image.ANTIALIAS)
        original_image.save(output_image_path)

        scaled_image = Image.open(output_image_path)
        width, height = scaled_image.size
        print('The scaled image size is {wide} wide x {height} '
              'high'.format(wide=width, height=height))

#перенесение картинок
def file_remover (dir_from, dir_to, count):
    for i in range(count):
        file_name = random.choice(os.listdir(dir_from))
        os.replace(dir_from + '\\' + file_name, dir_to + '\\' + file_name)
        i += 1

        file_list_benign = glob.glob("isic_benign_train/*.jpg")
        for file in file_list_benign:
            file_changed = file[:-16] + 'ben_' + file[-16:]
            scale_image(input_image_path=file, output_image_path=file_changed, width=1024)

        file_list_malignant = glob.glob("isic_malignant_train/*.jpg")
        for file in file_list_malignant:
            file_changed = file[:-16] + 'mal_' + file[-16:]
            scale_image(input_image_path=file, output_image_path=file_changed, width=1024)
