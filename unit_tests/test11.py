import unittest
import vf

class testcase(unittest.TestCase):

    def test(self):
        fs = vf.WriteFmtStr(value=0x001020, address=0x601020, value_base=0x55440000, offset=10, arch=64)
        test_fmt_str = fs.generate_fmt_str()
        correct_fmt_str = b'%4128c%17$hn%17700c%18$hn%43708c%19$hn%65536c%20$hn00000 \x10`\x00\x00\x00\x00\x00"\x10`\x00\x00\x00\x00\x00$\x10`\x00\x00\x00\x00\x00&\x10`\x00\x00\x00\x00\x00'
        self.assertTrue(test_fmt_str == correct_fmt_str)

if __name__ == '__main))':
    unittest.main()
