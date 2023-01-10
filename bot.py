# I have created a temporary channel for the demostartion purpose
# TOKEN_ID = xoxb-4617787520580-4618893687733-QXrxPmmTTbiVkdzzRNiWM4uV
# CHANNEL_ID = C04HNP0BTFZ

from slack_sdk import WebClient

usernames = []

client = WebClient(token='xoxb-4617787520580-4618893687733-QXrxPmmTTbiVkdzzRNiWM4uV')    # Replace with your own SLACK Bot User OAuth Token
response = client.conversations_members(channel="C04HNP0BTFZ")   # Replace with the channel_id of your own
users = response["members"]


for user in users:
    response = client.users_info(user=user)
    user_name = response['user']['name']
    usernames.append(user_name)

for u in usernames:
    print(u)
