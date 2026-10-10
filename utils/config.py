
import os

Base_URL = os.getenv(
    "ORANGEHRM_BASE_URL",
    "https://opensource-demo.orangehrmlive.com"
)

USERNAME = os.getenv("ORANGEHRM_USERNAME", "Admin")
PASSWORD = os.getenv("ORANGEHRM_PASSWORD", "admin123")


