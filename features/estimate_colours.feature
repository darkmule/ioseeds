Feature: Estimate the percentage of a colour in an image file

Scenario: Return the percentage of green pixels in a fully green image
    Given I have a image that is entirely green
    When the image is analysed 
    Then the result should be 100 percent green

Scenario Outline: Return percentages of green in a variety of images
    Given I have a list of image files
    When a "<file>" from the list is analysed
    Then the correct percentages of green are returned

    Examples: files list
        |file                   |
        |source/green.png       |
        |source/tray.jpg        |
        |source/fifty.png       |

    



    