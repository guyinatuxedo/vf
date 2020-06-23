import unittest
import vf

class testcase(unittest.TestCase):

    def test(self):
        fs = vf.WriteFmtStr(value=0x601020, address=0x00006030, address_base=0x55440000, offset=10, arch=64)
        test_fmt_str = fs.generate_fmt_str()
        correct_fmt_str = b'%4128c%17$hn%61504c%18$hn%65440c%19$hn%65536c%20$hn000000`DU\x00\x00\x00\x002`DU\x00\x00\x00\x004`DU\x00\x00\x00\x006`DU\x00\x00\x00\x00'
        self.assertTrue(test_fmt_str == correct_fmt_str)

if __name__ == '__main))':
    unittest.main()
