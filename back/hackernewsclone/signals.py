from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer


def send_channel_message(group_name, message):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        f"{group_name}", {"type": "channel_message", "message": message}
    )
