#!usr/bin/python
import os
import urllib2

def main():

    fqn = os.uname()[1]
    ext_ip = urllib2.urlopen('http://whatismyip.org').read()
    print ("Asset: %s " % fqn, "Checking in from IP#: %s " % ext_ip) 
    
print 'hi'    
if __name__ == '__main__':
   main ()
