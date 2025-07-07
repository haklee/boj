import os
import json
from datetime import datetime

from dotenv import load_dotenv
from boj_crawler import BOJCrawler

load_dotenv()
user_id = os.environ.get("USER_ID")
date = None

with open("data/solved_problems.json", "r", encoding="utf-8") as f:
    data = json.load(f)

    # 마지막으로 푼 문제의 날짜를 찾는다.
    # 가장 큰 submission_id값을 가진 문제가 가장 마지막에 푼 문제다.
    last_prob = sorted(data, key=lambda i: int(i["submission_id"]))[-1]
    sub_time = datetime.strptime(last_prob["submission_time"], "%Y-%m-%d %H:%M:%S")
    date = sub_time.strftime("%y%m%d")

# 앞서 찾은 날짜를 포함하여 푼 문제 크롤링.
# 마지막 크롤링 이후 같은 날 다른 문제를 더 풀었을 수 있다.
crawler = BOJCrawler(user_id, start_date=date)
problems = crawler.get_solved_problems()

# 새로운 문제들을 앞에 붙임
data = [
    p for p in problems if int(p["submission_id"]) > int(last_prob["submission_id"])
] + data

with open("data/solved_problems.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
