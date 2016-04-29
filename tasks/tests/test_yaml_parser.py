import unittest
from random import randint
import logging

import yaml

import tasks.yaml_parser
from tasks.tests.structure_generator import StructureGenerator
from tasks.tests.cycle_decorator import cycle_decorator


class TestYmlParser(unittest.TestCase):
    def test_list_first(self):
        result = tasks.yaml_parser.st_parser('file2.yml')
        self.assertEqual(tasks.yaml_parser.yml_parser('file2.yml'), result)

    def test_dict_first(self):
        result = tasks.yaml_parser.st_parser('file3.yml')
        self.assertEqual(tasks.yaml_parser.yml_parser('file3.yml'), result)

    def test_dict_first2(self):
        result = tasks.yaml_parser.st_parser('file1.yml')
        self.assertEqual(tasks.yaml_parser.yml_parser('file1.yml'), result)

    def test_dict_is_list_element(self):
        result = tasks.yaml_parser.st_parser('file4.yml')
        self.assertEqual(tasks.yaml_parser.yml_parser('file4.yml'), result)

    def test_yml_dump_list_is_dict_element(self):
        result = tasks.yaml_parser.st_parser('file5.yml')
        self.assertEqual(tasks.yaml_parser.yml_parser('file5.yml'), result)

    def test_yml_dump_list_is_list_element(self):
        result = tasks.yaml_parser.st_parser('file6.yml')
        self.assertEqual(tasks.yaml_parser.yml_parser('file6.yml'), result)

    @cycle_decorator(5000)
    def test_stress(self):
        depth = randint(1, 4)
        size = randint(1, 5)
        seed = randint(0, 9999999999)

        structure = StructureGenerator(size, depth, seed).structure
        result = yaml.dump(structure, default_flow_style=False)

        logging.basicConfig(format=u'%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s',
                            level=logging.DEBUG, filename=u'mylog.log')
        logging.debug('Depth: {0}, size: {1}, seed: {2}'.format(depth, size, seed))

        with open("res.yml", 'w')as fd:
            fd.write(result)
        self.assertEqual(tasks.yaml_parser.yml_parser("res.yml"), structure)


if __name__ == '__main__':
    unittest.main()
