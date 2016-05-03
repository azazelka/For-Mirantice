import logging
from random import randint

import pytest
import yaml

import tasks.yaml_parser
from tasks.tests.structure_generator import StructureGenerator


class TestPyTest(object):
    def setup_class(self):
        self.depth = randint(1, 4)
        self.size = randint(1, 5)
        self.seed = randint(0, 9999999999)
        print ("\nclass setup\n")

    def teardown_class(self):
        print ("\nclass teardown\n")

    def setup(self):
        print("\nsetup method\n ")

    def teardown(self):
        print("\nteardown method\n")

    @pytest.mark.mytest
    def test_one(self):
        result = tasks.yaml_parser.st_parser('file3.yml')
        assert tasks.yaml_parser.yml_parser('file3.yml') == result

    @pytest.mark.mytest
    def test_one(self):
        result = tasks.yaml_parser.st_parser('file2.yml')
        assert tasks.yaml_parser.yml_parser('file2.yml') == result

    def test_two(self):
        result = tasks.yaml_parser.st_parser('file1.yml')
        assert tasks.yaml_parser.yml_parser('file1.yml') == result

    @pytest.mark.parametrize('i', [1, 2, 3])
    def test_stress2(self, i):

        structure = StructureGenerator(self.size, self.depth, self.seed).structure
        result = yaml.dump(structure, default_flow_style=False)

        logging.basicConfig(format=u'%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s',
                            level=logging.DEBUG, filename=u'mylog.log')
        logging.debug('Depth: {0}, size: {1}, seed: {2}'.format(self.depth, self.size, self.seed))

        with open("res.yml", 'w')as fd:
            fd.write(result)
        assert tasks.yaml_parser.yml_parser("res.yml") == structure
