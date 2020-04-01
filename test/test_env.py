import configparser as cp
from os import path

config_file = path.join(path.dirname(__file__), '../setup.cfg')


def test_config():
    config = cp.ConfigParser()

    assert config.read(config_file, encoding='utf8') == [config_file]
    assert 'metadata' in config, 'section [metadata] is not exists'
    assert config['metadata']['name'] == 'python3-test'
