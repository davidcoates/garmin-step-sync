#!/usr/bin/env python3

from datetime import date, timedelta
from dotenv import load_dotenv
import json
import os
from pathlib import Path
import requests
import sys

from garminconnect import (
    Garmin,
)


load_dotenv()

TOKEN_STORE_PATH = Path(os.getenv("TOKEN_STORE_PATH", "tokens"))
TRACKER_TOKEN = os.environ["TRACKER_TOKEN"]

def sync_steps(days_back):
    """
    Retrieve and send step data for a specified number of days in the past.

    Args:
        days_back: Number of days in the past to retrieve step data for (including today)
    """

    client = Garmin()
    client.login(str(TOKEN_STORE_PATH))

    target_date = date.today()
    for _ in range(days_back):

        target_date_str = target_date.strftime('%Y-%m-%d')
        steps = client.get_stats(target_date_str)["totalSteps"]
        print(f"Pulled steps({steps}) from Garmin for date({target_date})")

        step_data = json.dumps({
            'date': target_date.strftime('%Y-%m-%d'),
            'steps': steps,
        })
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.put(f"https://steps.mayb.gay/api/steps?token={TRACKER_TOKEN}", data=step_data, headers=headers)
        print(f"Pushed to tracker: {response.text}")

        target_date -= timedelta(days=1)


if __name__ == '__main__':

    if len(sys.argv) > 1:
        try:
            days = int(sys.argv[1])
        except ValueError:
            print("Usage: python sync.py [days]")
            exit(1)
    else:
        days = 1

    sync_steps(days)
