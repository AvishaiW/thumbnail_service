from flask import Flask, request

from .my_image import MyImage
from .errors import InputsError

thumbnail_app = Flask(__name__)


@thumbnail_app.route('/thumbnail')
def get_request():
    try:
        url, width, height = check_params(request.args)
        img = MyImage(url=url)
        new_img = img.new_proportions(width, height)
        padded_img = new_img.pad_image(width, height)
        return padded_img.serve_pil_image()
    except Exception as e:
        return str(e), 400


def check_params(params):
    if len(params) != 3 or not all(x in params for x in ['url', 'width', 'height']):
        raise InputsError("Wrong parameters! Enter the url of your image and the target height & width only")
    try:
        url = params.get('url')
        height = int(params.get('height'))  # check if int larger than 0
        width = int(params.get('width'))  # check if int larger than zero
    except ValueError:
        raise ValueError("height and width must be numbers")
    if height <= 0 or width <= 0:
        raise InputsError("height and width must be positive numbers")

    return url, width, height


if __name__ == "__main__":
    thumbnail_app.run(host='0.0.0.0')
