from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
import json


class UserNotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        print(self.room_name)
        self.room_group_name = 'notification_%s' % self.room_name
        print(self.room_group_name)
        if self.room_name=='undefined':
            pass
        else:
            await self.channel_layer.group_add(
                self.room_group_name,
                self.channel_name
            )
            await self.accept()
            await self.send(text_data=json.dumps({"message": "hello this is my first message"}))


    async def notificator(self,event):
        message = event['message']
        await self.send(text_data=json.dumps({
            'type':'reloader',
            'message':message
        }))


    async def disconnect(self, close_code):
        print("disconnect")
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

