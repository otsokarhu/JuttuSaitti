JuttuSaitti is an online forum, where people can register, create new conversation topics and comment them.

For now, users can register, login, add categories and then topics to them with unique content, and comment on those topics


To Do:
contact page
deleting topics and comments


How to start it:

1. git clone this repository
2. create .env file, with:<br>
      DATABASE_URL= local database<br>
      SECRET_KEY= secret key<br>

3. Activate virtual environment: <br>
      $ python3 -m venv venv<br>
      $ source venv/bin/activate<br>
      $ pip install -r ./requirements.txt<br>
      
4. Make the database:<br>
      $ psql < schema.sql
                         
5. Run the application:<br>
      $ flask run