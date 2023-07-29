# ETL Data from API to Database

<p align="center">
  <img src="https://d33wubrfki0l68.cloudfront.net/868dca64c9bf719cc113ee151faa2dae77be128b/71196/static/f825d8a6a4a9d7ee7ec139fbb191d661/12fd3/entity-extraction-api-thumbnail.png" alt="BikeStore" width=100%" height="400">
</p>

## Introduction

After finishing the [Python for Everybody Specialization course on Coursera](https://www.coursera.org/specializations/python) (instructed by [Dr. Charles Russell Severance](https://www.dr-chuck.com/) from University of Michigan), I decided to work on my first ETL project to put my Python skills to the test. Among the free public APIs on the market I've seen, freetogame.com API is argubly one of the best - has detailed data of ~400 games, 100% free access to all endpoints, no authorization required, extremely generous rate limit (4 requests PER SECOND - who even needs that many?). A pitch-perfect API for beginner-level coding projects. <br />

TL;DR: This is a Python app that extracts, transforms, and loads data from freetogame.com API to your database. <br />

## Technologies Used

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) <br />
- Extract game data from freetogame.com API <br />
- Create a relational database to store extracted data. <br />
- Allow users to see their query results on a webpage. <br />

![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white) <br />
- My choice of database engine in this project - easy to install, easy to use. <br />
- Create table relationships and constraints. <br />

![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white) & ![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white) <br />
- Showcase users' query results on an HTML webpage with some simple CSS styles. <br />
- ***Disclaimer:*** HTML and CSS are outside of Python for Everybody's scope, I just wanted to do some experiments with them. <br />

## How To Use
1. Install [Python 3.11](https://www.python.org/downloads/), [DB Browser for SQLite 3.12.2](https://sqlitebrowser.org/dl/), and optionally any code editor you prefer (mine is [Visual Studio Code](https://code.visualstudio.com/)). <br />
2. First, run [API_call.py](https://github.com/phamquochung279/API-Data-Extraction/blob/main/API_call.py) the file to extract all game data from freetogame.com API that matches your criteria.<br />
3. After extraction is completed, run [DB_fill.py](https://github.com/phamquochung279/API-Data-Extraction/blob/main/DB_fill.py) to create a SQLite database and insert all extracted data into it.<br />
4. Then, run [display_results.py](https://github.com/phamquochung279/API-Data-Extraction/blob/main/Display_results.py) and enter your SQL query. If the query is valid (i.e. a SELECT statement that returns results), you will be asked to name an HTML file (either new or existing) to store your result set. Enter a name and the HTML file shall be generated.<br />
5. Finally, open the HTML file with a browser to see your results!<br />

***Note:***
- In [API_call.py](https://github.com/phamquochung279/API-Data-Extraction/blob/main/API_call.py): Add any query parameters to line 7 - function **urllib.parse.urlencode()**'s parameters (see freetogame.com's API doc [here](https://www.freetogame.com/api-doc) for available query parameters) <br />
- If you don't want to blow up freetogame.com's API with repeated requests, the file [games.json](https://github.com/phamquochung279/freetogame.com-API-ETL/blob/main/games.json) has freetogame.com's full Live games list (retrieved from endpoint [https://www.freetogame.com/api/games](https://www.freetogame.com/api/games)) as of July 24th, 2023.<br />
- In [DB_fill.py](https://github.com/phamquochung279/API-Data-Extraction/blob/main/DB_fill.py): You can change the database name to be created/connected to on line 6 - 1st parameter of **sqlite3.connect()** function.<br />
- Please excuse my pathetic effort in the HTML file's styles, feel free to customize them in [styles.css](https://github.com/phamquochung279/API-Data-Extraction/blob/main/styles.css). <br />
- Fun fact: [project_presentation.pdf](https://github.com/phamquochung279/freetogame.com-API-ETL/blob/main/project_presentation.pdf) is the actual slide deck that I used for this project's presentation to my colleagues at Got It Inc., check it out if you're interested! <br />

## Special thanks to:

- Dr. Chuck and his Python for Everybody program - one of the best programming courses for newbies in tech.
- freetogame.com for their wonderful, free-to-use API.

## Contact

Author: Pham Quoc Hung <br />

<a href="mailto:pham.quochung0999@gmail.com">![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)</a> <a href="https://public.tableau.com/app/profile/hung.pham279">![Tableau](https://img.shields.io/badge/Tableau-E97627?style=for-the-badge&logo=Tableau&logoColor=white)</a> <a href="https://github.com/phamquochung279">![Github](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)</a> <a href="https://www.linkedin.com/in/pham-quochung/">![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)</a>

