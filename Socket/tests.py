from django.test import RequestFactory, TestCase
from channels.testing import WebsocketCommunicator
from .user import WSUser

class WSUserConnectTest(TestCase):

    async def test_details(self):

        # Payload
        ID_CHANNEL = 55
        JWT_USER = 'hdugyy4'
        BLUEPRINT = '23423432'

        communicator = WebsocketCommunicator(WSUser.as_asgi(), f"/ws/some_url/{ID_CHANNEL}/{JWT_USER}/{BLUEPRINT}/")
        connected, subprotocol = await communicator.connect()
        assert connected
        # Test sending text
        # await communicator.send_to(text_data="hello")
        response = await communicator.receive_from()
        assert response == '{"message": "nice"}'
        # Close
        await communicator.disconnect()