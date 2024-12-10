# REPO:
https://github.com/eshut/Framework-Python

# PAGES
This directory should contain Page-Objects with described logic and locators for each page

### Structural Example:
```
- login_page.py 
- main_page.py
....
```

### Page Example:
```python
import os

from framework.logger.logger import Logger
from framework.utils.BrowserActions import LinkOperations
from framework.utils.ElementOperations import Button, Input
from framework.utils.time_utils import wait_time


email = os.getenv("EMAIL_VALUE")
password = os.getenv("PASS_VALUE")


class LoginPage(Logger):
    def __init__(self, logger=__file__):
        super().__init__(logger)
        self.login_page = LinkOperations("https://www.website.com/login")
        self.main_page = LinkOperations("https://www.website.com/")
        self.login_button = Button("//button[@type='submit']")
        self.login_input = Input("//input[@id='email']")
        self.password_input = Input("//input[@id='password']")

    def login(self):
        # Open and login on the page
        self.login_page.get()
        self.login_input.move_mouse()
        self.login_input.click()
        self.login_input.send(email)
        self.password_input.move_mouse()
        self.password_input.click()
        self.password_input.send(password)
        wait_time(5)
        self.login_button.move_mouse()
        wait_time(1)
        self.login_button.click()
        
        # Open Main Page
        self.main_page.get()

```