#!/usr/bin/env python

import sqlite3

conn = sqlite3.connect('quotations.db')
print("Opened database successfully")

create_author_table = """CREATE TABLE authors(
  aid    INTEGER PRIMARY KEY,
  name  TEXT NOT NULL
);"""

create_quote_table = """CREATE TABLE quotations(
  qid     INTEGER PRIMARY KEY,
  quote   TEXT NOT NULL,
  aid INTEGER NOT NULL,
  FOREIGN KEY(aid) REFERENCES authors(aid)
);"""

conn.execute(create_author_table)
print("author table created successfully")

conn.execute(create_quote_table)
print("quote table created successfully")

conn.close()
