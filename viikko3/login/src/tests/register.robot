*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  kallervo
    Set Password  kallervo123
    Set Password Confirmation  kallervo123
    Click Button  Register
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ka
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Click Button  Register
    Register Should Fail With Message  Username must be at least 3 characters

Register With Valid Username And Too Short Password
    Set Username  kalle1
    Set Password  kalle1
    Set Password Confirmation  kalle1
    Click Button  Register
    Register Should Fail With Message  Password must be at least 8 characters

Register With Valid Username And Invalid Password
    Set Username  kalle2
    Set Password  kallekalle
    Set Password Confirmation  kallekalle
    Click Button  Register
    Register Should Fail With Message  Password must not consist of only letters

Register With Nonmatching Password And Password Confirmation
    Set Username  kallervo1
    Set Password  kallervo123
    Set Password Confirmation  kallervo456
    Click Button  Register
    Register Should Fail With Message  Passwords don't match

Register With Username That Is Already In Use
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Click Button  Register
    Register Should Fail With Message  Username already taken


*** Keywords ***

Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page

Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}