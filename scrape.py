import instaloader
import csv

class getInstagramProfile():
    def __init__(self) -> None:
        self.bot = instaloader.instaloader()
    
    def download_users_profile_picture(self, username):
        self.bot.download_profile(username, profile_pic_only=True)
        
    def get_users_followers(self, username):
        '''Note: login required to get a profile's followers.'''
        self.bot.login(input("Input your username: "), input("Input your password: ") ) 
        profile = instaloader.Profile.from_username(self.bot.context, username)
        file = open("follower_names.txt","a+")
        for follower in profile.get_followers():
            user_name = follower.username
            file.write(username + "\n")
            print(user_name)
    
    def get_users_followings(self, username):
        '''Note: login required to get a profile's followings.'''
        self.bot.login(input("input your username: "), input("input your password: ") ) 
        profile = instaloader.Profile.from_username(self.bot.context, username)
        file = open("following_names.txt","a+")
        for followee in profile.get_followees():
            user_name = followee.username
            file.write(user_name + "\n")
            print(user_name)
            
    def get_post_info_csv(self, username):
        with open(username+'.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            posts = instaloader.Profile.from_username(self.L.context, username).get_posts()
            for post in posts:
                print("post date: " + str(post.date))
                print("post profile: " + post.profile)
                print("post caption: " + post.caption)
                print("post location: " + str(post.location))
                
                posturl = "https://www.instagram.com/p/" + post.shortcode
                print("Post url: " + posturl)
                writer.writerow(["post", post.mediaid, post.profile, post.caption, post.date, 
                                 post.location, posturl, post.typename, post.mediacount, post.caption_hashtags, 
                                 post.caption_mentions, post.tagged_users, post.likes, post.comments, post.title,  
                                 post.url])
            
                for comment in post.get_comments():
                    writer.writerow(["comment", comment.id, comment.owner.username,comment.text,comment.created_at_utc])
                    print("comment username: " + comment.owner.username)
                    print("comment text: " + comment.text)
                    print("comment date : " + str(comment.created_at_utc))
                print("\n\n")
        
if __name__ == '__main__':
    client = getInstagramProfile()
    username = input("Enter the username of the account which you want to scrap: ")
    client.get_post_info_csv("")
