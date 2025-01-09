"""
Viveretur : velox_exemplum.py
Ab https://docs.pytest.org/en/stable/
"""

def incremento(a):
    """
    Explicat ipsum.
    """
    return a + 1

def tento_incremento():
    """
    Hoc est deficere.
    """
    assert incremento(3) == 5
