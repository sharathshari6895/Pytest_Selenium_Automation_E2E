import allure, logging, pytest
from Utils.util import analyze_accessibility_results
from Tests.configtest import accessibility_driver, run_accessibility_test, config_path, logger_setup, read_config_data


class TestAccessibility:
    """Test method for URL accessibility, utilizing fixtures for WebDriver, test execution, configuration reading, and logging setup."""

    @pytest.mark.run(order=15)
    @allure.severity(allure.severity_level.CRITICAL)
    def test_accessibility_on_url(self, accessibility_driver, run_accessibility_test,
                                  logger_setup):
        logging.getLogger("root").info("Starting test_accessibility_on_url")
        accessibility_config = read_config_data(config_path, 'Accessibility')
        results = run_accessibility_test(accessibility_config['accessibility_url'])
        analyze_accessibility_results(results)
        logging.getLogger("root").info("Finding  violations completed")
        logging.getLogger("root").info("Ending test_accessibility_on_url")
