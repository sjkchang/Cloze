# vigilant-waffle
Cloze, a productivity webapp, (travis ci says failing, but tests pass if you run pytest in cmd line)
[![Build Status](https://travis-ci.com/sjkchang/vigilant-waffle.svg?branch=master)](https://travis-ci.com/sjkchang/vigilant-waffle)
## How to Run
To run the project, run the run.py file with python 2.7, the go to http://localhost:5000 (pip Install any imports that you do not already have on your system)

### Feature #1 Register
Registers user into the database, with their username, email, and password
To verify: Click on register link on nav bar and register.
 
 ### Feature #2 Login
Logs registered users into the website using their email and password
To verify: When registering, you are automatically logged in. To verify that the login forms work to log in, press logout in the nav bar, then login with the email, and password you used when registering
  
### Feature #3 Logout
To verify: You already verified it works verifying the last feature

### Feature #4 Style
To Verify: Look at website, and see that it is styled

### Feature #5 Pomodoro Timer
To Verify: Click pomodoro Timer in nav bar. There are four buttons, work should start a 25 minute countdown, shortBreak should start a 5 minute coundown, long break a 15 minute countdown, stop should stop any of the previous countdowns and reset the timer to 25min

### Feature #6 Change Username or Email
To verify: Go to account on the nav bar, and fill out the form for what you want to change. Log out and log back in with the new username or email

### Feature #7 Add meal
To verify: go to meal log on nav bar, and press the add meal link. Fill out the form, and submit. A banner indicating a meal has been added should be show up. We have yet to display this data, but you could look in the db file to see if its their. 

### Feature #8 Journal
