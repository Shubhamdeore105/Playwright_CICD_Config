from playwright.sync_api import Page

class dashboard:
    def __init__(self, page:Page):

        self.page=Page

        self.sidebar_button= page.locator('//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/div/div/button')

        self.Profile_dropdown=page.locator("//img[@alt='profile picture']")

        self.logout_button=page.get_by_text("Logout")

    def dashboard_test(self):

        self.sidebar_button.click()

    def logout(self):
        self.Profile_dropdown.click()
        self.logout_button.click()
        