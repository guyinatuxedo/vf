import unittest
import vf

class testcase(unittest.TestCase):

    def test(self):
        fs = vf.WriteFmtStr(value=0x00004008, address=0x00006030, value_vase=0x77550000, address_base=0x55440000, offset=10)
        test_fmt_str = fs.generate_fmt_str()
        correct_fmt_str = b'0`DU2`DU%16384x%10$hn%49144x%11$hn'
        self.assertTrue(test_fmt_str == correct_fmt_str)

if __name__ == '__main))':
    unittest.main()
