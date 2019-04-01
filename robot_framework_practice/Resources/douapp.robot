*** Settings ***
Documentation  Keyword file for Dou tests
Resource  PO/main.robot
Resource  PO/results.robot
Resource  PO/forum.robot

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