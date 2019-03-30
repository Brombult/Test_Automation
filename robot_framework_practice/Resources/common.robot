*** Settings ***
Library  SeleniumLibrary

*** Keywords ***
Begin Web Test
    [Arguments]  ${browser}
    open browser  about:blank  ${browser}
End Web Test
    close browser