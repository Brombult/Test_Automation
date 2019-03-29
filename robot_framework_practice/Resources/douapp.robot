*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${COMPANY_NAME}  dou

*** Keywords ***
Dou.Open Dou
    go to  https://dou.ua/
Dou.Search For A Company
    press keys  id:txtGlobalSearch  ${COMPANY_NAME}  RETURN
Dou.Search For Non-existent Company
    press keys  id:txtGlobalSearch  ahsjhsahchjkxzcjh  RETURN
Dou.Verify That Company Name Is In Search Results
    element should contain  class:gs-title  ${COMPANY_NAME}  ignore_case=True
Dou.Verify That Nothing Is Found In Search Results
    page should contain element  class:gs-no-results-result
