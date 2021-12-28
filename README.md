# SmartReviewTool

[![GitHub stars](https://img.shields.io/github/stars/rameshbabuvfx/smart_review_tool)](https://github.com/rameshbabuvfx/smart_review_tool/stargazers) ![GitHub release](https://img.shields.io/badge/python-3.7+-green) ![GitHub release (latest by date)](https://img.shields.io/badge/nuke-11.0+-yellow)


SmartReviewTool is a Markup/Annotaion tool for nuke. This tool helps the artist/reviewers to do markups on image.

This tool has lot of features :

* Drawing lines.
* Adding text.
* Erasing drawn lines.
* Change Font Style/Size etc.

![smart_review_tool](https://user-images.githubusercontent.com/73053972/138094526-6b44b660-5065-4c57-80d7-c1d34964606b.png)

## How to use

* The Smart Review tool has been added to the pane menu.
* To start the tool, click the SmartReview menu option.
* Import image pick the color for pen and draw on image
* Click on `Eraser` icon to enable eraser to remove the drawn lines on image.
* Click on `Add Text` button to add text on image.
* Add color to the text and set the color aswell.
* To delete the text, press the 'Del' key.
* `Double Click` on the text layer to add text on image.
* To `Save` image click save button.



## Installation

* Clone the [smart_review_tool](https://github.com/rameshbabuvfx/smart_review_tool.git) git repo in any location or `.nuke` folder.

```
https://github.com/rameshbabuvfx/smart_review_tool.git
```

* Copy the smart_review_tool folder path.
* Open `init.py` python file from `.nuke` or nuke plugin folder
* add this line of code in init.py file.

```
nuke.pluginAddPath("C:/Users/username/.nuke/smart_review_tool")
```

* Launch/Restart Nuke.



