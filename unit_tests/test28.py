import unittest
import vf

class testcase(unittest.TestCase):

    def test(self):
        fs = vf.WriteFmtStr(value=0x402010, address=0x601030, offset=10, write_sizes=[2, 1, 2])
        test_fmt_str = fs.generate_fmt_str()
        correct_fmt_str = b'0\x10`\x002\x10`\x003\x10`\x00%8196x%10$hn%304x%11$hhn%57024x%12$hn'
        self.assertTrue(test_fmt_str == correct_fmt_str)

if __name__ == '__main))':
    unittest.main()
