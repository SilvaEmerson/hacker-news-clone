from channels.generic.websocket import WebsocketConsumer
import json


class PostConsumer(WebsocketConsumer):
    def connect(self):
        self.author_name = self.scope["url_route"]["kwargs"]["author"]
        print(self.scope)
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        self.send(text_data=json.dumps({"message": message}))


class WriterConsumer(WebsocketConsumer):
    def connect(self):
        self.author_name = self.scope["url_route"]["kwargs"]
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        self.send(text_data=json.dumps({"message": message}))
