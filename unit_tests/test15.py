import unittest
import vf

class testcase(unittest.TestCase):

    def test(self):
        fs = vf.WriteFmtStr(value=0x08044008, address=0x08046030, offset=10, printed_bytes=30, alignment_bytes=20)
        test_fmt_str = fs.generate_fmt_str()
        correct_fmt_str = b'000000000000000000000`\x04\x082`\x04\x08%16334x%10$hn%51196x%11$hn'
        self.assertTrue(test_fmt_str == correct_fmt_str)

if __name__ == '__main))':
    unittest.main()
