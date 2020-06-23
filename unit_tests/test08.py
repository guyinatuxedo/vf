import unittest
import vf

class testcase(unittest.TestCase):

    def test(self):
        fs = vf.WriteFmtStr(value=0x00004008, address=0x8045060, valueBase=0x55440000, offset=10)
        test_fmt_str = fs.generate_fmt_str()
        correct_fmt_str = b'`P\x04\x08bP\x04\x08%16384x%10$hn%49144x%11$hn'
        self.assertTrue(test_fmt_str == correct_fmt_str)

if __name__ == '__main))':
    unittest.main()
