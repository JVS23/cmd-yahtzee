import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):

    def setUp(self):
        self.kassapaate = Kassapaate()


    def tarkasta_kassapaate(self, raha, edu, mau):
        self.assertEqual(self.kassapaate.kassassa_rahaa, raha)
        self.assertEqual(self.kassapaate.edulliset, edu)
        self.assertEqual(self.kassapaate.maukkaat, mau)


    def test_kassapaate_oikein(self):
        self.tarkasta_kassapaate(100000, 0, 0,)

    def test_kassapaate_kateismaksu_riittava(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.tarkasta_kassapaate(100640, 1, 1,)

    def test_kassapaate_kateismaksu_riittamaton(self):
        self.kassapaate.syo_maukkaasti_kateisella(230)
        self.tarkasta_kassapaate(100000, 0, 0,)

    def test_kassapaate_korttimaksu_riittava(self):
        self.maksukortti = Maksukortti(10000)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.tarkasta_kassapaate(100400, 0, 1,)