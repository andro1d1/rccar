import sys
import requests

class MapParams:
    def __init__(self):
        self.lat, self.lon = 55.657116, 37.229969
        self.zoom = 16
        self.type = "map"
    
    def load_map(self):
        map_request = "http://static-maps.yandex.ru/1.x/?ll={ll}&z={z}&l={type}&pt={lon},{lat},round".format(ll=str(self.lon)+","+str(self.lat),lat=self.lat, lon=self.lon, z=self.zoom, type=self.type)
        response = requests.get(map_request)
        if not response:
            print("Ошибка выполнения запроса:")
            print(map_request)
            print("Http статус:", response.status_code, "(", response.reason, ")")
            sys.exit(1)
    
        map_file = "map.png"
        try:
            with open(map_file, "wb") as file:
                file.write(response.content)
        except IOError as ex:
            print("Ошибка записи временного файла:", ex)
            sys.exit(2)
        return map_file
    
    def set_coords(self, lat, lon):
        self.lat, self.lon = lat, lon