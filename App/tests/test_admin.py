import os, tempfile, pytest, logging, unittest
from werkzeug.security import check_password_hash, generate_password_hash

from App.main import create_app
from App.database import create_db
from App.models import InternAdmin
from App.controllers import (
    create_admin,
    get_all_admins_json,
    authenticate,
    get_admin,
    get_admin_by_username,
    get_admin_by_name,
    update_admin
)

from wsgi import app


LOGGER = logging.getLogger(__name__)

'''
   Unit Tests
'''
class InternAdminUnitTests(unittest.TestCase):

    def test_new_admin(self):
        admin = InternAdmin("bob", "bobpass", "bobby")
        assert admin.username == "bob"

    # pure function no side effects or integrations called
    def test_get_json(self):
        admin = InternAdmin("bob", "bobpass", "bobby")
        admin_json = admin.get_json()
        self.assertDictEqual(admin_json, {"id":None, "adminname":"bob"})
    
    def test_hashed_password(self):
        password = "mypass"
        hashed = generate_password_hash(password, method='sha256')
        admin = InternAdmin("bob", password)
        assert admin.password != password

    def test_check_password(self):
        password = "mypass"
        admin = InternAdmin("bob", password)
        assert admin.check_password(password)

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


def test_authenticate():
    admin = create_admin("bob", "bobpass", "bobby")
    assert authenticate("bob", "bobpass") != None

class InternAdminsIntegrationTests(unittest.TestCase):

    def test_create_admin(self):
        admin = create_admin("rick", "bobpass", "rick")
        assert admin.username == "rick"

    def test_get_all_admin_json(self):
        admin_json = get_all_admin_json()
        self.assertListEqual([{"id":1, "username":"bob"}, {"id":2, "username":"rick"}], admin_json)

    # Tests data changes in the database
    def test_update_admin(self):
        update_admin(1, "ronnie")
        admin = get_admin(1)
        assert admin.username == "ronnie"
