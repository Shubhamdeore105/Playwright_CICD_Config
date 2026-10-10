from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page:Page):

        self.page=Page

        self.username = page.locator("//input[@name='username']")
        self.password = page.locator("//input[@name='password']")
        self.login_button = page.get_by_role("button", name="Login")

    def login(self, username, password):
        self.username.fill(username)
        self.password.fill(password)
        self.login_button.click()
        