
import snscrape.modules.twitter as sntwitter
import psycopg2
maxTweets = 3000
db = psycopg2.connect(user="postgres", password="12345",
                      host="localhost", port="5432", database="twitter")

for i, tweet in enumerate(sntwitter.TwitterSearchScraper('#atatürk since:2020-03-1 until:2022-04-11').get_items()):
    if i > maxTweets:
        break
    print(tweet.content)
    print(tweet.username)
    print(tweet.date)
    content = tweet.content
    username = tweet.username
    date=tweet.date
    sorgu = "Insert into tweetler(content,username,date) Values(%s,%s,%s)"
    cursor = db.cursor()
    cursor.execute(sorgu, (content, username, date))
    db.commit()
    cursor.close()
