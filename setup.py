# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
#
# # Note: To use the 'upload' functionality of this file, you must:
# #   $ pip install twine
#
import io
import os
import sys
from shutil import rmtree
from setuptools import find_packages, setup, Command

#
# # Package meta-data.
NAME = 'mioAuto'
DESCRIPTION = 'An e2e testing core.'
URL = 'https://github.com/balzaron/BlueTest-AutoBrowser'
EMAIL = 'shanyue.gao@mioying.com'
AUTHOR = 'shanyue.gao'
REQUIRES_PYTHON = '>=3.7.0'
VERSION = "0.0.1"
#
# # What packages are required for this module to be executed?
REQUIRED = [
    "	aiohttp==3.4.4	",
    "	aircv==1.4.6	",
    "	asn1crypto==0.24.0	",
    "	async-timeout==3.0.1	",
    "	atomicwrites==1.2.1	",
    "	attrs==18.2.0	",
    "	better-exceptions-fork==0.2.1.post6	",
    "	cchardet==2.1.4	",
    "	certifi==2018.10.15	",
    "	cffi==1.11.5	",
    "	chardet==3.0.4	",
    "	colorama==0.4.1	",
    "	cryptography==2.3.1	",
    "	Deprecated==1.2.4	",
    "	googleapis-common-protos==1.5.5	",
    "	grpcio==1.16.1	",
    "	grpcio-tools==1.16.1	",
    "	idna==2.7	",
    "	Jinja2==2.10	",
    "	loguru==0.2.4	",
    "	lxml==4.2.5	",
    "	miotech-py-commons==0.0.1	",
    "	more-itertools==4.3.0	",
    "	multidict==4.5.2	",
    "	numpy==1.15.4	",
    "	oauthlib==2.1.0	",
    "	opencv-python==3.4.4.19	",
    "	pandas==0.23.4	",
    "	Pillow==5.3.0	",
    "	pluggy==0.8.0	",
    "	protobuf==3.6.1	",
    "	py==1.7.0	",
    "	pycparser==2.19	",
    "	Pygments==2.7.4	",
    "	pymongo==3.7.2	",
    "	pyOpenSSL==18.0.0	",
    "	pytesseract==0.2.6	",
    "	pytest==4.0.0	",
    "	python-dateutil==2.7.5	",
    "	pytz==2018.9	",
    "	PyYAML==3.13	",
    "	requests==2.19.1	",
    "	requests-oauthlib==0.8.0	",
    "	selenium==3.141.0	",
    "	six==1.11.0	",
    "	TestLink-API-Python-client==0.8.0	",
    "	unittest-data-provider==1.0.1	",
    "	unittest-xml-reporting==2.2.0	",
    "	urllib3==1.23	",
    "	wrapt==1.11.0	",
    "	yarl==1.2.6	",
]

# What packages are optional?
EXTRAS = {
    # 'fancy feature': ['django'],
}

# The rest you shouldn't have to touch too much :)
# ------------------------------------------------
# Except, perhaps the License and Trove Classifiers!
# If you do change the License, remember to change the Trove Classifier for that!

here = os.path.abspath(os.path.dirname(__file__))

# Import the README and use it as the long-description.
# Note: this will only work if 'README.md' is present in your MANIFEST.in file!
try:
    with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

# Load the package's __version__.py module as a dictionary.
about = {}
if not VERSION:
    with open(os.path.join(here, NAME, '__version__.py')) as f:
        exec(f.read(), about)
else:
    about['__version__'] = VERSION


class UploadCommand(Command):
    """Support setup.py upload."""

    description = 'Build and publish the package.'
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print('\033[1m{0}\033[0m'.format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status('Removing previous builds…')
            rmtree(os.path.join(here, 'dist'))
        except OSError:
            pass

        self.status('Building Source and Wheel (universal) distribution…')
        os.system('{0} setup.py sdist bdist_wheel --universal'.format(sys.executable))

        self.status('Uploading the package to PyPI via Twine…')
        os.system('twine upload dist/*')

        self.status('Pushing git tags…')
        os.system('git tag v{0}'.format(about['__version__']))
        os.system('git push --tags')

        sys.exit()
#
#
# # Where the magic happens:
setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(exclude=('tests',)),
    # If your package is a single module, use this instead of 'packages':
    # py_modules=['mypackage'],

    # entry_points={
    #     'console_scripts': ['mycli=mymodule:cli'],
    # },
    install_requires=REQUIRED,
    extras_require=EXTRAS,
    include_package_data=True,
    license='MIT',
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7.0',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
    # $ setup.py publish support.
    cmdclass={
        'upload': UploadCommand,
    },
)

setup(name='autoMiotech',
      version='0.0.1',
      description='Miotech Library for Python automatic testing',
      author='shanyue.gao',
      author_email='shanyue.gao@mioying.com',
      license='Apache 2.0',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=REQUIRED)
