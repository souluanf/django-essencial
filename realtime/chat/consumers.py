from channels.generic.websocket import AsyncJsonWebsocketConsumer
import json


class ChatConsumer(AsyncJsonWebsocketConsumer):

    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['nome_sala']
        self.room_group_name = f'chat_{self.room_name}'

        # entrar na sala
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, code):
        # sair da sala

        await self.channel_layer.group_discard(
            self.room_group_name,
            self.room_name
        )

    # Recebe mensagem do WebSocket
    async def receive(self, text_data=None, bytes_data=None, **kwargs):
        text_data_json = json.loads(text_data)
        mensagem = text_data_json['mensagem']
        # envia mensagem

        await self.channel_layer.group_send(
            self.room_group_name, {
                'type': 'chat_message',
                'message': mensagem
            }
        )

    # Recebe mensagem da sala
    async def chat_message(self, event):
        mensagem = event['message']

        # envia a mensagem para o WebSocket

        await self.send(text_data=json.dumps({
            'mensagem': mensagem
        }))
