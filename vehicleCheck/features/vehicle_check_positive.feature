Feature: Vehicle check is Successful

Scenario: User is able to search cover of a vehicle by inputting a vehicles registration

    Given I open the url in a web browser
    And the home page has loaded
    When the user inputs a 'OV12UYY' (vehicle registration) which is present in the data base
    And selects the search button
    Then the web page should present Result for: 'OV12UYY'
    And the start and end date of the cover, START: '09 FEB 2022 : 16 : 26' END: '18 FEB 2022 : 23 : 59'