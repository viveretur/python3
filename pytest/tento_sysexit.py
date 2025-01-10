"""
viveretur : tento_sysexit.py
Ab https://docs.pytest.org/en/stable/getting-started.html
"""

import pytest


def f():
    """
    Explicat ipsum.
    """
    raise SystemExit(1)


def tento_tento_meus():
    """
    Explicat ipsum.
    """
    with pytest.raises(SystemExit):
        f()
