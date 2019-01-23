import yaml
from mioAuto.common.utils import get_abs_path


def getConfig():
    with open(get_abs_path(__file__) + '/config.yml') as f:
        conf = yaml.load(f)
        return conf


