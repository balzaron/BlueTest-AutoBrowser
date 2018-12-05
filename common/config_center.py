import yaml, os

from common.utils import get_parent_abs_path


def globalconfig():
    with open(get_parent_abs_path()+'/resource/config.yaml') as f:
        conf = yaml.load(f)
        return conf

def IDsConfig():
    with open(get_parent_abs_path()+'/resource/full_regression.yaml') as f:
        conf = yaml.load(f)
        return conf

minus = os.environ.get('minus')

if __name__ == '__main__':
    ids = IDsConfig()
    print(ids)
    nav= ids.get('super admin')
    print(nav)