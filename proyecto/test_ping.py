import unittest
from ping import ping

class TestPing(unittest.TestCase):
    
    def test_pingCorrecto(self):
        resultado,inf_extra=ping("google.es",1000)
        self.assertTrue(resultado)
        
    def test_pingIncorrecto(self):
        resultado,inf_extra=ping("googlecito.es",1000)
        self.assertFalse(resultado)

unittest.main()