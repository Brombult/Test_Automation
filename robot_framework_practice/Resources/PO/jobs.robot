*** Settings ***
Documentation  Dou Jobs Page PO
Library  SeleniumLibrary

*** Variables ***
${JOBS_LINK} =  https://jobs.dou.ua/
${JOB_CATEGORY_DROPDOWN} =  css:select[name='category']
${JOB_VACANCIES_HEADER} =  class:b-inner-page-header

*** Keywords ***
Load Jobs Page
    go to  ${JOBS_LINK}
Select Job Category Via Dropdown By Text
    [Arguments]  ${category_name}
    select from list by label  ${JOB_CATEGORY_DROPDOWN}  ${category_name}
Verify Chosen Job Category
    [Arguments]  ${category_name}
    element should contain  ${JOB_VACANCIES_HEADER}  ${category_name}