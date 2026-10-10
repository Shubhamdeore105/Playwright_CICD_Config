from pages.login_page import LoginPage
from pages.dashboard_page import dashboard
from utils.config import PASSWORD, USERNAME, Base_URL


def testlogin(page):
        page.goto( Base_URL+"/web/index.php/auth/login",
                  wait_until="domcontentloaded",
                  timeout=30000)

        login_page=LoginPage(page)
        dashboard_page=dashboard(page)

        login_page.login(USERNAME, PASSWORD)

        dashboard_page.sidebar_button.click()
        dashboard_page.Profile_dropdown.click()
        dashboard_page.logout_button.click()

        #Test CICD configuration
        


