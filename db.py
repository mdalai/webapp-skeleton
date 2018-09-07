import sqlite3

def create_db(db_path):
  conn = sqlite3.connect(db_path)
  cur = conn.cursor()
  # drop tables before create
  cur.execute("DROP TABLE IF EXISTS applications")
  cur.execute("DROP TABLE IF EXISTS users")
  cur.execute("DROP TABLE IF EXISTS userapps")

  cur.execute('''CREATE TABLE IF NOT EXISTS applications
                  (pid INTEGER PRIMARY KEY,
                   name TEXT,
                   description TEXT,
                   color TEXT,
                   defaultstatus INTEGER,
                   link TEXT )  ''')
  
  cur.execute('''CREATE TABLE IF NOT EXISTS users
                  (pid INTEGER PRIMARY KEY,
                   login TEXT,
                   password TEXT )  ''')

  cur.execute('''CREATE TABLE IF NOT EXISTS userapps
                  (pid INTEGER PRIMARY KEY,
                   placeorder INTEGER,
                   userid INTEGER,
                   appid INTEGER,
                   FOREIGN KEY (userid) REFERENCES users (pid),
                   FOREIGN KEY (appid) REFERENCES applications (pid)
                    )  ''')

  apps = [
    (None,'Google','Search Engine','Red',1,'http://www.google.com'),
    (None,'Wisc','UW homepage','Blue',0,'http://www.wisc.edu'),
    (None,'GLBRC','Great Lakes Bioenergy Research Center','Yellow',1,'http://www.glbrc.org'),
    (None,'WEI','Wisconsin Energy Institute','Green',0,'https://energy.wisc.edu/'),
    (None,'Twitter','Twitter','Purple',0,'https://twitter.com/'), 
  ]
  cur.executemany('INSERT INTO applications VALUES (?,?,?,?,?,?)', apps)

  users = [
    (None, 'user1', 'glbrcpass'),
    (None, 'user2', 'glbrcpass'),
    (None, 'user3', 'glbrcpass'),
  ]
  cur.executemany('INSERT INTO users VALUES (?,?,?)', users)
  
  conn.commit()
  conn.close

  print('DB Created Successfully!')

def desc_db(db_path):
  conn = sqlite3.connect(db_path)
  c = conn.cursor()

  # databse descriptions
  tables = c.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
  print('-'*5 + ' TABLES '+ '-'*30)
  for t in tables:
    print(t)

  print('-'*5 + ' TABLE INFO '+ '-'*30)
  meta = c.execute("PRAGMA table_info('applications')")
  for r in meta:
    print(r)
  print('-'*10)
  meta = c.execute("PRAGMA table_info('users')")
  for r in meta:
    print(r)
  print('-'*10)
  meta = c.execute("PRAGMA table_info('userapps')")
  for r in meta:
    print(r)
  
  #print(c.fetchall())

  print('-'*5 + ' TABLE DATA '+ '-'*30)

  for row in c.execute('SELECT * FROM applications'):
        print(row)

  print('-'*10)

  for row in c.execute('SELECT * FROM users'):
        print(row)

  print('-'*10)

  for row in c.execute('SELECT * FROM userapps'):
        print(row)

  conn.close

def gen_appuser_data(db_path):
  conn = sqlite3.connect(db_path)
  c = conn.cursor()

  rows = c.execute('''select 1,pid from applications 
                    WHERE defaultstatus=1
                    ''').fetchall()
  data = [ (None,i+1,)+row for i,row in enumerate(rows)]
  print(data)
  c.executemany('INSERT INTO userapps VALUES (?,?,?,?)', data)
  
  conn.commit()
  conn.close()

if __name__ == '__main__':
  db_path = 'db.sqlite3'
  #create_db(db_path)
  gen_appuser_data(db_path)
  desc_db(db_path)