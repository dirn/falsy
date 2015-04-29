"""Check for falsy values."""

_FALSY_VALUES = {'false', 'f', 'no', 'n', 'none', 'null', 'nil'}


def is_(value):
    """Return True when a value is falsy.

    Args:
        value: The value to check.

    Returns:
        bool: True when the value is falsy.
    """
    if not value:
        # If the value evaluates to false, get out early.
        return True

    if hasattr(value, 'lower'):
        value = value.lower()

    return value in _FALSY_VALUES
