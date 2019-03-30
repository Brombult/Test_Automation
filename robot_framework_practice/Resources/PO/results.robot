*** Settings ***
Documentation  Search Results Page PO
Library  SeleniumLibrary

*** Variables ***
${SEARCH_RESULTS} =        class:gs-title
${SEARCH_RESULTS_EMPTY} =  class:gs-no-results-result

*** Keywords ***
SearchResults.Verify Company Name Is Present
    element should contain  ${SEARCH_RESULTS}  ${COMPANY}   ignore_case=True
SearchResults.Verify Nothing Is Found
    page should contain element  ${SEARCH_RESULTS_EMPTY}