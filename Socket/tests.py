from django.test import RequestFactory, TestCase
from channels.testing import WebsocketCommunicator
from .user import WSUser

class WSUserConnectTest(TestCase):

    async def test_details(self):

        communicator = WebsocketCommunicator(WSUser.as_asgi(), "/ws/some_url/")
        connected, subprotocol = await communicator.connect()
        assert connected
        # Test sending text
        # await communicator.send_to(text_data="hello")
        response = await communicator.receive_from()
        assert response == '{"message": "nice"}'
        # Close
        await communicator.disconnect()