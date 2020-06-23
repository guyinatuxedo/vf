import unittest
import vf

class testcase(unittest.TestCase):

    def test(self):
        fs = vf.WriteFmtStr(value=0x402010, address=0x601030, offset=10, arch=64, write_sizes=[2, 1, 2, 1, 2, 2])
        test_fmt_str = fs.generate_fmt_str()
        correct_fmt_str = b'%8208c%21$hn%304c%22$hhn%57024c%23$hn%256c%24$hhn%65280c%25$hn%65536c%26$hn00000000000000\x10`\x00\x00\x00\x00\x002\x10`\x00\x00\x00\x00\x003\x10`\x00\x00\x00\x00\x005\x10`\x00\x00\x00\x00\x006\x10`\x00\x00\x00\x00\x008\x10`\x00\x00\x00\x00\x00'
        self.assertTrue(test_fmt_str == correct_fmt_str)

if __name__ == '__main))':
    unittest.main()
