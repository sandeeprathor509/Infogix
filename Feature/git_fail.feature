Feature: Infogix Coding Test
  Scenario: Git verify login button
    Given Launch the git page
    Then User will be navigate to the login page
    Then Verify the username and password field mandatory fields
    Then Close the browser

  Scenario: Git verify resent password functionaltiy
    Given Launch the git page
    Then  User will be navigate to the login page
    Then Click on forgot password
    Then Enter the m.ie in the username field
    Then verify the text after entering the wrong email
    Then Verify the text after entering nothing in email
    Then Close the browser

  Scenario: Verify the Signup functionality
    Given Launch the git page
    Then Click on the signup button
    Then Verify the Join GitHub text on the signup page
    Then Verify the presence Create account button
    Then Close the browser