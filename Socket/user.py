from channels.generic.websocket import WebsocketConsumer
import json
from time import sleep
from random import randint

class WSUser(WebsocketConsumer):
    def connect(self):


        self.ID_CHANNEL = self.scope['url_route']['kwargs']['uri']
        self.USER_JWT = self.scope['url_route']['kwargs']['ua']
        self.BLUEPRINT = self.scope['url_route']['kwargs']['b']

        print(self.ID_CHANNEL)

        self.accept()

        for i in range(100):
           self.send(json.dumps({'message': 'nice'}));
           sleep(1)
          