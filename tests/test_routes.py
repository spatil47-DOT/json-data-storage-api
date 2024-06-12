"""
Author- Suraj Prakash Patil
Date- 11/06/2024

"""

import unittest
from app import create_app, db
from app.models import Data

class RoutesTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app.config['TESTING'] = True
        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.drop_all()

    def test_create_data(self):
        response = self.client.post('/data', json={'key': 'value'}, headers={'Authorization': 'Basic YWRtaW46c2VjcmV0'})
        self.assertEqual(response.status_code, 201)
        self.assertIn('id', response.get_json())

    def test_get_data(self):
        with self.app.app_context():
            data = Data(content={'key': 'value'})
            db.session.add(data)
            db.session.commit()
            data_id = data.id
        
        response = self.client.get(f'/data/{data_id}', headers={'Authorization': 'Basic YWRtaW46c2VjcmV0'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {'key': 'value'})

    def test_update_data(self):
        with self.app.app_context():
            data = Data(content={'key': 'value'})
            db.session.add(data)
            db.session.commit()
            data_id = data.id
        
        response = self.client.put(f'/data/{data_id}', json={'new_key': 'new_value'}, headers={'Authorization': 'Basic YWRtaW46c2VjcmV0'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {'message': 'Data updated'})

    def test_delete_data(self):
        with self.app.app_context():
            data = Data(content={'key': 'value'})
            db.session.add(data)
            db.session.commit()
            data_id = data.id
        
        response = self.client.delete(f'/data/{data_id}', headers={'Authorization': 'Basic YWRtaW46c2VjcmV0'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {'message': 'Data deleted'})

if __name__ == '__main__':
    unittest.main()
