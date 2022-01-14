import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_negatiivinen_tilavuus_antaa_nollan(self):
        varasto = Varasto(-0.1)
        self.assertEqual(varasto.tilavuus, 0)

    def test_negatiivinen_saldo_antaa_nollan(self):
        varasto = Varasto(1, -1)
        self.assertEqual(varasto.saldo, 0)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)
    
    def test_negaa_ei_voi_lisata(self):
        self.varasto.lisaa_varastoon(10)
        self.varasto.lisaa_varastoon(-100)
        self.assertEqual(self.varasto.saldo, 10)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)
    
    def test_lisays_ei_ylita_tilavuutta(self):
        self.varasto.lisaa_varastoon(12)
        self.assertEqual(self.varasto.paljonko_mahtuu(), 0)
    
    def test_voi_ottaa_vain_mita_on(self):
        self.varasto.ota_varastosta(100000000)
        self.assertEqual(self.varasto.saldo, 0)
    
    def test_negaa_ei_voi_nyhjaista(self):
        otettu = self.varasto.ota_varastosta(-10)
        self.assertEqual(otettu, 0)
        

    def test_stringi_antaa_oikean(self):
        stringi = str(self.varasto)
        self.assertEqual(stringi, 'saldo = 0, vielä tilaa 10')