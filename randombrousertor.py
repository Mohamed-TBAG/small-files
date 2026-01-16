from selenium import webdriver
from stem import Signal
from stem.control import Controller
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from fake_useragent import UserAgent
import tempfile
import shutil
import random
from time import sleep

# Function to request a new Tor identity


def switch_ip():
    try:
        with Controller.from_port(port=9051) as controller:
            controller.authenticate()
            controller.signal(Signal.NEWNYM)
            print('Successfully requested a new Tor identity.')
    except Exception as e:
        print('An error occurred while switching Tor identity:', str(e))

# Function to configure the proxy


def configure_proxy(options, proxy):
    options.set_preference("network.proxy.type", 1)
    options.set_preference("network.proxy.socks",
                           proxy.split("//")[1].split(":")[0])
    options.set_preference("network.proxy.socks_port",
                           int(proxy.split(":")[2]))
    options.set_preference("network.proxy.socks_version", 5)
    options.set_preference("network.proxy.socks_remote_dns", True)
    # options.set_preference("places.history.enabled", False)
    options.set_preference("privacy.clearOnShutdown.offlineApps", True)
    options.set_preference("privacy.clearOnShutdown.passwords", True)
    options.set_preference("privacy.clearOnShutdown.siteSettings", True)
    options.set_preference("privacy.sanitize.sanitizeOnShutdown", True)
    options.set_preference("signon.rememberSignons", False)
    # options.set_preference("network.cookie.cookieBehavior", 2)
    options.set_preference("network.dns.disablePrefetch", True)
    options.set_preference("network.http.sendRefererHeader", 0)
    # Ensure no direct connections
    options.set_preference("network.proxy.no_proxies_on", "")

# Function to create a new temporary Firefox profile


def create_temp_profile():
    profile_dir = tempfile.mkdtemp()
    return profile_dir

# Function to clean up the temporary profile


def cleanup_profile(profile_dir):
    shutil.rmtree(profile_dir)

# Randomize User Agent


def get_random_user_agent():
    ua = UserAgent()
    return ua.random

# Function to configure random screen size and other browser attributes


def configure_random_browser_attributes(options):
    width = random.randint(1024, 1920)
    height = random.randint(768, 1080)
    options.add_argument(f"--width={width}")
    options.add_argument(f"--height={height}")


# Main script
if __name__ == "__main__":
    switch_ip()
    PROXY = "socks5://localhost:9050"
    options = FirefoxOptions()
    # options.add_argument("--headless")
    options.set_preference("general.useragent.override",
                           get_random_user_agent())

    # Create a new temporary Firefox profile
    profile_dir = create_temp_profile()
    options.profile = profile_dir

    # Configure the proxy
    # configure_proxy(options, PROXY)

    # Configure random browser attributes
    configure_random_browser_attributes(options)

    # Set up the Firefox service
    service = FirefoxService(
        executable_path=r'./geckodriver.exe'
    )

    # Launch the browser
    browser = webdriver.Firefox(service=service, options=options)
    browser.get("https://ident.me/")

    input("Press Enter to close the browser...")
    switch_ip()
    input("Press Enter to close the browser...")
    # Quit the browser and clean up the profile
    browser.quit()
    cleanup_profile(profile_dir)

# https://www.tiktok.com/signup/age-gate
# Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36
