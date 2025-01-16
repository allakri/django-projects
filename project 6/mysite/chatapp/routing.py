# Import the required modules
from django.urls import path  # Import path function to define URL patterns
from . import consumers  # Import the consumers module where WebSocket consumers are defined

# Define the WebSocket URL patterns
websocket_urlpatterns = [
    # Define a WebSocket route (URL pattern) that takes a room_name as a string parameter
    # The URL will match any URL like /ws/<room_name>/, where <room_name> is the name of the chat room
    path('ws/<str:room_name>/', consumers.ChatConsumer.as_asgi()),
    # The above URL pattern will be matched when the WebSocket client connects with a URL like:
    # ws/example_room/ or ws/room_name/
]
