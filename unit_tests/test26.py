import unittest
import vf

class testcase(unittest.TestCase):

    def test(self):
        fs = vf.WriteFmtStr(value=0x402010, address=0x601030, offset=10, arch=64, num_writes=8)
        test_fmt_str = fs.generate_fmt_str()
        correct_fmt_str = b'%16c%23$hhn%16c%24$hhn%32c%25$hhn%192c%26$hhn%256c%27$hhn%256c%28$hhn%256c%29$hhn%256c%30$hhn000000000000\x10`\x00\x00\x00\x00\x001\x10`\x00\x00\x00\x00\x002\x10`\x00\x00\x00\x00\x003\x10`\x00\x00\x00\x00\x004\x10`\x00\x00\x00\x00\x005\x10`\x00\x00\x00\x00\x006\x10`\x00\x00\x00\x00\x007\x10`\x00\x00\x00\x00\x00'
        self.assertTrue(test_fmt_str == correct_fmt_str)

if __name__ == '__main))':
    unittest.main()
