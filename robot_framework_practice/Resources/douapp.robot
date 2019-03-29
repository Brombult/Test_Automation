*** Settings ***
Documentation  Keyword file for Dou tests
Resource  PO/main.robot
Resource  PO/results.robot

*** Keywords ***
Dou.Open Dou
    Main.Load
Dou.Search For A Company
    Main.Type Text in Search  ${COMPANY}
    Main.Press Submit in Search
Dou.Search For Non-existent Company
    Main.Type Text in Search  sdsfdvdfbvc
    Main.Press Submit in Search
Dou.Verify That Company Name Is In Search Results
    SearchResults.Verify Company Name Is Present
Dou.Verify That Nothing Is Found In Search Results
    SearchResults.Verify Nothing Is Found
