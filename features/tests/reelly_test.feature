# Created by thesu at 5/30/2024
Feature: Reelly exploratory test

  Scenario: User can filter by sale status High Demand
    Given log in to Reelly_io
    When Navigate to High Demand filter
    Then Verify High demand items are displayed
