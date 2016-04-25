import string
import unittest
from logging import log

import yaml

import yaml_parser
from random import randint, choice
import structure_generator


class TestYmlParser(unittest.TestCase):
    def test_list_first(self):
        result = yaml_parser.st_parser('file2.yml')
        self.assertEqual(yaml_parser.yml_parser('file2.yml'), result)

    def test_dict_first(self):
        result = yaml_parser.st_parser('file3.yml')
        self.assertEqual(yaml_parser.yml_parser('file3.yml'), result)

    def test_dict_first2(self):
        result = yaml_parser.st_parser('file1.yml')
        self.assertEqual(yaml_parser.yml_parser('file1.yml'), result)

    def test_dict_is_list_element(self):
        result = yaml_parser.st_parser('file4.yml')
        self.assertEqual(yaml_parser.yml_parser('file4.yml'), result)

    def test_yml_dump_list_is_dict_element(self):
        result = yaml_parser.st_parser('file5.yml')
        self.assertEqual(yaml_parser.yml_parser('file5.yml'), result)

    def test_yml_dump_list_is_list_element(self):
        result = yaml_parser.st_parser('file6.yml')
        self.assertEqual(yaml_parser.yml_parser('file6.yml'), result)

    def test_stress(self):
        for i in range(5000):
            depth = randint(1, 6)
            size = randint(1, 20)
            seed = randint(0, 9999999999)

            structure = structure_generator.structure_generator(size, depth, seed).structure
            result = yaml.dump(structure, default_flow_style=False)
            res = result.split('\n')
            # print i, seed
            self.assertEqual(yaml_parser.rec_parser(res), structure)

if __name__ == '__main__':
    unittest.main()
