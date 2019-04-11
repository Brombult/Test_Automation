*** Settings ***
Documentation  DOU Feed PO
Library  SeleniumLibrary

*** Variables ***
${FEED_LINK} =   https://dou.ua/lenta/
${SPECIAL_PROJECTS_LOCATOR} =  css:.col18.m-hide

*** Keywords ***
Load Feed Page
    go to  ${FEED_LINK}

Verify projects
    [Arguments]  @{project_list}
    :FOR    ${project}  IN  @{project_list}
    \   element should contain  ${SPECIAL_PROJECTS_LOCATOR}  ${project}