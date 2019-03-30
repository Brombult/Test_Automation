*** Settings ***
Documentation  Dou Main Page PO
Library  SeleniumLibrary

*** Variables ***
${DOU_LINK} =           https://dou.ua/
${MAIN_SEARCH_BAR} =    id:txtGlobalSearch

*** Keywords ***
Main.Load
    go to  ${DOU_LINK}
Main.Verify Page loaded
    page should contain link  ${DOU_LINK}
Main.Type Text in Search
    [Arguments]  ${text}
    input text  ${MAIN_SEARCH_BAR}  ${text}
Main.Press Submit in Search
    press keys  ${MAIN_SEARCH_BAR}  RETURN