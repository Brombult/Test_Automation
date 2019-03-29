*** Settings ***
Documentation  Search Results Page PO
Library  SeleniumLibrary

*** Keywords ***
SearchResults.Verify Company Name Is Present
    element should contain  class:gs-title  ${COMPANY}   ignore_case=True
SearchResults.Verify Nothing Is Found
    page should contain element  class:gs-no-results-result