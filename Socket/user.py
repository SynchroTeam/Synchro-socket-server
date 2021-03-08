from channels.generic.websocket import AsyncWebsocketConsumer
import json
from time import sleep
from random import randint

class WSUser(AsyncWebsocketConsumer):

    async def connect(self):

        self.room_name = self.scope['url_route']['kwargs']['uri']
        self.USER_JWT = self.scope['url_route']['kwargs']['ua']
        self.BLUEPRINT = self.scope['url_route']['kwargs']['b']


        self.room_group_name = 'chat_%s' % self.room_name
        

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        
        await self.accept()

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chatroom_message',
                'message': {},
                'username': {},
            }
        )


    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        
        #text_data_json = json.loads(text_data)
        
        #message = text_data_json['message']
        #username = text_data_json['username']

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chatroom_message',
                'message': text_data,
                'username': "username",
            }
        )

    async def chatroom_message(self, event):
        message = event['message']
        username = event['username']

        await self.send(text_data=json.dumps({
            'message': message,
            'username': username,
        }))

    pass