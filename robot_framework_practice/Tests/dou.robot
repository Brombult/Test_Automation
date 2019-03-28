*** Settings ***
Documentation  This is some basic info about the whole suite
Library  SeleniumLibrary
Library  SeleniumLibrary
Test Setup  Begin Web Test
Test Teardown  End Web Test

*** Variables ***
${BROWSER}  chrome
${COMPANY_NAME}  dou

*** Test Cases ***
Search for company
    [Documentation]  Visit Dou, then search company from main page, then verify that company is found
    [Tags]  Smoke
    Open Dou
    Search For A Company
    Verify That Company Name Is In Search Results

*** Keywords ***
Begin Web Test
    open browser  about:blank  ${BROWSER}
Open Dou
    go to  https://dou.ua/
Search For A Company
    press keys  id:txtGlobalSearch  ${COMPANY_NAME}  RETURN
Verify That Company Name Is In Search Results
    element should contain  class:gs-title  ${COMPANY_NAME}  ignore_case=True
End Web Test
    close browser
