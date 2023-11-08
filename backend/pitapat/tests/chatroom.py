from datetime import date
from django.test import TestCase, Client
from pitapat.testutils.setup import setup
from ..models import Chat, Chatroom, User


class ChatroomTestCase(TestCase):
    def setUp(self):
        setup()

    def test_chatroom(self):
        client = Client()
        user = User.objects.get(nickname='a')
        chatroom = Chatroom.objects.create(user_count=1)
        chat = Chat.objects.create(chatroom=chatroom, author=user, content='hi',
                                   reg_dt=date.today(), upd_dt=date.today())
        self.assertEqual(str(chatroom), f'chatroom {chatroom.id}')
        self.assertEqual(str(chat), f'{user.nickname}: {chat.content}')
        response = client.get(f'/api/chatroom/{user.id}/user/')
        self.assertEqual(response.status_code, 200)
