Feature: Logging messages

    Scenario Outline: Logging to standard out
        Given I have a "<message>" of type , "<level>" to log
        When the message is sent to standard output
        Then message is routed to the correct location
        And the message has the correct logging level
        And the message has the correct datetime stamp

        Examples: Messages to log
        |   level   |   message                         |
        |   info    |   Here is some infomation to log  |
        |   warning |   Here is a warning               |
        |   error   |   Here is an error                |

