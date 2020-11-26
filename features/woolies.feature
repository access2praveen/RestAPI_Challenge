Feature: Good day to Surf
  Scenario Outline: As a choosey surfer
    Given I like to surf in any 2 beaches "<Out of top ten>" of Sydney
    And I only like to surf on any 2 days specifically "<Thursday & Friday>" in next "16" Days
    When I look up the the weather forecast for the next 16 days using "<postcode>"
    Then I check to if see the temperature is between "<20℃ and 30℃>"
    And I check to see if UV index is <= "20"
    And I Pick two spots based on suitable weather forecast for the day
   Examples: Top Ten Beaches
     | Out of top ten   |   postcode    |
     | Bondi            |   2026        |
     | Manly            |   2095        |
     | Clovelly         |   2031        |
     | Coogee           |   2034        |
     | Bronte           |   2024        |
     | Shelly           |   2261        |
     | Balmoral         |   2088        |
     | Nielsen Park     |   2030        |
     | Milk             |   2030        |
     | Bilgola          |   2107        |


