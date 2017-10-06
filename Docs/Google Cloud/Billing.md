# Google Cloud Billing

## Instance Hour calculations

https://stackoverflow.com/questions/16782136/how-are-frontend-instance-hours-calculated-on-app-engine

You're charged 15 minutes every time an instance is spins up.

If you have few requests, but they are spaced out, your instance would shut down, and you'll incur the 15 minute charge the next time the instance spins up.

You could easily rack up 4.5 instance hours with 18 HTTP requests.

https://serverfault.com/questions/717810/app-engine-instance-hours-seem-way-too-high
There are no instance classes counting as 3 times a B1; but for example instance class B4 counts as 4 times a B1, so it would consume 6 instance hours in 1.5 hours of elapsed-time activity, counting the 15 minutes after it goes idle each time.

6 requests in 2 hours, equally spaced, each processed "instantly" (thus counting only the 15 minutes after it goes idle) by a B4 instance, for example, would show up as "6 instance hours" (6 * 0.25 * 4), i.e, 75% of the 8-hours "free quota" for backend "instance hours".
