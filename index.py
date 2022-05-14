import wikipedia
import sqlite3

con = sqlite3.connect("celebs.db") #creates new db file if file doesnt already exist
cur = con.cursor() #enables command execution on the database
print("Type your search...")
query = input() #stores the input
suggestion = wikipedia.suggest(query)#stores alternative results suggested by wiki api
result = wikipedia.search(query, 1)# the search result based on input
summary = wikipedia.summary(query)

def create_table(): #creates the table if it doesnt exist
  cur.execute("CREATE TABLE IF NOT EXISTS famous_people (id integer primary key autoincrement, name text, summary text)") 

def insert_data(): #insert data values into the table
  if result:
    con.execute("""INSERT INTO famous_people (name, summary) VALUES (?, ?)""", ( result[0], summary))
    con.commit()
    print("data added to the database")
    #print(select_all())
  else:
    print("I don't know this person. Did you mean " + suggestion + " ?")
  
# def select_all():
#   data = cur.execute("SELECT * FROM famous_people")
#   info = data.fetchall()
#   return info

create_table()
insert_data()
con.close()
