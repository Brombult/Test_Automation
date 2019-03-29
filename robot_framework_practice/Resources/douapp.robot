*** Settings ***
Documentation  Keyword file for Dou tests
Resource  PO/main.robot
Resource  PO/results.robot
*** Variables ***


*** Keywords ***
Dou.Open Dou
    Main.Load
Dou.Search For A Company
    [Arguments]  ${text}
    Main.Type Text in Search  ${text}
    Main.Press Submit in Search
Dou.Search For Non-existent Company
    [Arguments]  ${text}
    Main.Type Text in Search  ${text}
    Main.Press Submit in Search
Dou.Verify That Company Name Is In Search Results
    [Arguments]  ${text}
    SearchResults.Verify Company Name Is Present  ${text}
Dou.Verify That Nothing Is Found In Search Results
    SearchResults.Verify Nothing Is Found
