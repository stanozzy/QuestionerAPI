''' Questions will be stored in a list
'''
question_list = []

class Question():
    def __init__(self):
        self.db = question_list

    def create_question(self, createdOn, title, author, body, votes):
        data = {
            'question_id': len(self.db) + 1,
            'createdOn' : createdOn,	   
            'title' : title,
            'author' : author,
            'body' : body,
            'votes' : votes
        }   

        self.db.append(data)
        return data

    def get_all(self):
        return self.db

    def get_one(self,question_id):
            specific_question = [item for item in self.db] if item['question_id'] == question_id
            return specific_question

        
