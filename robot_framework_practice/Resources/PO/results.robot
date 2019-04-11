*** Settings ***
Documentation  Search Results Page PO
Library  SeleniumLibrary

*** Variables ***
${SEARCH_RESULTS} =        class:gs-title
${SEARCH_RESULTS_EMPTY} =  class:gs-no-results-result

*** Keywords ***
Verify Company Name Is Present
    [Arguments]  ${company_name}
    element should contain  ${SEARCH_RESULTS}  ${company_name}   ignore_case=True

Verify Nothing Is Found
    page should contain element  ${SEARCH_RESULTS_EMPTY}