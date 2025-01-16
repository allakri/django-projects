from channels.generic.websocket import AsyncWebsocketConsumer
import json
from asgiref.sync import sync_to_async
from django.contrib.auth.models import User
from .models import ChatRoom, ChatMessage

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Retrieve the room name from the URL route
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        
        # Add the user to the corresponding group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        
        # Accept the WebSocket connection
        await self.accept()
        
    async def disconnect(self, close_code):
        # Remove the user from the group when the WebSocket closes
        await self.channel_layer.group_discard(
            self.room_group_name,  # Use the room group name, not self.channel_layer
            self.channel_name
        )
        
    async def receive(self, text_data):
        # Parse the incoming message data
        data = json.loads(text_data)
        message = data['message']
        username = data['username']
        room = data['room']
        
        # Broadcast the message to the group
        await self.channel_layer.group_send(
            self.room_group_name, {
                'type': 'chat_message',
                'message': message,
                'username': username,
                'room': room,
            }
        )
        
        # Save the message to the database asynchronously
        await self.save_message(username, room, message)
    
    async def chat_message(self, event):
        # When a message is received from the group, send it to WebSocket clients
        message = event['message']
        username = event['username']
        room = event['room']
        
        # Send the message data back to the client (WebSocket)
        await self.send(text_data=json.dumps({
            'message': message,
            'username': username,
            'room': room,
        }))
    
    @sync_to_async
    def save_message(self, username, room, message):
        try:
            # Fetch the user and room from the database
            user = User.objects.get(username=username)
            room = ChatRoom.objects.get(slug=room)
            
            # Create and save the new message
            ChatMessage.objects.create(user=user, room=room, message_content=message)
        except User.DoesNotExist:
            pass  # Handle user not found scenario
        except ChatRoom.DoesNotExist:
            pass  # Handle room not found scenario
