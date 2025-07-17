import pytest
from selenium import webdriver

from Actions.ActionPage import Action_Page, Admin_Page, Admin_User_Management_Page
from Config.Configuration import Config

@pytest.fixture(scope="session")
def driver_setup():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture(scope = "session")
def login(driver_setup):
    driver = driver_setup
    login_page = Action_Page(driver)
    login_page.navigate_to_login_url(Config.BASE_URL)
    return login_page

def test_login_page_on_automation_customer_service_website(login):
    login.enter_username("Admin")
    login.enter_password("admin123")
    login.click_login_button()

def test_admin_page(login):
    admin_page = Admin_Page(login.driver)
    admin_page.click_admin_job()

def test_admin_user_management_page(login):
    admin_user_management = Admin_User_Management_Page(login.driver)
    admin_user_management.click_user_management()
    admin_user_management.click_users()
    admin_user_management.click_job()
    admin_user_management.click_job_title()
    admin_user_management.click_job_drop()
    admin_user_management.click_pay_grades()
    admin_user_management.click_job_dropdown()
    admin_user_management.click_employment_status()
    admin_user_management.click_job_drop_down()
    admin_user_management.click_job_categories()
    admin_user_management.click_job_down()
    admin_user_management.click_works_shifts()
    admin_user_management.click_organisation()
    admin_user_management.click_general_information()
    admin_user_management.click_locations()
    admin_user_management.click_structures()
    admin_user_management.click_qualifications()
    admin_user_management.click_skills()
    admin_user_management.click_education()
    admin_user_management.click_licenses()
    admin_user_management.click_languages()
    admin_user_management.click_memberships()
    admin_user_management.click_nationalities()
    admin_user_management.click_corporate_branding()
    admin_user_management.click_configuration()
    admin_user_management.click_email_configuration()
    admin_user_management.click_emai_subscriptions()
    admin_user_management.click_localization()
    admin_user_management.click_language_packages()
    admin_user_management.click_modules()
    admin_user_management.click_social_media_authentication()
    admin_user_management.click_register_oauth_client()
    admin_user_management.click_ldap_configuration()

