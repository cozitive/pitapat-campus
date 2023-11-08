import json
from django.test import TestCase, Client
from pitapat.testutils.setup import setup
from ..models import User



class PitapatTestCase(TestCase):
    def setUp(self):
        setup()

    def test_pitapat_create(self):
        client = Client()
        from_id = User.objects.get(nickname='a').id
        to_id = User.objects.get(nickname='b').id

        response = client.post('/api/pitapat/')
        self.assertEqual(response.status_code, 400)

        response = client.post('/api/pitapat/',
                               json.dumps({'from': from_id, 'to': to_id}),
                               content_type='application/json')
        self.assertEqual(response.status_code, 201)

        response = client.post('/api/pitapat/',
                                json.dumps({'from': from_id, 'to': to_id}),
                                content_type='application/json')
        self.assertEqual(response.status_code, 409)

        response = client.post('/api/pitapat/',
                                json.dumps({'from': to_id, 'to': from_id}),
                                content_type='application/json')
        self.assertEqual(response.status_code, 205)

    def test_pitapat_delete(self):
        client = Client()
        from_id = User.objects.get(nickname='a').id
        to_id = User.objects.get(nickname='b').id

        response = client.delete('/api/pitapat/')
        self.assertEqual(response.status_code, 400)

        response = client.delete('/api/pitapat/',
                               json.dumps({'from': from_id, 'to': to_id}),
                               content_type='application/json')
        self.assertEqual(response.status_code, 404)

        response = client.post('/api/pitapat/',
                                json.dumps({'from': from_id, 'to': to_id}),
                                content_type='application/json')
        response = client.delete('/api/pitapat/',
                               json.dumps({'from': from_id, 'to': to_id}),
                               content_type='application/json')
        self.assertEqual(response.status_code, 204)
