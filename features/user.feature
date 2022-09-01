Feature: Handle storing, retrieving and deleting customer details # test/features/user.feature:1

  Scenario: Retrieve a customers details
    Given some users are in the system
    When I retrieve the customer 'jasonb'
    Then I should get a '200' response
    And the following user details are returned:
      | name        |
      | Jason Borne |

  Scenario: Add a new user
    Given the user "freddy" doesn't exist
    When I receive a POST request on '/users' with the username "freddy"
    Then the user "freddy" should be added
    And I should get a '201' response
