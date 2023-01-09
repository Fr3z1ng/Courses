from django.core.exceptions import ValidationError
import re


def validate_login(value):
    if not re.match(r'[0-9a-zA-Z]{6,10}$', value):
        raise ValidationError(
            ('%(value)s less at 6 characters'),
            params={'value': value},
        )


def validate_email(value):
    if not re.match(r'^[\w.-]+@[\w.-]+\.(\S{2}$)', value):
        raise ValidationError(
            ('%(value)s incorrectly entered data'),
            params={'value': value},
        )
