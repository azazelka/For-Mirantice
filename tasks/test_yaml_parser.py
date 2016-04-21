import unittest
import yaml_parser


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
