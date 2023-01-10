

from slack_sdk import WebClient

usernames = []

client = WebClient(token='BOT_TOKEN')    # Replace with your own SLACK Bot User OAuth Token
response = client.conversations_members(channel="CHANNEL_ID")   # Replace with the channel_id of your own
users = response["members"]


for user in users:
    response = client.users_info(user=user)
    user_name = response['user']['name']
    usernames.append(user_name)

for u in usernames:
    print(u)
