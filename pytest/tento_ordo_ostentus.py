"""
viveretur : tento_ordo_ostentus.py
Ab https://docs.pytest.org/en/stable/getting-started.html
"""

class TentoOrdoOstentusExemplum:
    """
    Proba multae Ostentiae.
    """
    value = 0       # Singularis nam ordo.


    def tento_unum(self):
        """
        Explicat ipsum.
        """
        self.value = 1
        assert self.value == 1


    def tento_duo(self):
        """
        Hoc est deficere.
        """
        assert self.value == 1
