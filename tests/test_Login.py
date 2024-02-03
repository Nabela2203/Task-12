# Using Data Driven Testing Framework (DDT), Page Object Model (POM), Explicit Wait, Expected Conditions, Pytest
# kindly do the following task as mentioned below :-
# 1) Create an Excel file which will comprise of Test ID, Username, Password, Date, Time of Test, Name of Tester,
# Test Result for login into the Zen portal.
# 3) Login into the Zen Portal using the Username and Password provided in the Excel file. Try to use 5 Username and Password.
# 4) If the Login is successful your Python code will write in the Excel file whether your Test Passed or Test Failed.
# 5) Do not use sleep() method
from datetime import datetime

import pytest
from pages.LoginPage import LoginPage
from utilities import ExcelUtils

path = "ExcelFiles/zen_portal.xlsx"
sheet_name = "LoginTest"


@pytest.mark.usefixtures("setup_and_teardown")
class TestZenPortal:

    def test_login(self):

        rows = ExcelUtils.get_row_count(path, sheet_name)

        for r in range(2, rows + 1):
            username = ExcelUtils.read_data(path, sheet_name, r, 2)
            password = ExcelUtils.read_data(path, sheet_name, r, 3)

            login_page = LoginPage(self.driver)
            class_page = login_page.click_login_button(username, password)
            # to add date in excel
            current_date = datetime.now().strftime("%d-%m-%Y")
            ExcelUtils.write_data(path, sheet_name, r, 4, current_date)
            # to add time in excel
            current_time = datetime.now().time().strftime("%H:%M:%S")
            ExcelUtils.write_data(path, sheet_name, r, 5, current_time)

            try:
                class_page.class_text_is_displayed().is_displayed()
                ExcelUtils.write_data(path, sheet_name, r, 7, "PASS")
                class_page.click_on_logout()
            except:
                ExcelUtils.write_data(path, sheet_name, r, 7, "FAIL")
                class_page.refresh_page()



