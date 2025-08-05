import pytest
from py_app.domain.foo import bar


def test_bar():
    assert bar() == "bar"
