from django import template
from datetime import datetime
from datetime import timezone

register = template.Library()

@register.filter
def convert_str_date(value):
    """
    It takes a string in ISO format and converts it to a string in the format of '%d %B, %Y %H:%M:%S'
    
    :param value: The value to be converted
    :return: A string
    """
    date = datetime.fromisoformat(value).astimezone(timezone.utc)
    return str(datetime.strftime(date, '%d %B, %Y %H:%M:%S'))


@register.filter
def convert_fahrenheit_to_celcious(value):
    """
    It takes a value in Fahrenheit and returns the equivalent value in Celsius
    
    :param value: The value to convert
    :return: the value of the calculation.
    """
    return  round((value - 32) * 5/9,)