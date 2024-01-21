import praw
import os
import time
from keep_alive import keep_alive

reddit = praw.Reddit(
  client_id = os.getenv('client_id'),
  client_secret = os.getenv('client_secret'),
  username= os.getenv('username'),
  password = os.getenv('password'),
  user_agent = "<TenHagBot1.0>",
)

keep_alive()
comment_text = "It's Ten Hag with one 'a'.\n\n ---\n\n *I am a bot. For any feedback please contact [my creator](https://www.reddit.com/user/Tempoulker).*"
subreddit = reddit.subreddit("reddevils+soccer+PremierLeague")

for comment in subreddit.stream.comments(skip_existing = True):
  comment_lower = comment.body.lower()
  
  if "ten haag" in comment_lower:
    print(comment.body)
    try:
      comment.reply(comment_text)
    except Exception as e:
      print(e)
      time.sleep(600)
      comment.reply(comment_text)
