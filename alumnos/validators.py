from django.core.exceptions import ValidationError

def validate_email(value):
    if not "gmail.com" or not "hotmail.com" or not "yahoo.com" or not "outlook.com"in value:
        raise ValidationError("A valid email must be entered in")
    else:
        return value