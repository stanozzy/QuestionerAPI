# questioner-API  
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

This is the API for Questioner, a platform for crowdsourcing questions for a meetup. 
The project is managed with a Pivotal tracker board. [View the board here](https://www.pivotaltracker.com/n/projects/2235257)
# Required Features
-----------------------
1. Admin can create meetups.
2. Users can create an account and log in.
3. Users can post questions to a specific meetup.
4. Users can upvote or downvote a question.
5. Questions are sorted based on the number of upvotes a question has, which helps the
meetup organizer(s) to prioritize questions most users are interested in.
6. Users can post comments to a specific question.

#Optional Features:
1. Admin can add images to a meetup record.
2. Admin can add tags to a meetup record.
3. User can reset password.


You can view the user interface [here](https://stanozzy.github.io.)

Pre-requisites
----------------------
1. Python
2. Flask
4. Postman

Getting started
--------------------
1. Clone this repository
```
    https://github.com/stanozzy/questioner-api-2.git
```

2. Navigate to the cloned repository
```
    cd questioner-api-2
```

Installation
---------------------------------
1. Create a virtual environment
```
    virtualenv -p python3 venv
```

2. Activate the virtual environment
```
    source venv/bin/activate
```

3. Install git
```
    sudo apt-get install git-all
```

4. Switch to 'develop' branch
```
    git checkout develop
```

5. Install requirements
```
    pip install -r requirements.txt
```
Run the application
---------------------------------
```
    python run.py
```
API endpoints:
-----------------------------------------------

| Endpoint | Functionality |
----------|---------------
POST/meetups | Create a meetup record
GET/meetups/&lt;meetup-id&gt; | Fetch a specific meetup record
GET /meetups/upcoming/ | Fetch all upcoming meetup records
POST /questions | Create a question for a specific meetup
PATCH /questions/&lt;question-id&gt;/upvote | Upvote (increase votes by 1) a specific question
PATCH /questions/&lt;question-id&gt;/downvote | Downvote (decrease votes by 1) a specific question
POST /meetups/&lt;meetup-id&gt;/rsvps | Respond to meetup RSVP




Author:
---------------
**Stanslous Yegon**  [stanozzy](https://github.com/stanozzy)

License
-----------
This project is licensed under the MIT License. See [License](https://github.com/stanozzy/questioner-ui/blob/master/LICENSE) for details.


Acknowledgements:
---------------

- Andela workshops
- Learning Facilitators
- Team mates
