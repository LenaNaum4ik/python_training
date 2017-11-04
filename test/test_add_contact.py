# -*- coding: utf-8 -*-
import pytest

from fixture.application import Application
from model.contact import Contact


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
     app.session.login(username="admin", password="secret")
     app.create_contact(Contact(firstname="11111",middlename= "2222", lastname="33333", nickname="444444", title="5555", company="666", address="777777", home="88888888888",
                           mobile= "9999999999", work="wwwwwwwww", fax="rrrrrrrrr", email="gggggggg", email2="hhhhhhhhhhh", email3="nnnnnnnnnnn",
                           homepage= "ccccccccccc", byear="1234", ayear="3214", address2="fffffffff", phone2="fffffffffff", notes="ffffffff"))
     app.session.logout()


def test_add_empty_contact(app):
     app.session.login(username="admin", password="secret")
     app.create_contact(Contact(firstname="",middlename= "", lastname="", nickname="", title="", company="", address="", home="",
                           mobile= "", work="", fax="", email="", email2="", email3="",
                           homepage= "", byear="", ayear="", address2="", phone2="", notes=""))
     app.session.logout()

