from apscheduler.schedulers.blocking import BlockingScheduler
import datetime

start_time = datetime.datetime.now()
print('=== Skyze Scheduler ========== ' + str(start_time) + ' ========== ')
print()

sched = BlockingScheduler()


@sched.scheduled_job('cron', day_of_week='mon-sun', hour='0-23')
def cryptopia_hourly_update():
    message = 'Scheduler:: Triggering:: cryptopia_hourly_update'
    print(message)
    send_message(message)


@sched.scheduled_job('cron', day_of_week='mon-sun', hour=14, minute=30)
def cmc_daily_update():
    message = 'Scheduler:: Triggering:: CMC all markets Daily Update at 2:30pm.'
    print(message)
    send_message(message)


@sched.scheduled_job('cron', day_of_week='mon-sun', hour=10, minute=12)
def poloniex_daily_update():
    message = 'Scheduler:: Triggering:: Poloniex all markets Daily Update at 10:12am'
    print(message)
    send_message(message)


sched.print_jobs()
print("\n\n")
sched.start()
