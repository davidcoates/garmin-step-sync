# Garmin Step Sync

Pushes Garmin step count [Steps Tracker](https://steps.mayb.gay/).

## Setup

1. Acquire a [Steps Tracker](https://steps.mayb.gay/) token and place it in `.env` as `TRACKER_TOKEN=...`.
2. Run `docker compose run --rm login` and enter your Garmin credentials.

## Sync

Run `docker compose run --rm sync` daily to synchronize steps.

This synchonizes steps for the past three days (including today) by default. The number of days can be changed with the `SYNC_DAYS` environment variable.
