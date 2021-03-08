from channels.generic.websocket import WebsocketConsumer
import json
from time import sleep
from random import randint

class WSUser(WebsocketConsumer):
    def connect(self):
        print('hwllow')
        self.accept()

        for i in range(100):
           self.send(json.dumps({'message': 'nice'}));
          