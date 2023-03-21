import unittest
from maksukortti import Maksukortti
from kassapaate import Kassapaate

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)
        self.kassa = Kassapaate()

    def test_luotu_kassa_on_olemassa(self):
        self.assertNotEqual(self.kassa, None)

    def test_kassa_luotu_oikeilla_arvoilla(self):
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(self.kassa.edulliset, 0)
        self.assertEqual(self.kassa.maukkaat, 0)
        
    def test_käteisostot(self):
        vaihtoraha_edullinen = self.kassa.syo_edullisesti_kateisella(240)
        vaihtoraha_maukas = self.kassa.syo_maukkaasti_kateisella(400)

        self.assertEqual(self.kassa.kassassa_rahaa, 100000 + 240 + 400)
        self.assertEqual(self.kassa.edulliset, 1)
        self.assertEqual(self.kassa.maukkaat, 1)
        self.assertEqual(vaihtoraha_maukas, 0)
        self.assertEqual(vaihtoraha_edullinen, 0)


        vaihtoraha_edullinen = self.kassa.syo_edullisesti_kateisella(100)
        vaihtoraha_maukas = self.kassa.syo_maukkaasti_kateisella(100)

        self.assertEqual(self.kassa.kassassa_rahaa, 100000 + 240 + 400)
        self.assertEqual(self.kassa.edulliset, 1)
        self.assertEqual(self.kassa.maukkaat, 1)
        self.assertEqual(vaihtoraha_maukas, 100)
        self.assertEqual(vaihtoraha_edullinen, 100)

    def test_korttiostos(self):
        edullinen_korttiostos = self.kassa.syo_edullisesti_kortilla(self.maksukortti)
        maukas_korttiostos = self.kassa.syo_maukkaasti_kortilla(self.maksukortti)

        self.assertEqual(self.maksukortti.saldo, 1000 - 240 - 400)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(self.kassa.edulliset, 1)
        self.assertEqual(self.kassa.maukkaat, 1)
        self.assertTrue(edullinen_korttiostos)
        self.assertTrue(maukas_korttiostos)

        korttiJollaEiTarpeeksiRahaa = Maksukortti(100)
        edullinen_korttiostos = self.kassa.syo_edullisesti_kortilla(korttiJollaEiTarpeeksiRahaa)
        maukas_korttiostos = self.kassa.syo_maukkaasti_kortilla(korttiJollaEiTarpeeksiRahaa)

        self.assertEqual(korttiJollaEiTarpeeksiRahaa.saldo, 100)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(self.kassa.edulliset, 1)
        self.assertEqual(self.kassa.maukkaat, 1)
        self.assertFalse(edullinen_korttiostos)
        self.assertFalse(maukas_korttiostos)

    def test_kortille_rahan_lataus(self):
        self.kassa.lataa_rahaa_kortille(self.maksukortti,1000)

        self.assertEqual(self.maksukortti.saldo, 2000)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000 + 1000)

        self.kassa.lataa_rahaa_kortille(self.maksukortti, -1000)

        self.assertEqual(self.maksukortti.saldo, 2000)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000 + 1000)
