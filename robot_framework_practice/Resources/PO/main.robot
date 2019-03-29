*** Settings ***
Documentation  Dou Main Page PO
Library  SeleniumLibrary

*** Variables ***

*** Keywords ***
Main.Load
    go to  https://dou.ua/
Main.Verify Page loaded
    page should contain link  https://dou.ua/
Main.Type Text in Search
    [Arguments]  ${text}
    input text  id:txtGlobalSearch  ${text}
Main.Press Submit in Search
    press keys  id:txtGlobalSearch  RETURN