# The Daily Script [Movie Scripts Downloader]

### Source Website Link:
      http://www.dailyscript.com/movie.html

      http://www.dailyscript.com/movie_n-z.html

### Functions:
__saveFile()__ : It is downloading any files (.html, .txt, .pdf, .RTF, .doc etc)

__sleepRandom__ : Set random delay in between 1 to 3 seconds

### Download Folder:

> Files are stored into *ScriptsDL* Folder

### Command to run the spider:

````
scrapy crawl movieScript
````

### Folder structure:
````
.
├── README.md
├── ScriptsDL
│   ├── 13\ Days.html
│   ├── Aliens.pdf
│   └── Amadeus.txt
├── dailyscript
│   ├── __init__.py
│   ├── items.py
│   ├── middlewares.py
│   ├── pipelines.py
│   ├── settings.py
│   └── spiders
│       ├── __init__.py
│       └── movieScript.py
└── scrapy.cfg

3 directories, 17 files
````
### To do:
1. Work on log capturing and analyze entire performance
2. Work redirection
3. Export related info [name, link, etc] to a csv file
