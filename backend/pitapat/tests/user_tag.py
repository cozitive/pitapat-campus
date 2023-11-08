import json
from django.test import TestCase, Client
from pitapat.testutils.setup import setup
from ..models import User, Tag, UserTag


class UserTagTestCase(TestCase):
    def setUp(self):
        setup()
        Tag.objects.create(name='soccer', type='SPORT').save()

    def test_user_tag(self):
        client = Client()
        user_id = User.objects.get(nickname='a').id
        tag = Tag.objects.get(name='soccer')
        tags = [tag.id]

        self.assertEqual(str(tag), tag.name)

        response = client.post(f'/api/user/{user_id}/tag/',
                               json.dumps({'tags': tags}),
                               content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(str(UserTag.objects.get(tag=tag)), f'user {user_id} - tag {tag.id}')

        response = client.delete(f'/api/user/{user_id}/tag/',
                               json.dumps({'tags': tags}),
                               content_type='application/json')
        self.assertEqual(response.status_code, 204)
