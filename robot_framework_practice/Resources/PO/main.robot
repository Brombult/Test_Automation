*** Settings ***
Documentation  Dou Main Page PO
Library  SeleniumLibrary

*** Variables ***
${DOU_LINK} =           https://dou.ua/
${MAIN_SEARCH_BAR} =    id:txtGlobalSearch

*** Keywords ***
Load Main Page
    go to  ${DOU_LINK}

Verify That Main Page Is Loaded
    page should contain link  ${DOU_LINK}

Type Text in Search
    [Arguments]   ${company_name}
    input text  ${MAIN_SEARCH_BAR}  ${company_name}

Press Submit in Search
    press keys  ${MAIN_SEARCH_BAR}  RETURN

Click on "Forum" link
    click link  ${FORUM_LINK}

Click on "Feed" link
    click link  ${FEED_LINK}

Click on "Salaries" Link
    click link  ${SALARIES_LINK}

Click on "Jobs" Link
    click link  ${JOBS_LINK}

Click on "Calendar" link
    click link  ${CALENDAR_LINK}