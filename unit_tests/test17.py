import unittest
import vf

class testcase(unittest.TestCase):

    def test(self):
        fs = vf.WriteFmtStr(value=0x402010, address=0x601030, offset=10, arch=64, alignment_bytes=20)
        test_fmt_str = fs.generate_fmt_str()
        correct_fmt_str = b'00000000000000000000%8188c%17$hn%57392c%18$hn%65472c%19$hn%65536c%20$hn0\x10`\x00\x00\x00\x00\x002\x10`\x00\x00\x00\x00\x004\x10`\x00\x00\x00\x00\x006\x10`\x00\x00\x00\x00\x00'
        self.assertTrue(test_fmt_str == correct_fmt_str)

if __name__ == '__main))':
    unittest.main()
