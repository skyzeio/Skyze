# Skzye Scheduler Service Manual

## Overview

This service schedules the sending of messages to other services.

It is used for things like triggering market data updates or scanner updates

## Adding a new message to be scheduled
1. Ensure the message module has been imported e.g. `from Skyze_Messaging_Service.Messages.MessageScreenerRun import MessageScreenerRun`. If the message does not exist then see the _SkyzeMessagingService Manual_ on how to create new message types
2. In `SkyzeSchedulerSerivce.py`add a function to call the job to be scheduled e.g. `Bitfinex 90 minute update`
3. In `SkyzeSchedulerSerivce.start()`add the timing of the update by scheduling the newly added function

### Connecting the Market Data Updater to the update message
See the `Skyze Market Data Updater Service` manual
