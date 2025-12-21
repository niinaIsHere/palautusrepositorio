from tuomari import Tuomari
from tekoaly_parannettu import TekoalyParannettu
from KPS import KiviPaperiSakset


class KPSParempiTekoaly(KiviPaperiSakset):

    def __init__(self):
        self.tekoaly = TekoalyParannettu(10)

    def _toisen_siirto(self, ensimmaisen_siirto):
        return self.tekoaly.anna_siirto()
