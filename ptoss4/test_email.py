import pytest
from email_tester import valid_email, email_in_database, reset_password


def test_valid_email():
    email = 'brunna.louisemr@gmail.com'
    response = valid_email(email)
    assert response == 'valid email address'


def test_email_in_database():
    email = 'brunna.louisemr@outlook.com'
    if valid_email(email) == 'valid email address':
        response = email_in_database(email)
        assert response == 'email address was found in database'
    
def test_email_sent_successfully():
    email = 'pedroinjustice@gmail.com'
    if valid_email(email) == 'valid email address':
        if email_in_database(email) == 'email address was found in database':
            response = reset_password(email)
            assert response == 'email was sent successfully'

