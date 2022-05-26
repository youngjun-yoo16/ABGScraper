import instaloader
import csv

class getInstagramProfile():
    def __init__(self) -> None:
        self.bot = instaloader.Instaloader()
    
    def download_users_profile_picture(self, username):
        self.bot.download_profile(username, profile_pic_only = True)
        
    def get_users_followers(self, username):
        '''Note: login required to get a profile's followers.'''
        self.bot.login(input("Input your username: "), input("Input your password: ") ) 
        profile = instaloader.Profile.from_username(self.bot.context, username)
        file = open("follower_names.txt", "a+")
        for follower in profile.get_followers():
            user_name = follower.username
            file.write(username + "\n")
            print(user_name)
    
    def get_users_followings(self, username):
        '''Note: login required to get a profile's followings.'''
        self.bot.login(input("Input your username: "), input("Input your password: ") ) 
        profile = instaloader.Profile.from_username(self.bot.context, username)
        file = open("following_names.txt", "a+")
        for followee in profile.get_followees():
            user_name = followee.username
            file.write(user_name + "\n")
            print(user_name)
            
    def get_post_info_csv(self, filename, username):
        '''Note: login required to get post details.'''
        self.bot.login(input("Input your username: "), input("Input your password: ") ) 
        with open(filename + '.csv', 'w', newline = '', encoding = 'utf-8') as file:
            writer = csv.writer(file)
            posts = instaloader.Profile.from_username(self.bot.context, username).get_posts()
            for post in posts:
                if "bay area" or "California" or "california" or "computer science" or "Computer Science" or "Computer" in str(post.caption) :
                    print("Post date: " + str(post.date))
                    print("Post profile: " + post.profile)
                    print("Post caption: " + post.caption)
                    
                    posturl = "https://www.instagram.com/p/" + post.shortcode
                    print("Post url: " + posturl)
                    writer.writerow(["post", post.caption, post.date, posturl, post.caption_mentions, post.tagged_users])
                    print("\n\n")
                    
if __name__ == '__main__':
    client = getInstagramProfile()
    username = input("Enter the username of the account which you want to scrap: ")
    client.get_post_info_csv("user_info", username)
