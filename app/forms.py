from flask.ext.wtf import Form
from wtforms import TextField, PasswordField, ValidationError
from wtforms.validators import Required, Email, Length, Regexp, EqualTo
from app.utils.extensions import get_extension


class UniqueUser(object):
    def __init__(self, message="User exists"):
        self.message = message

    def __call__(self, form, field):
        if get_extension('security').datastore.find_user(email=field.data):
            raise ValidationError(self.message)

validators = {
    'email': [
        Required(),
        Email('This is not a valid email address.'),
        UniqueUser(message='Email address is associated '
                   'with an existing account.'),
    ],
    'password': [
        Required(),
        Length(min=8, max=100),
        EqualTo('confirm', message='Passwords must match'),
        Regexp(r'^[A-Za-z0-9@#$%^&+=]*$',
               message='Password contains invalid characters')
    ],
    'fullname': [
        Required(),
        Length(min=1, max=50),
        Regexp(r'^[A-Za-z0-9 ]*$',
               message="Full name can only contain alphanumeric characters")
        ],

}


class RegisterForm(Form):
    fullname = TextField('Full Name', validators['fullname'])
    email = TextField('Email', validators['email'])
    password = PasswordField('Password', validators['password'], )
    confirm = PasswordField('Confirm Password')
