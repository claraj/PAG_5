from unittest import TestLoader
import xmlrunner

if __name__ == '__main__':

    test_loader = TestLoader()
    test_suite = test_loader.discover('tests')
    # Specify out directory, and report suffix. The default is a timestamp, which results in
    # lots of report files if this is run repeatedly. We only need the latest files.
    test_runner = xmlrunner.XMLTestRunner(output='test_reports', outsuffix='')
    test_runner.run(test_suite)
