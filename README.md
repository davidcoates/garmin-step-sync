# Garmin Step Sync

Pushes Garmin step count [Steps Tracker](https://steps.mayb.gay/).

## Setup

1. Create a virtual environment and install dependencies with `pip install -r requirements.txt`.
2. Acquire a [Steps Tracker](https://steps.mayb.gay/) token and place it in `.env` as `TRACKER_TOKEN=...`.
3. Run `python login.py` and enter your Garmin credentials.

## Sync

Run `python sync.py [days_to_sync]` daily to synchronize steps.
