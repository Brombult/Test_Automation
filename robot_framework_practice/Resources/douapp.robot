*** Settings ***
Documentation  Keyword file for Dou tests
Resource  PO/main.robot
Resource  PO/results.robot
Resource  PO/forum.robot
Resource  PO/feed.robot
Resource  PO/salaries.robot
Resource  PO/jobs.robot
Resource  PO/calendar.robot

*** Variables ***
${FORUM_ADMIN_TELEGRAM} =   Telegram-канал для IT-спільноти Києва
${CALENDAR_PAGE_HEADER} =  class:page-head

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
    Click on "Feed" link
Verify list of special projects in Special Project section
    [Arguments]  @{projects_list}
    Verify projects  @{projects_list}
Go to Salaries
    Click on "Salaries" Link
Pick QA Job Title
    [Arguments]  ${job_title}
    Select Job Title By Text   ${job_title}
Pick QA Specialization
    [Arguments]  ${qa_spec}
    Select Specialisation By Text  ${qa_spec}
Verify Minimum Salary
    [Arguments]  ${min_salary}
    Verify Min Salary  ${min_salary}
Go to Jobs
    Click On "Jobs" Link
Select Job Category Via Dropdown
    [Arguments]  ${category_name}
    Select Job Category Via Dropdown By Text  ${category_name}
Verify That Corresponding Job Category Is Open
    [Arguments]  ${category_name}
    Verify Chosen Job Category  ${category_name}
Go To Calendar
    Click on "Calendar" link
Choose A City For Events Using Dropdown
    [Arguments]  ${city_name}
    Select Sity By Text  ${city_name}
Choose A Topic For Events Using Dropdown
    [Arguments]  ${topic_name}
    Select Topic By Text  ${topic_name}
Verify That City And Topic Are Present In The Page Header
    [Arguments]  ${city_name}  ${topic_name}
    element should contain  ${CALENDAR_PAGE_HEADER}  ${city_name}  ignore_case=True
    element should contain  ${CALENDAR_PAGE_HEADER}  ${topic_name}  ignore_case=True