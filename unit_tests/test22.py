import unittest
import vf

class testcase(unittest.TestCase):

    def test(self):
        fs = vf.WriteFmtStr(value=0x08044008, address=0x08046030, offset=10, max_size=56, arch=64)
        test_fmt_str = fs.generate_fmt_str()
        correct_fmt_str = b'%134496264c%15$n%4160471032c%16$n00000000`\x04\x08\x00\x00\x00\x004`\x04\x08\x00\x00\x00\x00'
        self.assertTrue(test_fmt_str == correct_fmt_str)

if __name__ == '__main))':
    unittest.main()
