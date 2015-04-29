"""Test the falsy module."""

import pytest

import falsy


@pytest.mark.parametrize('value', [
    False,
    'false',
    'f',
    'no',
    'n',
    'none',
    'null',
    'nil',
])
def test_falsy(value):
    """Test is_ with falsy values."""
    assert falsy.is_(value)


@pytest.mark.parametrize('value', [
    True,
])
def test_truthy(value):
    """Test is_ with truthy values."""
    assert not falsy.is_(value)
