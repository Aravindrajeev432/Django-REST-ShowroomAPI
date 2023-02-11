
#
# from frontdesk.models import CarEnquires
# from .serializers import CarEnquiresSerializer
# class RequestConsumer(ListModelMixin, GenericAsyncAPIConsumer,):
#     queryset = CarEnquires.objects.all()
#     serializer_class = CarEnquiresSerializer
#
#


import json

from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async

from frontdesk.models import CarEnquiresmodel


class RequestConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.room_group_name = 'enqgroup'
        await(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        print("connect")
        # token = self.scope['headers'][b'authorization'].decode().split(' ')[1]
        # print(token)
        await self.accept()
        # await self.send(text_data=json.dumps({"message": "hello this is my first meassaeg"}))

    async def enq_message(self, event):
        print("enq_message")
        message = event['message']
        await self.send(text_data=json.dumps({
            'type': 'get-enq',
            'message': message
        }))

    @database_sync_to_async
    def get_enqs(self):
        return CarEnquiresmodel.objects.all()

    async def disconnect(self, close_code):
        print("disconnect")
        pass
