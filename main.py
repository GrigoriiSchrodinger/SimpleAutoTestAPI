import unittest

from asset.logo import logo
from src.utils import logger

logger = logger.setup_custom_logger('root')

if __name__ == '__main__':
    logger.info(logo)
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover('src/tests')
    runner = unittest.TextTestRunner()
    runner.run(test_suite)

