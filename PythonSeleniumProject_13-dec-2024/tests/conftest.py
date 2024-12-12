
import pytest
from selenium import webdriver


driver =  None

# Registering CLI option for pytest
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome",
        help="Browser name to execute tests: chrome, firefox, or IE"
    )


# Fixture for browser setup
@pytest.fixture(scope="class")
def setup(request):
    global driver

    # Retrieve the browser name from CLI argument
    browser_name = request.config.getoption("--browser_name")

    if browser_name == "chrome":
        # chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument("headless")  # Add headless mode for Chrome
        # driver = webdriver.Chrome(options=chrome_options)
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    elif browser_name == "IE":
        driver = webdriver.Ie()  # Ensure IE WebDriver is set up if required
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()

    # Attach driver to the test class
    request.cls.driver = driver
    yield
    driver.quit()

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
        driver.get_screenshot_as_file(name)
