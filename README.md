# WingTel Coding Challenge

## Requirements
* Python 3.5+
* SQLite

## Starting the server
Everything is set up, including the database and some seed data. All you need to do is create the virtual environment with the dependencies and then execute `flask run`. Voila!

## Challenge
1. Create an endpoint that return usage data for a subscription. This should include the following:

- Returns the amount of data usage for a given subscription in gigabytes for the current billing cycle
- If the subscription is over their allotted data limit of the related plan, this should be indicated in the response

2. Create a function in the tasks directory that checks if subscriptions are over their allotted data usage for the current billing cycle. If they are, they should have the "Data Block" service code applied to the subscription.

### NOTES:
- A subscription must be `active`, `suspended`, or `expired` to have any usage data
- A subscription should not have the data blocking service code applied if it's on an unlimited plan

## Bonuses
- Extra points for efficiency
- Add to or modify the schema to optimize usage queries
- Improve the existing code in general
