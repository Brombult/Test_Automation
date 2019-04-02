*** Settings ***
Documentation  Keyword file for Dou tests
Resource  PO/main.robot
Resource  PO/results.robot
Resource  PO/forum.robot
Resource  PO/feed.robot
Resource  PO/salaries.robot

*** Variables ***
${FORUM_ADMIN_TELEGRAM} =   Telegram-канал для IT-спільноти Києва

*** Keywords ***
Open Dou
    Load Main Page
    Verify That Main Page Is Loaded
Search For A Company
    [Arguments]  ${company_name}
    Type Text in Search  ${company_name}
    Press Submit in Search
Search For Non-existent Company
    Type Text in Search  sdsfdvdfbvc
    Press Submit in Search
Verify That Company Name Is In Search Results
    [Arguments]  ${company_name}
    Verify Company Name Is Present  ${company_name}
Verify That Nothing Is Found In Search Results
    Verify Nothing Is Found
Go to Forum
    Click on "Forum" link
Choose "Site Administration" option in topic selector
    Choose Topic By Index  1
Verify that "Site Administarion" topic is chosen
    page should contain  ${FORUM_ADMIN_TELEGRAM}
Go to Feed
    Load Feed Page
Verify list of special projects in Special Project section
    [Arguments]  @{projects_list}
    Verify projects  @{projects_list}
Go to Salaries
    Load Salaries Page
Pick QA Job Title
    [Arguments]  ${job_title}
    Select Job Title By Text   ${job_title}
Pick QA Specialization
    [Arguments]  ${qa_spec}
    Select Specialisation By Text  ${qa_spec}
Verify Minimum Salary
    [Arguments]  ${min_salary}
    Verify Min Salary  ${min_salary}
