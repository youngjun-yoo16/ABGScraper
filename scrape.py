import instaloader

if __name__ == '__main__':
    bot = instaloader.Instaloader()
    username = input("Enter the username of the account which you want to scrap: ")
    bot.download_profile(username, profile_pic_only = True)
