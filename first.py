from http import client
import praw
import os
import random
import time

reddit = praw.Reddit(
    client_id = "Client id",
    client_secret = "Client Secret",
    user_agent = "User Agent",
    username = "Reddit Username",
    password = "Reddit Password"    

)

subreddit = reddit.subreddit("MMA")

#storing the quotes in a list
quotes = ["In the middle of every difficulty lies opportunity.  -Albert Einstein,", 
          "If it matters to you, you’ll find a way  -Charlie Gilkey",
          "Tough times never last, but tough people do.  -Robert Schuller", "Every moment is a fresh beginning.  -T.S. Eliot",
          "Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle.  -Confucius",
          "Don’t judge each day by the harvest you reap but by the seeds that you plant.  -Robert Louis Stevenson"
]

for submission in subreddit.hot(limit = 12):
    # gives us the title for 12 hot posts
    print(submission.title)
    
    for comment in submission.comments:
        if hasattr(comment, "body"):
            comment_lower = comment.body.lower()
            # checking whether the word sad exists in the comment or not
            if (" sad " or " unhappy " or " dejected " in comment_lower):
                print(comment.body)
                rand_index = random.randint(0, len(quotes) - 1)
                # replying to the comment using a random quote
                comment.reply(quotes[rand_index])
                
                time.sleep(600)
                
                
