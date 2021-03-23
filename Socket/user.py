from channels.generic.websocket import AsyncWebsocketConsumer
import json

class WSUser(AsyncWebsocketConsumer):

    async def connect(self):

        self.room_name = self.scope['url_route']['kwargs']['ID']
        self.USER_JWT = self.scope['url_route']['kwargs']['USER_JWT']
        self.BLUEPRINT = self.scope['url_route']['kwargs']['BLUEPRINT']
        self.connection_id = self.scope['url_route']['kwargs']['connection_id']


        self.room_group_name = 'chat_%s' % self.room_name
        
        await self.accept()
        
        self.scope["session"]["USER_JWT"] = self.USER_JWT
        self.scope["session"]["connection_id"] = self.connection_id


        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        
        


    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chatroom_message',
                'message': text_data,
                'username': self.scope["session"]["USER_JWT"],
                'idConnection': self.scope["session"]["connection_id"]
            }
        )

    async def chatroom_message(self, event):
        message = event['message']
        username = event['username']
        idConnection = event['idConnection']

        await self.send(text_data=json.dumps({
            'message': message,
            'username': username,
            'idConnection': idConnection
        }))

    pass