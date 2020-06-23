import unittest
import vf

class testcase(unittest.TestCase):

    def test(self):
        fs = vf.WriteFmtStr(value=0x08044008, address=0x08046030, offset=10, num_writes=4)
        test_fmt_str = fs.generate_fmt_str()
        correct_fmt_str = b'0`\x04\x081`\x04\x082`\x04\x083`\x04\x08%248x%10$hhn%312x%11$hhn%196x%12$hhn%260x%13$hhn'
        self.assertTrue(test_fmt_str == correct_fmt_str)

if __name__ == '__main))':
    unittest.main()
