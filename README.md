# mealie
Docker Compose setup for Mealie docker app, with python script that pulls random meals from your Mealie instance for the next 7 days, formats them, and pushes them to your ntfy server.

Installation Process:
1. Save docker compose.yaml in directory
2. Create .env in directory with:
    * TZ=Timezone
    * BASE_URL=http://mealie.<your-domain>.com
3. Save mealie_ntfy.py in directory (*must be able to reach mealie container)

How to setup schedule using cron jobs
To automate this script to run automatically every Sunday at 6:00 PM (TZ), you can set up a Cron job on your Linux/macOS server:
1. Open crontab editor:

   crontab -e
   
2. Add the following line to execute the script every Sunday at 18:00 (Make sure to replace /path/to/python and /path/to/mealie_ntfy.py with your actual file paths):

   0 18 * * 0 TZ=<insert TZ> /usr/bin/python3 /path/to/mealie_ntfy.py >/dev/null 2>&1
