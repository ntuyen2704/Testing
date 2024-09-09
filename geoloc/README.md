Precondition:

-Create virtual env:

python -m venv venv
.\venv\scripts\activate

- Install requests, pytest 

pip install requests
pip install pytest



Example how to run the utility:

python geoloc_util.py --location "Madison, WI"

python geoloc_util.py --location "Madison, WI" "12345"

python geoloc_util.py --location "Madison, WI" "12345" "Chicago, IL" "10001"