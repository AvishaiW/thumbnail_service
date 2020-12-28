from io import BytesIO

import requests
from PIL import Image, ImageOps
from flask import send_file

from .errors import InputsError, FormatError


class MyImage(object):
    """
    holds an image with it's dimensions
    """
    def __init__(self, url=None, image=None):
        if url:
            response = requests.get(url)
        try:
            self.image = image or Image.open(BytesIO(response.content))
        except Exception:
            raise InputsError("The url must be a valid url of a JPEG image")

        self.width = self.image.width
        self.height = self.image.height

    def new_proportions(self, w, h):
        """
        returns an Image which fits the given dimensions
        maintaining the same aspect ratio as of the original image.
        calculations were made based on this: https://math.stackexchange.com/a/1620375

        :param w: int; the target width of the final image
        :param h: int; the target height of the final image
        :return: MyImage object; the Image with the correct
                    proportions to fit in the new dimensions
        """
        horiz_scale = w / self.width
        vert_scale = h / self.height
        scale = min(horiz_scale, vert_scale)
        new_height, new_width = int(scale * self.height), int(scale * self.width)
        # if the calculation concludes that the original image scales up,
        # we continue with the original size, due to the requirements of the project.
        if scale >= 1:
            return self
        else:
            new_image = self.image.resize((new_width, new_height))
            return self.__class__(image=new_image)

    def pad_image(self, target_width, target_height):
        """
        padding of the image resulting in an image in the target dimensions
        :param target_width: int; the target width of the final image
        :param target_height: int; the target height of the final image
        :return: PIL.Image
        """
        if (target_width, target_height) == (self.width, self.height):
            return self

        horiz_pad = (target_width - self.width) // 2
        vertical_pad = (target_height - self.height) // 2
        padding = (horiz_pad, vertical_pad, horiz_pad, vertical_pad)

        return self.__class__(image=ImageOps.expand(self.image, padding))

    def serve_pil_image(self):
        img_io = BytesIO()
        self.image.save(img_io, 'JPEG')
        img_io.seek(0)
        return send_file(img_io, mimetype='image/jpeg')
