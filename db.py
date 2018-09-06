import sqlite3

def create_db(db_path):
  conn = sqlite3.connect(db_path)
  cur = conn.cursor()
  cur.execute('''CREATE TABLE IF NOT EXISTS applications
                  (id INTEGER PRIMARY KEY,
                   name TEXT,
                   description TEXT,
                   color TEXT,
                   defaultstatus INTEGER,
                   link TEXT )  ''')
  
  cur.execute('''CREATE TABLE IF NOT EXISTS users
                  (id INTEGER PRIMARY KEY,
                   login TEXT,
                   password TEXT )  ''')

  cur.execute('''CREATE TABLE IF NOT EXISTS userapps
                  (id INTEGER PRIMARY KEY,
                   order INTEGER,
                   userid INTEGER,
                   appid INTEGER,
                   FOREIGN KEY(userid) REFERENCES users(id),
                   FOREIGN KEY(appid) REFERENCES applications(id)
                    )  ''')

  apps = [
    (NULL,'Google','Search Engine','Red',1,'http://www.google.com'),
    (NULL,'Wisc','UW homepage','Blue',0,'http://www.wisc.edu'),
    (NULL,'GLBRC','Great Lakes Bioenergy Research Center','Yellow',1,'http://www.glbrc.org'),
    (NULL,'WEI','Wisconsin Energy Institute','Green',0,'https://energy.wisc.edu/'),
    (NULL,'Twitter','Twitter','Purple',0,'https://twitter.com/'), 
  ]
  cur.executemany('INSERT INTO applications VALUES (?,?,?,?,?,?)', apps)

  users = [
    (NULL, 'user1', 'glbrcpass'),
    (NULL, 'user2', 'glbrcpass'),
    (NULL, 'user3', 'glbrcpass'),
  ]
  cur.executemany('INSERT INTO users VALUES (?,?,?)', users)
  
  conn.commit()
  conn.close

  print('DB Created Successfully!')

def desc_db(db_path):
  conn = sqlite3.connect(db_path)
  c = conn.cursor()

  for row in c.execute('SELECT * FROM applications'):
        print(row)

  print('-'*30)

  for row in c.execute('SELECT * FROM users'):
        print(row)

  conn.commit()
  conn.close

if __name__ == '__main__':
  db_path = 'db.sqlite3'
  create_db(db_path)
  desc_db(db_path)