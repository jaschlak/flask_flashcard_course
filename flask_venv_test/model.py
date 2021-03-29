# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 10:30:42 2021

@author: JordanSchlak
"""

import json

def load_db():
    with open('flashcards_db.json') as f:
        #print(str(f))
        return json.load(f)
          
def save_db():
    with open('flashcards_db.json', 'w') as f:
        return json.dump(db, f)
    
db = load_db()