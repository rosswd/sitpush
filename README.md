# sitpush
The [sit](https://itunes.apple.com/us/app/sit-a-beautiful-simple-meditation-timer/id1023238111?mt=8) app on iOS doesn't send notifications. Mindfulness is important to keep me straight but sometimes I get into bad habits. This little python based [pushover](https://pushover.net/) program will help keep me on the right road.

## setup
+ clone
+ `pip install -r requirements.txt`
+ create a new pushover app, note credentials
+ enter environment variables in .env (see below)
+ test run with `python app.py`
+ set up cron (linux) or launchd (mac)

### .env
Add your own .env file with pushover settings: `PUSHOVER_TOKEN`, `PUSHOVER_USER` and `PUSHOVER_TITLE`. `python-dotenv` will not work if your quote the variables like this `"PUSHOVER_TITLE"=Sit`. You have to enter the variable unquoted, `PUSHOVER_TITLE=Sit`.

### cron
Use cron to schedule when the notifications fire. Mine runs on a headless raspberry pi.

#### Cron Example
Note: You can run python files directly but this is how I do it.

+ Create a `script.sh` file
+ Add a bash shebang `#!/bin/bash`
+ Find your environment python, such as `$HOME/.virtualenvs/<env>/python`
+ Add a line that runs `app.py`
    + `$HOME/.virtualenvs/<env>/python $HOME/sites/sitpush/app.py`
+ Make your script.sh file executable with `chmod +x script.sh`
+ Test your file: `./script.sh`
