# Created by thesu at 5/30/2024
Feature: Reelly exploratory test
  # Enter feature description here

  Scenario: User can filter by sale status High Demand
    Given Open the webpage
    When Enter login email
    When Enter login password
    When click continue
    When click off plan
    When Verify correct page is open
    When click on filter icon
    When click on high demand
    Then verify high demand