#  Copyright (C) 2017
#      Jakub Krajniak (jkrajniak at gmail.com)
#
#  This file is part of instapp.
#
#  instapp is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  instapp is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.


# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types
from google.protobuf.json_format import MessageToJson


def handle_image(image):
    """Gets the features of the image from Google Vision and return JSON data

    Args:
        image: The models.Image object.

    Returns:
        The JSON string from Google Vision service.
    """
    client = vision.ImageAnnotatorClient()
    image.image.open()
    content = image.image.read()
    gcv_image = types.Image(content=content)
    request = {
        'image': {
            'content': gcv_image.content
        }
    }
    response = client.annotate_image(request)
    jsonObj = MessageToJson(response)
    return jsonObj