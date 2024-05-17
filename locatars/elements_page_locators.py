from selenium.webdriver.common.by import By


class TextBoxLocators:
    FULL_NAME = (By.CSS_SELECTOR, 'input[id="userName"]')
    EMAIL = (By.CSS_SELECTOR, 'input[id="userEmail"]')
    CURRENT_ADDRESS = (By.CSS_SELECTOR, 'textarea[id="currentAddress"]')
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, 'textarea[id="permanentAddress"]')
    SUBMIT = (By.CSS_SELECTOR, 'button[id="submit"]')

    #created from

    CREATED_FULL_NAME = (By.CSS_SELECTOR, '#output #name')
    CREATED_EMAIL = (By.CSS_SELECTOR, '#output #email')
    CREATED_CURRENT_ADDRESS = (By.CSS_SELECTOR, '#output #currentAddress')
    CREATED_PERMANENT_ADDRESS = (By.CSS_SELECTOR, '#output #permanentAddress')


#Тут мы ищем "span[class='rct-title']" по списку т.к здесь будет сразу много элементов
class CheckBoxPageLocators:
    EXPAND_ALL_BUTTON = (By.CSS_SELECTOR, 'button[title="Expand all"]')
    ITEM_LIST = (By.CSS_SELECTOR, "span[class='rct-title']")
    CHECKED_ITEMS = (By.CSS_SELECTOR, "svg[class ='rct-icon rct-icon-check']")
    TITLE_ITEM = ".//ancestor::span[@class='rct-text']'"
    OUTPUT_RESULT = (By.CSS_SELECTOR, "span[class='text-success']")


class RadioButtonPageLocators:
    PRESS_RADIO_BUTTON_YES = (By.XPATH, "//label[@for='yesRadio']")
    PRESS_RADIO_BUTTON_IMPRESSIVE = (By.XPATH, "//label[@for='impressiveRadio']")
    OUTPUT_RESULT = (By.CSS_SELECTOR, 'span[class="text-success"]')


class WebTablePageLocators:
    ADD_BUTTON = (By.CSS_SELECTOR, 'button[id="addNewRecordButton"]')
    FIRSTNAME_INPUT = (By.CSS_SELECTOR, 'input[id="firstName"]')
    LASTNAME_INPUT = (By.CSS_SELECTOR, 'input[id="lastName"]')
    EMAIL_INPUT = (By.CSS_SELECTOR, 'input[id="userEmail"]')
    AGE_INPUT = (By.CSS_SELECTOR, 'input[id="age"]')
    SALARY_INPUT = (By.CSS_SELECTOR, 'input[id="salary"]')
    DEPARTMENT_INPUT = (By.CSS_SELECTOR, 'input[id="department"]')
    SUBMIT = (By.CSS_SELECTOR, 'button[id="submit"]')

    #Check table
    FULL_PEOPLE_LIST = (By.CSS_SELECTOR, 'div[class="rt-tr-group"]')

    #Search table add person
    WORD_INPUT = (By.CSS_SELECTOR, 'input[id="searchBox"]')
    DELETE_BUTTON = (By.CSS_SELECTOR, 'span[title="Delete"]')

    #Edit person
    EDIT_PERSON = (By.CSS_SELECTOR, 'span[title="Edit"]')

    #Delete_person
    DELETE_PERSON = (By.CSS_SELECTOR, 'div[class="rt-noData"]')

    #Edit_string
    EDIT_STRING = (By.CSS_SELECTOR, 'select[aria-label="rows per page"]')


class ButtonsPageLocators:
    #Click
    DOUBLE_BUTTON = (By.CSS_SELECTOR, "button[id='doubleClickBtn']")
    CLICK_ME_BUTTON = (By.XPATH, '//button[text()="Click Me"]')

    #Result
    SUCCESS_DOUBLE = (By.XPATH, '//p[@id="doubleClickMessage"]')
    SUCCESS_CLICK_ME = (By.XPATH, '//p[@id="dynamicClickMessage"]')
