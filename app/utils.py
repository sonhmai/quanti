from webargs import fields
from webargs.flaskparser import FlaskParser


class CustomFlaskParser(FlaskParser):
    """Change default code 422 to 400 for validation error. Less stuff to remember."""
    DEFAULT_VALIDATION_STATUS = 400


parser = CustomFlaskParser()
use_args = parser.use_args


class IntOrFloat(fields.Number):
    """ We need to have both types int/ float, not forcing the whole list to be
    either int or float. Webargs only supply class for converting all elements
    of a list to either int or float.
    """
    def _format_num(self, value):
        if isinstance(value, int) or isinstance(value, float):
            return value
        try:
            return int(value)
        except ValueError:
            return float(value)
