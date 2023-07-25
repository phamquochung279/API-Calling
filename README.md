# API-Data-Extraction

<p align="center">
  <img src="https://d33wubrfki0l68.cloudfront.net/868dca64c9bf719cc113ee151faa2dae77be128b/71196/static/f825d8a6a4a9d7ee7ec139fbb191d661/12fd3/entity-extraction-api-thumbnail.png" alt="BikeStore" width=70%" height="400">
</p>

## Introduction

After finishing the [Python for Everybody Specialization course on Coursera](https://www.coursera.org/specializations/python) (instructed by [Dr. Charles Russell Severance](https://www.dr-chuck.com/) from University of Michigan), inspired by the Worked Exercises presented by Dr. Chuck throughout the course, I decided to create my first ever Python project to put my Python skills to the test. <br />

## Problem Statement

TBD <br />

## Tools Used

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) <br />
-  <br />
-  <br />
- <br />

![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white) <br />
-  <br />
-  <br />
- <br />

![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white) & ![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white) <br />
-  <br />
-  <br />
- <br />

## Installation
- Install Python 3.11, DB Browser for SQLite 3.12.2, and any code editor of choice (mine is Visual Studio Code). <br />
- First, run [API_call.py](https://github.com/phamquochung279/API-Data-Extraction/blob/main/API_call.py) the file to extract all game data from freetogame.com's API that matches your criteria.<br />
***Note:*** Add any query parameters you want in function **urllib.parse.urlencode()** on line 7 (see freetogame.com's API doc [here](https://www.freetogame.com/api-doc)). In case you don't want blow up freetogame.com's API with your repeated requests, the file [games.json](https://github.com/phamquochung279/API-Data-Extraction/blob/main/games.json) has freetogame.com's full Live games list (retrieved from endpoint [https://www.freetogame.com/api/games](https://www.freetogame.com/api/games)) as of July 24th, 2023.<br />
- After extraction is completed, run [DB_fill.py](https://github.com/phamquochung279/API-Data-Extraction/blob/main/DB_fill.py) to create a SQLite database and insert all extracted data into it.<br />
***Note:*** You can change the name of the SQLite database to be created/connected to on line 6 - parameter of **sqlite3.connect()** function.<br />
- Then, run [display_results.py](https://github.com/phamquochung279/API-Data-Extraction/blob/main/Display_results.py) and enter your SQL query. If the query is valid (i.e. a SELECT statement that returns results), you will be asked to name an HTML file (either new or existing) to store your result set. Enter a name and the HTML file shall be generated.<br />
***Note:*** Didn't put too much work on the front-end, so please excuse my horrible UI. You can customize how your webpage looks in [styles.css](https://github.com/phamquochung279/API-Data-Extraction/blob/main/styles.css).<br />
- Finally, open the HTML file with a browser to see your results!<br />

## Contact

Author: Pham Quoc Hung <br />

<a href="mailto:pham.quochung0999@gmail.com">![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)</a> <a href="https://public.tableau.com/app/profile/hung.pham279">![Tableau](https://img.shields.io/badge/Tableau-E97627?style=for-the-badge&logo=Tableau&logoColor=white)</a> <a href="https://github.com/phamquochung279">![Github](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)</a> <a href="https://www.linkedin.com/in/pham-quochung/">![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)</a>

## Special thanks to:

- Dr. Chuck and his program - Python for Everybody.
- freetogame.com for their beautiful, free-to-use API.