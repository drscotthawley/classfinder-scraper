# Classfinder Scraper

### Requirements



#### Mac (tested on macOS 10.15.7 Catalina):

Install ChromeDriver, ssl, and pg_config using HomeBrew

* `brew install chromedriver ssl postgresql`

If applicable, exit any other Python environments (e.g., conda, etc):

* `conda deactivate`

Create a Virtual Env
* `/usr/bin/python3 -m venv venv`
* `source venv/bin/activate`

Install dependencies
* `pip install -r requirements.txt`
* If issues arise with psycopg2 and/or ssl, search StackOverflow for answers (e.g. https://stackoverflow.com/questions/26288042/error-installing-psycopg2-library-not-found-for-lssl) and pip-install psycopg2 manually, then re-run the install for requirements. 

Run

* `python scraper.py`
* If you get an error about chromedriver from MacOs security, run `which chromedriver`, then `ls -l` that on file to see where the alias points to, then follow your [Mac's instructions](https://support.apple.com/guide/mac-help/open-a-mac-app-from-an-unidentified-developer-mh40616/mac) to override security for that executable (Ctrl-click, "Open", etc.) then re-run the scraper. 

Then run

* `python seed_db.py`
* ...and get a page full of Django errors.