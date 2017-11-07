from model.contact import Contact

def test_change_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.change_first_contact(Contact(firstname="11111", middlename="2222", lastname="33333", nickname="444444", title="5555", company="666", address="777777", home="88888888888",
                                mobile= "9999999999", work="wwwwwwwww", fax="rrrrrrrrr", email="gggggggg", email2="hhhhhhhhhhh", email3="nnnnnnnnnnn",
                                homepage= "ccccccccccc", byear="1234", ayear="3214", address2="fffffffff", phone2="fffffffffff", notes="ffffffff"))
    app.session.logout()