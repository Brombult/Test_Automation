*** Settings ***
Documentation  Dou Salaries PO
Library  SeleniumLibrary

*** Variables ***
${SALARIES_LINK} =  https://jobs.dou.ua/salaries/
${JOB_TITLE_SELECTOR} =  class:salarydec-field-title
${QA_SPECIALISATION_SELECTOR} =  css:div.salarydec-field_spec>select
${MIN_SALARY_SELECTOR} =  css:dd.salarydec-results-min>span

*** Keywords ***
Load Salaries Page
    go to  ${SALARIES_LINK}
Select Job Title By Text
    [Arguments]  ${job_title}
    select from list by label  ${JOB_TITLE_SELECTOR}  ${job_title}
Select Specialisation By Text
    [Arguments]  ${qa_spec}
    select from list by label  ${QA_SPECIALISATION_SELECTOR}  ${qa_spec}
Verify Min Salary
    [Arguments]  ${min_salary}
    wait until element contains  ${MIN_SALARY_SELECTOR}  ${min_salary}  2
    element text should be  ${MIN_SALARY_SELECTOR}  ${min_salary}