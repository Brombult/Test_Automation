*** Settings ***
Documentation  Dou Smoke Test
Resource  ../Resources/common.robot
Resource  ../Resources/douapp.robot
Suite Setup  Begin Web Test  ${BROWSER}
Suite Teardown  End Web Test

*** Variables ***
${BROWSER} =  chrome
${COMPANY} =  dou

*** Test Cases ***
Search for company
    [Documentation]  Visit Dou, then search company from main page, then verify that company is found
    [Tags]  Smoke
    Open Dou
    Search For A Company    ${COMPANY}
    Verify That Company Name Is In Search Results   ${COMPANY}

Search For Company that doesn't exists
    [Documentation]  Visit Dou, then search non-existent company, then verify that company is not found
    [Tags]  Smoke
    Open Dou
    Search For Non-existent Company
    Verify That Nothing Is Found In Search Results

Forum's topic selector should work
    [Documentation]  Visit Dou, click on "Forum" link, choose first option in topic selector, verify that page changed
    [Tags]  Smoke
    Open Dou
    Go to Forum
    Choose "Site Administration" option in topic selector
    Verify that "Site Administarion" topic is chosen