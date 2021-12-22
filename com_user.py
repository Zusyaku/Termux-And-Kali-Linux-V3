import socket
from urlparse import urlparse
import  time, urllib2, re,  httplib
print '''
#=[+]==========================================[+]=#
|             com_user server scanner              |
|==================================================|
|             Coded by Budz Story-zz               |
|            Indonesian Fighter Cyber              |
#=[+]==========================================[+]=# 
'''
file2=open('com_user.txt','a')

 

def check(site) :
 try  :

  w  = urllib2.urlopen(site).read()
 except urllib2.URLError, (err):
              pass
 except socket.error , v :
            pass
 except urllib2.HTTPError, err:
          pass
 except IOError, e:
             pass
 except httplib.IncompleteRead ,e:
  pass
 else :
   if re.findall('Image Manager',w) :
    ox=  urlparse(site)
    print 'w00t ! ! Found In  => ' + ox[1]
    file2.write(ox[1]+'\n')
    
def xlol(site):
        try:
           
            urllib2.urlopen(site)
 
        except urllib2.URLError, (err):
              pass
        except socket.error , v :
            pass
        except urllib2.HTTPError, err:
          pass
        except IOError, e:
             pass
        else:
            check(site)
def bing_it(ip):
 
     page  = 0
     while(page <= 200):
      try :
          bing      = "http://www.bing.com/search?q="+ip+"+index.php?option=com_&first="+str(page)
 
          openbing  = urllib2.urlopen(bing)
 
          readbing = openbing.read()
          findbing = re.findall('<div class="sb_tlst"><h3><a href="(.*?)" h=',readbing)
 
          for i in range(len(findbing)):
              x=findbing[i]
              global o
              o=  urlparse(x)
              y = o[2].replace('/index.php','')
              print 'checking ' + o[1]
              check('http://'+o[1]+y+'/index.php?option=com_users&view=registration')
              
 
          page = page + 10
      except httplib.IncompleteRead ,e:
        pass  
      except urllib2.URLError, (err):
              pass
      except socket.error , v :
            pass
      except urllib2.HTTPError, err:
          pass
      except IOError, e:
             pass
 
 
Xip = raw_input('Domain : ')
 
bing_it(Xip)