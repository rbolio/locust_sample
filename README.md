# Locust Performance testing

## Running with UI:

` $ locust -f ./locustfile.py --host=http://example.com `

View the UI at 

localhost:8089




## Running without the UI
`locust -f ./locustfile.py  --no-web -c 1000 -r 100 --run-time 1h30m --host=https://www.example.com`

where c = amount of users
r = spawn rate
run time = total time the test will run
