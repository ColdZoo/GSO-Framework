__author__ = 'adam'
import urllib2
import linecache
from bs4 import BeautifulSoup
import os

snapshot = ''
flag_snap = False  # Control the skip of WordList

# get last state
if os.path.exists('result'):
    out = open('result', 'r')
    out_count = len(out.readlines())
    snapshot = linecache.getline('result', out_count)
    snapshot = snapshot.split(',')[0]
    print 'Found a snapshot: ' + snapshot + ', restoring from the last state'
    out.close()

out = open('result', 'a')

for line in open('wordlist'):
    line = line.strip('\n')
    # restore from last state
    if snapshot != '':
        if flag_snap is False and line != snapshot:
            continue
        if flag_snap is False and line == snapshot:
            flag_snap = True
            continue

    # send search request, on error pass
    try:
        request = urllib2.urlopen('http://www.giphy.com/search/' + line)
        response = request.read()
    except:
        pass

    # Parse the HTML using BeautifulSoup
    soup = BeautifulSoup(response)

    if soup.html.body.h1:
        content = soup.html.body.h1.get_text()
        number = content.split(' ')[0]
        print line + ',' + number
        out.write(line + ',' + number + '\n')
        # flush the data to disk
        out.flush()
    else:
        continue

out.close()

