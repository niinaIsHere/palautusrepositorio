from tuomari import Tuomari
from tekoaly import Tekoaly
from KPS import KiviPaperiSakset


class KPSTekoaly(KiviPaperiSakset):

    def __init__(self):
        self.tekoaly = Tekoaly()

    def _toisen_siirto(self, eka):
        print("ASKED FOR MOVE")
        return self.tekoaly.anna_siirto()

