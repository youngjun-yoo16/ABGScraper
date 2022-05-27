# ABGScraper
## A scraper for finding ABGs from San Francisco, California, Bay Area
By the time many college freshmen arrive on campus this fall, they’ll have already met their roommate, their core friends, and many of their classmates on Instagram. They’re connecting through class accounts, Instagram pages set up by one or several incoming members of a college’s freshman class to help everyone meet before the school year officially starts. These accounts typically feature user-submitted photos and paragraph-long biographies of incoming students, often including their intended major, whether they’re looking for a roommate, and their personal Instagram handle. <br><br>
I developed this scraper with a simple Python script that scans through every post in a class acount searching for those posts that contain specific user-inputted keywords in the post caption. This way, you can quickly find Instagram accounts of Asian Baby Girls (ABGs) from California, Bay Area without having to manually go through every post on `thefreshmanclub_purdue`, a class account for Purdue. 

## Functionality
By running the script, a CSV file containing columns - `Post Caption`, `Post Date`, `Post URL`, `Mentions in Captions`, and `Tagged Users` in the following order - will be generated under the same folder with the repository. If you see a female-ish name introducing themselves in the post caption, you can instantly send friend request to them by referring to the `Tagged Users` column. <br><br>
![filtered_1](https://github.com/youngjun-yoo16/ABGScraper/blob/main/img/filtered_2.png?raw=true) <br><br>
Moreover, you can freely enter the username of the class acount of your respective college as a command line input whenever it asks you to enter the username of the account which you want to scrap. By this, you can find incoming ABGs from your respective college. As of now, location keywords are initially setted to San Francisco, California, Bay Area and major keywords are setted to find Computer Science and Data Science majors. I plan to make this a more versatile feature by allowing users to set their own location and major keywords for filtering posts.

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
## Further improvements
- Allow users to enter their own specific keywords for which they want to filter.
- Make it into a fully functional web application for the ease of access.
- Allow users to set specific time period for filtering posts based on the post date.
