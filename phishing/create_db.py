import os
from app import *
with app.app_context():
    db = get_db()
    cur = db.cursor()

    sql = '''
CREATE SEQUENCE user_id_seq;
    CREATE TABLE public."User"

  username character varying(120),
  clicked_link boolean,
  entered_password boolean,
  CONSTRAINT "username_pk" PRIMARY KEY (username)
)
WITH (
  OIDS=FALSE
);
'''

    cur.execute(sql)
    db.commit()
