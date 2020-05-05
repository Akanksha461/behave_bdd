Feature: Caribu Web Browsing
  As a web surfer,
  I want to find information online,
  So I can learn new things and get tasks done.


  Background:
    Given the Caribu home page is displayed


  Scenario: redirection to sign-in page
    When the user Clicks on sign-in page
    Then user should be redirected to the sign-in page