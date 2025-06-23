from apscheduler.schedulers.blocking import BlockingScheduler
from trends import get_trending_topics
from formatter import make_hype_post
from bot import send_post

def job():
    headlines = get_trending_topics()
    for h in headlines:
        post = make_hype_post(h)
        send_post(post)

scheduler = BlockingScheduler()
scheduler.add_job(job, 'interval', hours=2)
print("Бот запущен. Публикации будут каждые 2 часа.")
scheduler.start()
