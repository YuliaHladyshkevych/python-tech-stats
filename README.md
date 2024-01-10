# Djinni technologies statistics

* You can scrap Python Developer vacancies from Djinni website.
* And analyze scraped data to define most popular technologies.

## How to run

```shell
git clonehttps://github.com/YuliaHladyshkevych/python-tech-stats.git
python -m venv venv
source venv/bin/activate # on MacOS
venv\Scripts\activate # on Windows
pip install -r requirements.txt
```

## Getting started

Run scraper from directory, where is spiders directory

```shell
cd scraping
scrapy crawl vacancies -O vacancies.csv
```

Open data_analysis/vacancies.ipynb with Jupyter Notebook and run cells.


Sample of diagram:
![TopTechnologies.png](data_analysis%2Fdiagrams%2FTopTechnologies.png)