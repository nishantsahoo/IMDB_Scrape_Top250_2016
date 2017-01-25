import urllib2
import sys
from BeautifulSoup import BeautifulSoup
from pandas import Series, DataFrame
from tqdm import tqdm
sys.stdout = open('IMDB_Top_250.txt','w')
opener = urllib2.build_opener()
opener.addheaders=[('User-agent','Mozilla/5.0')]
url = "http://www.imdb.com/chart/top"
ourUrl = opener.open(url).read()
soup = BeautifulSoup(ourUrl)

table = soup.find('table', attrs={'data-caller-name':'chart-top250movie'})
table_tbody = table.findChildren('tbody', attrs={'class':'lister-list'})
count = 1
itermovie = iter(table_tbody[0].findChildren('tr'))

print 'IMDB Movie List Top 250: '

i = 1
next(itermovie)
for tr in tqdm(itermovie):
    title = tr.find('td', attrs={'class':'titleColumn'})
    title_info = title.findAll('a')
    for each in title_info:
        print str(i) + '. ' + str(title_info[0].text.encode('utf-8').decode('ascii', 'ignore')) + ' - ',
    rating = tr.findChildren('strong')
    print str(rating[0].text.encode('utf-8').decode('ascii', 'ignore'))
    i += 1
