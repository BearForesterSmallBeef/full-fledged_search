import sys
from io import BytesIO

import requests
from PIL import Image
import pprint

from GetDelta import get_param


toponym_to_find = " ".join(sys.argv[1:])

params = get_param(toponym_to_find)

if params == 0:
    print("Ничего не найдено")
    sys.exit()
else:
    toponym_longitude, toponym_lattitude, delta = params

map_params = {
    "ll": ",".join([toponym_longitude, toponym_lattitude]),
    "spn": delta,
    "l": "sat",
    "pt": f"{','.join([toponym_longitude, toponym_lattitude])},pm2dgl"
}

map_api_server = "http://static-maps.yandex.ru/1.x/"
response = requests.get(map_api_server, params=map_params)

Image.open(BytesIO(
    response.content)).show()