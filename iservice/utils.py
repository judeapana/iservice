import os
import secrets
from PIL import Image
from flask import current_app
from werkzeug.utils import secure_filename


def upload_image(file, file_mixin="", resize=(350, 350)):
    f = secure_filename(file.filename)
    enc_filename = f.split('.')[-1]
    file_name = f'{file_mixin}_{secrets.token_hex(10)}.{enc_filename}'
    path = os.path.join(current_app.root_path, f'static/images',
                        file_name)
    image = Image.open(file)
    image.thumbnail(resize)
    image.save(path)
    return file_name
