import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_oikein(self):
        self.assertEqual(self.maksukortti.saldo, 10)

    def test_lataus_toimii(self):
        self.maksukortti.lataa_rahaa(5)
        self.assertEqual(self.maksukortti.saldo, 15)

    def test_saldo_vahenee(self):
        self.assertTrue(self.maksukortti.ota_rahaa(5))
        self.assertEqual(self.maksukortti.saldo, 5)

    def test_saldo_ei_vahene_jos_otetaan_liikaa(self):
        self.assertFalse(self.maksukortti.ota_rahaa(15))
        self.assertEqual(self.maksukortti.saldo, 10)

    def test_saldo_euroissa_toimii(self):
        test = self.maksukortti.__str__()
        self.assertEqual(test, "saldo: 0.1")