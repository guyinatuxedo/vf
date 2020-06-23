import unittest
import vf

class testcase(unittest.TestCase):

    def test(self):
        fs = vf.WriteFmtStr(value=0x08044008, address=0x08046030, offset=10, arch=86)
        test_fmt_str = fs.generate_fmt_str()
        correct_fmt_str = b'0`\x04\x082`\x04\x08%16384x%10$hn%51196x%11$hn'
        self.assertTrue(test_fmt_str == correct_fmt_str)

if __name__ == '__main))':
    unittest.main()
