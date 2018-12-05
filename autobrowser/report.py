from unittest import defaultTestLoader

from BeautifulReport import BeautifulReport

if __name__ == '__main__':
    test_suite = defaultTestLoader.discover('./', pattern='Test*.py')
    result = BeautifulReport(test_suite)
    result.report(filename='Test report', description='Miotech', log_path='.')