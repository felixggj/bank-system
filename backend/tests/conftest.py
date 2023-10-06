import pytest
from iebank_api.models import Account
from iebank_api import db, app

@pytest.fixture(scope='module')
def testing_client():
    # Push an application context to the context stack
    app_context = app.app_context()
    app_context.push()

    db.create_all()
    account = Account('Test Account', '€')
    db.session.add(account)
    db.session.commit()

    with app.test_client() as testing_client:
        yield testing_client

    db.drop_all()
    # Pop the application context from the context stack
    app_context.pop()
