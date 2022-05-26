from pprint import pprint
import instagram_scraper

if __name__ == '__main__':
    args = {"login_user": "test.account0916", "login_pass": "dbdudwns"}
    insta_scraper = instagram_scraper.InstagramScraper(**args)
    insta_scraper.authenticate_with_login()
    shared_data = insta_scraper.get_shared_data_userinfo(username='thefreshmanclub_purdue')
    
    arr = []
    
    for item in insta_scraper.query_media_gen(shared_data):
        arr.append(item)

    pprint(arr)