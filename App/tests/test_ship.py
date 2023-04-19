import os, tempfile, pytest, logging, unittest
from werkzeug.security import check_password_hash, generate_password_hash

from App.main import create_app
from App.database import create_db
from App.models import Ship
from App.controllers import (
    create_ship,
    get_ship,
    get_all_ship_json,
    get_ship_by_name
)

from wsgi import app


LOGGER = logging.getLogger(__name__)

'''
   Unit Tests
'''
class InternshipUnitTests(unittest.TestCase):

    def test_new_ship(self):
        ship = Ship("first ship", "its first", "UWI","2022,10,5, 9:30", 30)
        assert ship.name == "first ship"

    # pure function no side effects or integrations called
    def test_get_json(self):
        ship = Ship("first ship", "its first", "UWI","2022,10,5, 9:30", 30)
        ship_json = ship.get_json()
        self.assertDictEqual(ship_json, {"id":None, "name":"first ship"})
    

'''
    Integration Tests
'''

# This fixture creates an empty database for the test and deletes it after the test
# scope="class" would execute the fixture once and resued for all methods in the class
@pytest.fixture(autouse=True, scope="module")
def empty_db():
    app.config.update({'TESTING': True, 'SQLALCHEMY_DATABASE_URI': 'sqlite:///test.db'})
    create_db(app)
    yield app.test_client()
    os.unlink(os.getcwd()+'/App/test.db')


class InternshipIntegrationTests(unittest.TestCase):

    def test_create_ship(self):
        ship = create_ship("first ship", "its first", "UWI","2022,10,5, 9:30", 30)
        assert ship.name == "first ship"

    def test_get_all_ship_json(self):
        ship_json = get_all_ship_json()
        self.assertListEqual([{"name":"first ship"}, {"description":"its first", "location":"UWI", "date/time":"2022,10,5, 9:30","Spots Remaning":30, "Enrolled":0}], ship_json)
    

