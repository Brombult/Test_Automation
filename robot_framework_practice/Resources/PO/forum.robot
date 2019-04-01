*** Settings ***
Documentation  Dou Forum PO
Library  SeleniumLibrary

*** Variables ***
${TOPIC_SELECTOR} =     name:topic
${FORUM_LINK} =         https://dou.ua/forums/

*** Keywords ***
Load Forum
    go to  ${FORUM_LINK}
Choose Topic By Index
    [Arguments]  ${index}
    select from list by index  ${TOPIC_SELECTOR}  ${index}
Choose Topic By Value
    [Arguments]  ${value}
    select from list by value  ${TOPIC_SELECTOR}  ${value}