*** Settings ***
Library  SeleniumLibrary

*** Keywords ***
Common.Begin Web Test
    [Arguments]  ${browser}
    open browser  about:blank  ${browser}
Common.End Web Test
    close browser