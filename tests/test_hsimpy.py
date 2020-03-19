# -*- coding: utf-8 -*-


import unittest
from hsimpy import Hsimpy


class HsimpyTest(unittest.TestCase):
    '''
    TESTING TYPE OF password PARAM
    '''
    def test_password_function_param(self):
        try:
            def func():
                return

            hsimp_func = Hsimpy(func)
        except TypeError as err:
            self.assertRaises(TypeError)

    def test_password_int_param(self):
        try:
            hsimp_number = Hsimpy(123456);
        except TypeError as err:
            self.assertRaises(TypeError)

    def test_password_float_param(self):
        try:
            hsimp_float = Hsimpy(123.456)
        except TypeError as err:
            self.assertRaises(TypeError)

    def test_password_dict_param(self):
        try:
            hsimp_dict = Hsimpy({dict: 2})
        except TypeError as err:
            self.assertRaises(TypeError)

    def test_password_json_param(self):
        try:
            hsimp_json = Hsimpy({"dict": "2"})
        except TypeError as err:
            self.assertRaises(TypeError)

    def test_password_unicode_param(self):
        hsimp_unicode = Hsimpy(u'dale')
        self.assertEqual(True, True)

    def test_password_str_param(self):
        hsimp_str = Hsimpy('dale')
        self.assertEqual(True, True)

    '''
    TESTING STRENGHT algorithm
    '''
    def test_password_bad_str_param(self):
        hsimp = Hsimpy('weak')
        self.assertEqual(hsimp.security_level, 'bad')
        self.assertEqual(hsimp.possible_characters, 26)
        self.assertEqual(hsimp.possible_combinations, 456976.0)
        self.assertEqual(hsimp.time_in_seconds, 0.11717333333333334)

    def test_password_bad_str_up_param(self):
        hsimp = Hsimpy('weakWEAK')
        self.assertEqual(hsimp.security_level, 'bad')
        self.assertEqual(hsimp.possible_characters, 52)
        self.assertEqual(hsimp.possible_combinations, 53459728531456.0)
        self.assertEqual(hsimp.time_in_seconds, 13707622.700373333)

    def test_password_ok_str_up_number_param(self):
        hsimp = Hsimpy('weakWEAK123')
        self.assertEqual(hsimp.security_level, 'good')
        self.assertEqual(hsimp.possible_characters, 62)
        self.assertEqual(hsimp.possible_combinations, 5.20365606838371e+19)
        self.assertEqual(hsimp.time_in_seconds, 13342707867650.537)

    def test_password_good_str_up_number_special_param(self):
        hsimp = Hsimpy('weakWEAK123!@#')
        self.assertEqual(hsimp.security_level, 'good')
        self.assertEqual(hsimp.possible_characters, 77)
        self.assertEqual(hsimp.possible_combinations, 2.575550990467221e+26)
        self.assertEqual(hsimp.time_in_seconds, 6.6039768986339e+19)

    def test_password_good_str_up_number_special_dots_param(self):
        hsimp = Hsimpy('weakWEAK123!@#.,')
        self.assertEqual(hsimp.security_level, 'good')
        self.assertEqual(hsimp.possible_characters, 96)
        self.assertEqual(hsimp.possible_combinations, 5.204029246664727e+31)
        self.assertEqual(hsimp.time_in_seconds, 1.334366473503776e+25)

    def test_password_bad_number_param(self):
        hsimp = Hsimpy('123')
        self.assertEqual(hsimp.security_level, 'bad')
        self.assertEqual(hsimp.possible_characters, 10)
        self.assertEqual(hsimp.possible_combinations, 1000.0)
        self.assertEqual(hsimp.time_in_seconds, 0.0002564102564102564)

    def test_password_bad_number_special_param(self):
        hsimp = Hsimpy('123!@#')
        self.assertEqual(hsimp.security_level, 'bad')
        self.assertEqual(hsimp.possible_characters, 25)
        self.assertEqual(hsimp.possible_combinations, 244140625.0)
        self.assertEqual(hsimp.time_in_seconds, 62.600160256410255)

    def test_password_bad_number_special_dot_param(self):
        hsimp = Hsimpy('123!@#.,')
        self.assertEqual(hsimp.security_level, 'bad')
        self.assertEqual(hsimp.possible_characters, 44)
        self.assertEqual(hsimp.possible_combinations, 14048223625216.0)
        self.assertEqual(hsimp.time_in_seconds, 3602108.6218502563)

    def test_password_ok_number_special_dot_upper_param(self):
        hsimp = Hsimpy('123!@#.,ABC')
        self.assertEqual(hsimp.security_level, 'good')
        self.assertEqual(hsimp.possible_characters, 70)
        self.assertEqual(hsimp.possible_combinations, 1.977326743e+20)
        self.assertEqual(hsimp.time_in_seconds, 50700685717948.72)

    def test_password_bad_special_param(self):
        hsimp = Hsimpy('!@#$')
        self.assertEqual(hsimp.security_level, 'bad')
        self.assertEqual(hsimp.possible_characters, 15)
        self.assertEqual(hsimp.possible_combinations, 50625.0)
        self.assertEqual(hsimp.time_in_seconds, 0.012980769230769231)

    def test_password_bad_dot_param(self):
        hsimp = Hsimpy('.,.')
        self.assertEqual(hsimp.security_level, 'bad')
        self.assertEqual(hsimp.possible_characters, 19)
        self.assertEqual(hsimp.possible_combinations, 6859.0)
        self.assertEqual(hsimp.time_in_seconds, 0.0017587179487179487)

    def test_password_ok_str_repeat_param(self):
        hsimp = Hsimpy('aaaaaaaaaaaaaa')
        self.assertEqual(hsimp.security_level, 'good')
        self.assertEqual(hsimp.possible_characters, 26)
        self.assertEqual(hsimp.possible_combinations, 6.450997470329715e+19)
        self.assertEqual(hsimp.time_in_seconds, 16541019154691.578)

    def test_password_ok_number_repeat_param(self):
        hsimp = Hsimpy('1111111111111111111')
        self.assertEqual(hsimp.security_level, 'good')
        self.assertEqual(hsimp.possible_characters, 10)
        self.assertEqual(hsimp.possible_combinations, 1e+19)
        self.assertEqual(hsimp.time_in_seconds, 2564102564102.564)



if __name__ == '__main__':
    unittest.main()
