import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


class PostConsumer(WebsocketConsumer):
    def connect(self):
        self.author_name = self.scope["url_route"]["kwargs"]["author"]
        print(self.channel_name)
        self.accept()
        async_to_sync(self.channel_layer.group_add)(
            self.author_name, self.channel_name
        )

    # message = json.dumps({'message': f'Listening to {self.author_name} new posts'})
    # self.send(text_data=message)

    def channel_message(self, event):
        message = event["message"]
        # Send message to WebSocket
        self.send(text_data=json.dumps({"message": message}))

    def disconnect(self, close_code):
        print(f"Close connection[Error code={close_code}]")
