import os, sys
os.chdir('/home/dad/Documents/twaudit/')

import twitter
import time, json
import google
import bayeslite
import numpy as np
import pandas as pd
ddl = """
CREATE TABLE IF NOT EXISTS
    follower( id INT PRIMARY KEY
            , nick TEXT
            , name TEXT
            , hasBio INT
            , fakeNews INT
            , verified INT
            , isEgg INT
            , imageUrl TEXT
            , followers INT 
            , friends INT
            , tweets INT
            , created TEXT)
"""

bql = """
INFER EXPLICIT
  isEgg, verified, hasBio
  followers, friends, tweets
  PREDICT fakeNews AS unfakeNews
  CONFIDENCE inferred_fakeNews_conf
  FROM follower
  WHERE fakeNews IS NULL;  
"""
# create databases table
with bayeslite.bayesdb_open(pathname='arolio.bdb') as bdb: bdb.sql_execute(ddl)

sql = 'select * from follower'    
with bayeslite.bayesdb_open(pathname='foo.bdb') as bdb: 
    data = bdb.sql_execute(sql).fetchall()
    df = pd.DataFrame(data)
    
# Load config from JSON
with open('config.json') as data_file: json = json.load(data_file)
    
# Connect to Twitter API
api = twitter.Api(consumer_key=json['twitter']['consumer_key']
                 ,consumer_secret=json['twitter']['consumer_secret']
                 ,access_token_key=json['twitter']['access_token_key']
                 ,access_token_secret=json['twitter']['access_token_secret'])
                      
name = 'Aroliso' 
# @Brandon87984627 ‏ nazi dude from charlottesville 0@GeWB0)@2S*Nh%V
# @uutdcbhy  arab bot
# @peplamb ‏  god bot
# @TrustTrump2020 @ElizabethVlaho1 twin bots
# @RichardByrnes rich bot
# @icutyourhair kek bot
# @smartsocialGB ‏ boss bot
# @Don__Locke ‏ brit bot
# @DeplorablePosey dog bot
# @randyferrell boss bot

users = api.GetFollowerIDs(screen_name=name, total_count=100000) 

filename = name + '.idx'
for id in users:
    with open(filename, "a") as followers: followers.write(("%s\n" % id).encode('UTF8'))

name = 'Aroliso.followers'
filename = name + '.csv'
with open(filename, "a") as followers: 
  for index, row in df.iterrows(): 
    followers.write(('%s,"%s",%s\n' % (row['id'], row['nick'], row['H'])).encode('UTF8'))

followers.write(("%s\n" % id).encode('UTF8'))

filename = name + '.csv'
for id in users:
    try:
        hasBio, isEgg, fakeNews = False, False, False
        
        follower = api.GetUser(user_id=id)
        if len(follower.description) > 0: 
            hasBio = True
        else:
            hasBio = False
            
        if follower.default_profile_image:
            isEgg = True
        else:
            isEgg = False
        
        if follower.followers_count == 0 or follower.followers_count == 2001:
            fakeNews = True
            
        if not hasBio and isEgg and follower.followers_count == 0 :
            fakeNews = True
                                
        sql = "REPLACE INTO follower VALUES(%s,'%s','%s',%s,%s,%s,%s,'%s',%s,%s,%s,'%s')"% (
                follower.id
              , follower.screen_name.replace("'","`")
              , follower.name.replace("'","`")
              , int(hasBio)
              , int(fakeNews)
              , int(follower.verified)
              , int(isEgg)
              , follower.profile_image_url
              , follower.followers_count
              , follower.friends_count
              , follower.statuses_count
              , follower.created_at)
        
        print (sql)
        with open(filename, "a") as followers: followers.write((sql+os.linesep).encode('utf8'))
        with bayeslite.bayesdb_open(pathname='arolio.bdb') as bdb: bdb.sql_execute(sql)
        Zzz = 0
    except Exception as e:
        print('Things go wrong sometimes %s' % e.message)
        Zzz += 90
        time.sleep(Zzz)
        

#lastid:889740995436457984