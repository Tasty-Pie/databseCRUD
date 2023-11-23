from apscheduler.schedulers.background import BackgroundScheduler
import requests


def ping_server():
    try:
        response = requests.get('https://db-as2-deploy.onrender.com/ping')  # Replace with your server URL
        print("Ping response:", response.status_code)
    except requests.RequestException as e:
        print("Error pinging the server:", e)


def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(ping_server, 'interval', minutes=13)
    scheduler.start()
