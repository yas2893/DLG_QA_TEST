Feature: Vehicle check is Unsuccessful

Scenario: User is notified that the vehicle is not present in the database by inputting a vehicles registration which has no cover

    Given I open the url in a web browser
    And the home page has loaded
    When the user inputs a 'HB12CYC' (vehicle registration) which is not present in the data base
    And selects the search button
    Then the web page should present 'sorry record not found'