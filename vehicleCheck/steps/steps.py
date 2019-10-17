from behave import given, when, then
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotInteractableException

driver = webdriver.Chrome(executable_path=r'C:/Users/Yaaseen/PycharmProjects/DLG_PROJECT/drivers/chromedriver')

@given("I open the url in a web browser")
def open_url(context):
    """
    Stp to open the url in a browser
    :param context:
    :return:
    """
    context.webdriver = driver.get('https://covercheck.vwfsinsuranceportal.co.uk/')
    time.sleep(2)

@given("the home page has loaded")
def assert_home_page_loaded(context):
    """
    Step to verify homepage is loaded
    :param context:
    :return:
    """
    context.webdriver = driver.find_element_by_tag_name('img')

    try:
        WebDriverWait(context.webdriver, 3).until(EC.presence_of_element_located((By.TAG_NAME, 'img')))
        print
        "Page is ready!"
    except TimeoutException:
        print
        "Loading took too much time!"

@when("the home page has loaded")
def assert_home_page_loaded(context):
    """
    Step to verify homepage is loaded
    :param context:
    :return:
    """
    context.webdriver = driver.find_element_by_tag_name('img')

    try:
        WebDriverWait(context.webdriver, 3).until(EC.presence_of_element_located((By.TAG_NAME, 'img')))
        print
        "Page is ready!"
    except TimeoutException:
        print
        "Loading took too much time!"

@then("I should see a page with VWFS Services as the heading")
def assert_home_page_header(context):
    """
    Step to verify home page header is VOlKSWAGON FINANCIAL SERVICES
    and webpage title is Dealer Portal
    :param context:
    :return:
    """
    context.webdriver = driver.find_element_by_css_selector("[title='Volkswagen Financial Services']")
    context.webdriver.title = driver.title
    try:
        assert "Dealer Portal" == context.webdriver.title
    except ArithmeticError as e:
        print('FAIL')

@then("a search box to find a vehicle")
def assert_search_box_is_present(context):
    """
    Step to verify that a search box to find a vehicle is present
    :param context:
    :return:
    """
    context.webdriver = driver.find_element_by_id('vehicleReg')
    try:
        WebDriverWait(context.webdriver, 3).until(EC.presence_of_element_located((By.ID, 'vehicleReg')))
        print
        "Search box is ready!"
    except TimeoutException:
        print
        "Loading took too much time!"

@when("the user inputs a '{reg}' (vehicle registration) which is not present in the data base")
def input_text_in_search_box(context, reg):
    """
    Step to input a vehicle registration, which is not present in the data base, into the search box
    :param context:
    :return:
    """
    context.webdriver = driver.find_element_by_id('vehicleReg')
    context.webdriver.send_keys(reg)

@when("the user inputs a '{reg}' (vehicle registration) which is present in the data base")
def input_text_in_search_box(context, reg):
    """
    Step to input a vehicle registration, which is present in the data base, into the search box
    :param context:
    :return:
    """
    context.webdriver = driver.find_element_by_id('vehicleReg')
    context.webdriver.send_keys(reg)

@when("selects the search button")
def select_search_button(context):
    """
    Step to click on the search button present
    :param context:
    :return:
    """
    context.webdriver = driver.find_element_by_tag_name('button')
    try:
        context.webdriver.click()
    except (NoSuchElementException, ElementNotInteractableException):
        time.sleep(5)


@then("the web page should present 'sorry record not found'")
def verify_error_message(context):
    """
    Step to verify a 'Sorry not found' error message is presented
    :param context:
    :return:
    """
    # Verify the error message section has loaded
    try:
        WebDriverWait(context.webdriver, 3).until(EC.presence_of_element_located((By.CLASS_NAME, 'result')))
        print
        "Page is ready!"
    except TimeoutException:
        print
        "Loading took too much time!"

    context.webdriver = driver.find_element_by_class_name('result')
    # Verify correct error message presented
    try:
        assert "Sorry record not found" == context.webdriver.text
    except ArithmeticError as e:
        print('FAIL')

@then("the web page should present Result for: '{reg}'")
def verify_error_message(context, reg):
    """
    Step to verify a 'Result for "reg"' message is presented
    :param context:
    :return:
    """
    # Verify the result section has loaded
    try:
        WebDriverWait(context.webdriver, 3).until(EC.presence_of_element_located((By.CLASS_NAME, 'result')))
        print
        "Page is ready!"
    except TimeoutException:
        print
        "Loading took too much time!"

    context.webdriver = driver.find_element_by_class_name('result')
    # Verify the text is presented with the correct reg matching the feature file
    try:
        assert "Result for : %s" % reg == context.webdriver.text
    except ArithmeticError as e:
        print('FAIL')

@then("the start and end date of the cover, START: '{start}' END: '{end}'")
def verify_start_and_end_date_of_cover(context, start, end):
    """
    Step to verify the start and end date of the vehicles cover is presented correctly
    :param context:
    :return:
    """
    # Verify start and end date section has loaded
    try:
        WebDriverWait(context.webdriver, 3).until(EC.presence_of_element_located((By.CLASS_NAME, 'resultDate-bold')))
        print
        "Page is ready!"
    except TimeoutException:
        print
        "Loading took too much time!"

    context.webdriver = driver.find_elements_by_xpath("//span[@class='resultDate']")

    # The following code iterates through the dates presented verifying the start and end matches the feature file
    try:
        for i in context.webdriver:
            if i.text == start:
                continue
            if i.text == end:
                break
    except ArithmeticError as e:
        print('FAIL')