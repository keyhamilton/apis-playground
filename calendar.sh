#!/bin/bash
#!/usr/bin/python3

# usage
# ./calendar.sh [nationality] [(optional)year]

curl "https://www.googleapis.com/calendar/v3/calendars/pt.{$1}%23holiday%40group.v.calendar.google.com/events?key=AIzaSyBsz28BT9vZUSnTqiyhuK5q_3V-xyXhlXQ" > calendar.json

python3 calendar.py $2