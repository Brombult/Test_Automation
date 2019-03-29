*** Settings ***
Documentation  Dou Smoke Test
Resource  ../Resources/common.robot
Resource  ../Resources/douapp.robot
Test Setup  Common.Begin Web Test  ${BROWSER}
Test Teardown  Common.End Web Test

*** Variables ***
${BROWSER} =  chrome
${COMPANY} =  dou

*** Test Cases ***
Search for company
    [Documentation]  Visit Dou, then search company from main page, then verify that company is found
    [Tags]  Smoke
    Dou.Open Dou
    Dou.Search For A Company  ${COMPANY}
    Dou.Verify That Company Name Is In Search Results  ${COMPANY}

Search For Company that doesn't exists
    [Documentation]  Visit Dou, then search non-existent company, then verify that company is not found
    [Tags]  Smoke
    Dou.Open Dou
    Dou.Search For Non-existent Company  sdsfdvdfbvc
    Dou.Verify That Nothing Is Found In Search Results
