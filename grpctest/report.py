from unittest import defaultTestLoader

from BeautifulReport import BeautifulReport

if __name__ == '__main__':
    test_suite = defaultTestLoader.discover('./', pattern='test*.py')
    result = BeautifulReport(test_suite)
    result.report(filename='report', description='Grpc FI pikachu', log_path='.')