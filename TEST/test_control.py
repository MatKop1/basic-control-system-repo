import unittest
import control 
import interface as inter

class TestControl(unittest.TestCase):
 
    def test_obj1(self):
        H1 = control.tf([1],[2,1])
        H2 = inter.LinearObj([1],[2,1])
        self.assertEqual(H1.num, H2.num,"Numerator of H1 is equal to H2")
        #self.assertEqual(H1.den, H2.den,"Denumerator of H1 is equal to H2")

    def test_obj2(self):
        H1 = control.tf([2],[1,1])
        H2 = inter.LinearObj([1],[2,1])
        self.assertNotEqual(H1.num, H2.num,"Numerator of H1 is not equal to H2")

    def test_strTolsit(self):
        s1 = "11"
        s2 = "0,0,0"
        s3 = "1,12,123,12345"
        s4 = ",1,"
        s5 = ",10,"
        s6 = "1,,2"
        self.assertEqual(inter.stringToList(s1),[11])
        self.assertEqual(inter.stringToList(s2),[0,0,0])
        self.assertEqual(inter.stringToList(s3),[1,12,123,12345])
        self.assertEqual(inter.stringToList(s4),[1])
        self.assertEqual(inter.stringToList(s5),[10])
        self.assertEqual(inter.stringToList(s6),[1,2])

