*** Settings ***
Documentation  DOU Calendar PO
Library  SeleniumLibrary

*** Variables ***
${CALENDAR_LINK} =   https://dou.ua/calendar/
${CITY_SELECTOR} =   css:select[name='city']
${TOPIC_SELECTOR_CALENDAR} =  css:select[name='tag']

*** Keywords ***
Load Calendar Page
    go to  ${CALENDAR_LINK}
Select Sity By Text
    [Arguments]  ${city_name}
    select from list by label  ${CITY_SELECTOR}  ${city_name}
Select Topic By Text
    [Arguments]  ${topic_name}
    select from list by label  ${TOPIC_SELECTOR_CALENDAR}  ${topic_name}
