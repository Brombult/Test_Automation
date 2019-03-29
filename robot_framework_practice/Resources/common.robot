*** Settings ***
Library  SeleniumLibrary

*** Keywords ***
Common.Begin Web Test
    open browser  about:blank  ${BROWSER}
Common.End Web Test
    close browser