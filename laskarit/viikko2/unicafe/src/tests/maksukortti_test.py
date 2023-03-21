import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")
    
    def test_rahan_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(2500)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 35.00 euroa")

    def test_saldo_vahenee_jos_tarpeeksi_rahaa(self):
        self.maksukortti.ota_rahaa(400)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 6.00 euroa")

    def test_saldo_ei_muutu_jos_rahaa_ei_ole_tarpeeksi(self):
        maksukortti = Maksukortti(100)
        
        maksukortti.ota_rahaa(1000)

        self.assertEqual(str(maksukortti), "Kortilla on rahaa 1.00 euroa")

    def test_metodi_palauttaa_true_jos_rahat_riittivät_ja_muuten_false(self):
        kortti = Maksukortti(100)

        self.assertTrue(kortti.ota_rahaa(100))
        self.assertFalse(kortti.ota_rahaa(100))
