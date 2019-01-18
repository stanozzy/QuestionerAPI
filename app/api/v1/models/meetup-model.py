''' meetup model.
data will be stored in a list'''

meetup_list = []
rsvp_list = []

class Meetup():
    def __init__(self):
        self.db = meetup_list

    def create_meetup(self, title, venue, topic, date, time, tags):
    	data = {
    		"meetup_ID" = len(self.db) + 1, 
    		"title" : title,
    		"venue" : venue,
    		"topic" : topic,
    		"date"  : date,
    		"time"  : time,
    		"tags"  : tags

    	}
    self.db.append(data)
    return self.db	

    def fetch_all_meetups(self):
    	return self.db

    def fetch_one_meetup(self, meetup_ID):
    	specific_meetup = [item for item in self.db] if item['meetup_ID'] == meetup_ID
        return specific_meetup

class Rsvp():
	def __init__(self):
		self.db = rsvp_list

	def reply(self, topic, status):
		data = {
			"rsvp_ID" = len(self.db) + 1,
			"topic" = topic,
			"status" = status;
		}
		self.db.append(data)
		return self.db


