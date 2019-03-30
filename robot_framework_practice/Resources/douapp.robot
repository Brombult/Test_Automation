*** Settings ***
Documentation  Keyword file for Dou tests
Resource  PO/main.robot
Resource  PO/results.robot

*** Keywords ***
Open Dou
    Load
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
