*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${BROWSER}  chrome

*** Keywords ***
Common.Begin Web Test
    open browser  about:blank  ${BROWSER}
Common.End Web Test
    close browser