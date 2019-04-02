*** Settings ***
Documentation  Dou Smoke Test
Resource  ../Resources/common.robot
Resource  ../Resources/douapp.robot
Suite Setup  Begin Web Test  ${BROWSER}
Suite Teardown  End Web Test

*** Variables ***
${BROWSER} =  chrome
${COMPANY} =  dou
@{SPECIAL_PROJECTS_LIST} =  DOU Ревизор  DOU Проектор  DOU Labs  DOU Books
${JOB_TITLE} =  QA engineer
${SPECIALIZATION} =  Automation QA
${MIN_SALARY} =  1500

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

Forum's Topic Selector Should Work
    [Documentation]  Visit Dou, click on "Forum" link, choose first option in topic selector, verify that page changed
    [Tags]  Smoke
    Open Dou
    Go to Forum
    Choose "Site Administration" option in topic selector
    Verify that "Site Administarion" topic is chosen

Verify Projects in Feed's Special Project Sections
    [Documentation]  Visit Dou, click on "Feed" link, verify projects in "Special Projects" section
    [Tags]  Smoke
    Open Dou
    Go to Feed
    Verify list of special projects in Special Project section  @{SPECIAL_PROJECTS_LIST}

Verify That Salaty Widged Is Working in "Salaries" tab
    [Documentation]  Visit Dou, click on "Salaries" link, use salaries widget to display salary
    [Tags]  Smoke
    Open Dou
    Go to Salaries
    Pick QA Job Title  ${JOB_TITLE}
    Pick QA Specialization  ${SPECIALIZATION}
    Verify Minimum Salary  ${MIN_SALARY}