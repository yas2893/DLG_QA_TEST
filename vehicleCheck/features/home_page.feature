Feature: Home page should be presented when opening url

Scenario: User is able to navigate to home page successfully

   Given I open the url in a web browser
   When the home page has loaded
   Then I should see a page with VWFS Services as the heading
   And a search box to find a vehicle
