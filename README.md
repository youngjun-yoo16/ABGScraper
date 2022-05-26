# ABGScraper
## A scraper for finding ABGs in San Francisco, California, Bay Area
By the time many college freshmen arrive on campus this fall, they’ll have already met their roommate, their core friends, and many of their classmates on Instagram. They’re connecting through class accounts, Instagram pages set up by one or several incoming members of a college’s freshman class to help everyone meet before the school year officially starts. <br> <br>
I developed this scraper with a simple Python script so that I can quickly find Instagram accounts of Asian Baby Girls (ABGs) from California, bay area without having to go through every post on `thefreshmanclub_purdue` a class account for Purdue. 

## Functionality
By running the script, a CSV file containing columns - Post Caption, Post Date, Post URL, Mentions in Captions, and Tagged Users - will be generated in the following order. If I see a female-ish name introducing themselves in the post caption, I can instantly send friend request to them by referring to the "Tagged Users" column.

## Requirements
```
#1. Python3
Make sure Python3 is installed and check its version by python -V 

#2. Requirements
pip install -r requirements.txt
```

## How to run
```
#1. Clone the repository 
git clone https://github.com/youngjun-yoo16/ABGScraper.git

#2. Run the script
python3 app.py
```
