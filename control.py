import socket

HOST_ESP32 = '178.176.46.90' #esp_32
PORT_ESP32 = 20001
ADDR_ESP32 = (HOST_ESP32, PORT_ESP32)

class ControlCar():
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.client.connect(ADDR_ESP32)

        self.old_servo = -1
        self.old_speed = -1
        self.speed = 0
        self.servo = 7.5

        self.previous_keys = set()

    def control_car(self, keys):
        if "w" in keys and "s" in keys:
            self.speed = 0
        elif "w" in keys:
            if "s" in self.previous_keys:
                self.speed = 0
            else:
                self.speed = 100
        elif "s" in keys:
            if "w" in self.previous_keys:
                self.speed = "b"
            else:
                self.speed = -100

        if "a" in keys and "d" in keys:
            self.servo = 7.5
        elif "a" in keys:
            if "d" in self.previous_keys:
                self.servo = 7.5
            else:
                self.servo = 11
        elif "d" in keys:
            if "a" in self.previous_keys:
                self.servo = 7.5
            else:
                self.servo = 5

        if self.old_servo != self.servo:
            msg = f"s={self.servo}"
            message = msg.encode("utf-8")
            self.client.send(message)
            print(msg)
            self.old_servo = self.servo
            
        if self.old_speed != self.speed:
            msg = f"m={self.speed}"
            message = msg.encode("utf-8")
            self.client.send(message)
            print(msg)
            self.old_speed = self.speed