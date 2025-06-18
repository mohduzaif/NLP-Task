import json

class Database:
    
    # add the data into a json file.
    def add_data(self, name, email, password):

        # open the file for collect complete user details.
        with open('database.json', 'r') as rf:
            data = json.load(rf)

        # print(data)
        # check email exists or not
        if email in data:
            return False
        else:
            data[email] = [name, password]
            
            # write back the data by adding new user. 
            with open('database.json', 'w') as wf:
                json.dump(data, wf)
            
            return True
        

    # match the credentials of the user
    def match_credentials(self, email, password):
        
        with open('database.json', 'r') as rf:
            data = json.load(rf)

        if email in data:
            if data[email][1] == password:
                return True
            else:
                return False
            
        else:
            return False