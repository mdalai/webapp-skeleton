import sqlite3

def create_db(db_path):
  conn = sqlite3.connect(db_path)
  cur = conn.cursor()
  # drop tables before create
  cur.execute("DROP TABLE IF EXISTS applications")
  cur.execute("DROP TABLE IF EXISTS users")
  cur.execute("DROP TABLE IF EXISTS userapps")

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
                   placeorder INTEGER,
                   user_id INTEGER,
                   app_id INTEGER,
                   FOREIGN KEY (user_id) REFERENCES users (id),
                   FOREIGN KEY (app_id) REFERENCES applications (id)
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
  print('-'*10 + ' TOTAL Tables: {}'.format(len(tables)))
  for i,t in enumerate(tables):
    print(str(i+1) + '-'*10 + ' DESC {}: '.format(t[0]))
    meta = c.execute("PRAGMA table_info({})".format(t[0]))
    for r in meta:
      print(r)
    print(str(i+1) + '-'*10 + ' QUERY {}: '.format(t[0]))
    for row in c.execute('SELECT * FROM {}'.format(t[0])):
        print(row)
  
  #print(c.fetchall())
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

def desc_table(db_path,tablename):
  conn = sqlite3.connect(db_path)
  c = conn.cursor()

  print('-'*10 + ' DESC {}: '.format(tablename))
  meta = c.execute("PRAGMA table_info({})".format(tablename))
  for r in meta:
    print(r)
  print('-'*10 + ' QUERY {}: '.format(tablename))
  for row in c.execute('SELECT * FROM {}'.format(tablename)):
      print(row)
  
  conn.close()

if __name__ == '__main__':
  db_path = 'mydb.sqlite3'
  #create_db(db_path)
  #gen_appuser_data(db_path)
  #desc_db(db_path)
  desc_table(db_path,'userapps')
  #desc_table(db_path,'users_customuser')