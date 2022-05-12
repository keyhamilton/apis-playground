#!/bin/bash

#test
#echo 'Hi'

# curl "https://gorest.co.in/public/v2/users/" -H "Accept:application/json" > users.json

curl -i \
-H "Accept:application/json" \
-H "Authorization: Bearer 3c7dd720c035ae862e9f84ef23b296aa39ea004d6b516f52f6f164c903c708dc" \
-H "Content-Type: application/json" \
-X PATCH "https://gorest.co.in/public/v2/users/3779" -d '{"status":"active"}'



