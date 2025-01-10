"""
viveretur : tento_exceptiongroup.py
Ab https://docs.pytest.org/en/stable/getting-started.html
"""

import pytest


def f():
    """
    Explicat ipsum.
    """
    raise ExceptionGroup(
        "Coetus nuntius",
        [
            RuntimeError(),
        ]
    )


def tento_exceptis_in_coetus():
    """
    Probatio coetus exceptione.
    """
    with pytest.raises(ExceptionGroup) as excnoti:
        f()
    assert excnoti.group_contains(RuntimeError)
    assert not excnoti.group_contains(TypeError)
