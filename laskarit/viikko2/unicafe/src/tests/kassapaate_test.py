import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):

    def setUp(self):
        self.kassapaate = Kassapaate()
        self.kortti = Maksukortti(10000)


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

    def test_kassapaate_kateismaksu_riittamaton_maukas(self):
        self.kassapaate.syo_maukkaasti_kateisella(230)
        self.tarkasta_kassapaate(100000, 0, 0,)

    def test_kassapaate_kateismaksu_riittamaton_edullinen(self):
        self.kassapaate.syo_edullisesti_kateisella(5)
        self.tarkasta_kassapaate(100000, 0, 0,)

    def test_kassapaate_korttimaksu_riittava_maukas(self):

        self.assertTrue(self.kassapaate.syo_maukkaasti_kortilla(self.kortti))
        self.tarkasta_kassapaate(100000, 0, 1,)
        self.assertEqual(self.kortti.saldo, 9600)

    def test_kassapaate_korttimaksu_riittava_edullinen(self):

        self.assertTrue(self.kassapaate.syo_edullisesti_kortilla(self.kortti))
        self.tarkasta_kassapaate(100000, 1, 0,)
        self.assertEqual(self.kortti.saldo, 9760)

    def test_kassapaate_korttimaksu_eiriita_maukas(self):

        tyhjaKortti = Maksukortti(5)
        self.assertFalse(self.kassapaate.syo_maukkaasti_kortilla(tyhjaKortti))
        self.tarkasta_kassapaate(100000, 0, 0,)
        self.assertEqual(tyhjaKortti.saldo, 5)

    def test_kassapaate_korttimaksu_eiriita_edullinen(self):

        tyhjaKortti = Maksukortti(5)
        self.assertFalse(self.kassapaate.syo_edullisesti_kortilla(tyhjaKortti))
        self.tarkasta_kassapaate(100000, 0, 0,)
        self.assertEqual(tyhjaKortti.saldo, 5)

    def test_kortille_rahaa_toimii(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti, 10000)
        self.assertEqual(self.kortti.saldo, 20000)
        self.tarkasta_kassapaate(110000, 0, 0,)

    def test_kortille_rahaa_eitoimi(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti, 0)
        self.tarkasta_kassapaate(100000, 0, 0,)