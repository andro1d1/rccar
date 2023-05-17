import asyncio
import sys
from PySide6.QtWidgets import QApplication
import cam
import gps
import os
import requests

async def get_coords():
    while True:
        try:
            request = "http://192.168.10.101:5000/gps"
            response = requests.get(request).json()
            yield response["coordinates"]["latitude"], response["coordinates"]["longitude"]
            await asyncio.sleep(1)
        except:
            pass

async def main():
    app = QApplication(sys.argv)
    window = cam.Widgets()
    window.showFullScreen()
    mp = gps.MapParams()
    mp.load_map()
    window.update_additional_widget(os.getcwd()+"\map.png")
    coords_generator = get_coords()
    while True:
        try:
            latitude, longitude = await coords_generator.__anext_
            if (latitude != 0) & (longitude != 0):
                mp.set_coords(latitude, longitude)
                mp.load_map()
                window.update_additional_widget(os.getcwd()+"\map.png")
                os.remove(os.getcwd()+r"\map.png")
        except:
            pass
        finally:
            app.processEvents()


if __name__ == '__main__':
    asyncio.run(main())