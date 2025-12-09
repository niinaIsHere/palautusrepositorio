from enum import Enum
from tkinter import ttk, constants, StringVar


class Komento(Enum):
    SUMMA = 1
    EROTUS = 2
    NOLLAUS = 3
    KUMOA = 4


class Summa:
    def __init__(self, io):
        self.io = io
        self._previous = None

    def suorita(self, syote):
        self._previous = self.io.arvo()
        self.io.plus(syote)

    def kumoa(self):
        if self._previous is not None:
            self.io.aseta_arvo(self._previous)


class Erotus:
    def __init__(self, io):
        self.io = io
        self._previous = None

    def suorita(self, syote):
        self._previous = self.io.arvo()
        self.io.miinus(syote)

    def kumoa(self):
        if self._previous is not None:
            self.io.aseta_arvo(self._previous)


class Nollaus:
    def __init__(self, io):
        self.io = io
        self._previous = None

    def suorita(self, syote):
        self._previous = self.io.arvo()
        self.io.nollaa()

    def kumoa(self):
        if self._previous is not None:
            self.io.aseta_arvo(self._previous)


class Kumoa:
    pass

class Kayttoliittyma:
    def __init__(self, sovelluslogiikka, root):
        self._sovelluslogiikka = sovelluslogiikka
        self._root = root
        self._previous = None

        self._komennot = {
            Komento.SUMMA: Summa(sovelluslogiikka),
            Komento.EROTUS: Erotus(sovelluslogiikka),
            Komento.NOLLAUS: Nollaus(sovelluslogiikka),
        }

    def _lue_syote(self):
        arvo = 0
        try:
            arvo = int(self._syote_kentta.get())
        except Exception:
            pass
        return arvo

    def kaynnista(self):
        self._arvo_var = StringVar()
        self._arvo_var.set(self._sovelluslogiikka.arvo())
        self._syote_kentta = ttk.Entry(master=self._root)

        tulos_teksti = ttk.Label(textvariable=self._arvo_var)

        summa_painike = ttk.Button(
            master=self._root,
            text="Summa",
            command=lambda: self._suorita_komento(Komento.SUMMA)
        )

        erotus_painike = ttk.Button(
            master=self._root,
            text="Erotus",
            command=lambda: self._suorita_komento(Komento.EROTUS)
        )

        self._nollaus_painike = ttk.Button(
            master=self._root,
            text="Nollaus",
            state=constants.DISABLED,
            command=lambda: self._suorita_komento(Komento.NOLLAUS)
        )

        self._kumoa_painike = ttk.Button(
            master=self._root,
            text="Kumoa",
            state=constants.DISABLED,
            command=lambda: self._suorita_komento(Komento.KUMOA)
        )

        tulos_teksti.grid(columnspan=4)
        self._syote_kentta.grid(columnspan=4, sticky=(constants.E, constants.W))
        summa_painike.grid(row=2, column=0)
        erotus_painike.grid(row=2, column=1)
        self._nollaus_painike.grid(row=2, column=2)
        self._kumoa_painike.grid(row=2, column=3)

    def _suorita_komento(self, komento):

        if komento == Komento.KUMOA and self._previous is not None:
            komento_olio = self._komennot[self._previous]
            komento_olio.kumoa()
        else:
            self._previous = komento
            komento_olio = self._komennot[komento]
            arvo = self._lue_syote()
            komento_olio.suorita(arvo)

        self._kumoa_painike["state"] = constants.NORMAL

        if self._sovelluslogiikka.arvo() == 0:
            self._nollaus_painike["state"] = constants.DISABLED
        else:
            self._nollaus_painike["state"] = constants.NORMAL

        self._syote_kentta.delete(0, constants.END)
        self._arvo_var.set(self._sovelluslogiikka.arvo())
