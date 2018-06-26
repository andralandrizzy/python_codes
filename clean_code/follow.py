# Date: Feb, 10, 2018
# Description: Quick program code to calculate number of my follower.
# Author: Andral Orelus

import datetime
import math

goal_follow = int(input("Enter the amount of instagram followers goal: "))
current_follow = int(input("What is your current number of followers? "))
follow_to_go = goal_follow  - current_follow

avg_follow_day = int(input("Enter your average followers per day: "))
days_to_go = math.ceil(follow_to_go / avg_follow_day)

today = datetime.date.today()
res = today + datetime.timedelta(days = days_to_go)

if res > today:
    print("You will reach the amount of instagram follower goal in: -->", res)
else:
    print("You have reached your goal for instagram followers since: -->", res)















