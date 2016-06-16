# coding = utf-8
from bs4 import BeautifulSoup
#import requests

#url = 'http://jmlr.org/proceedings/papers/v48/'
#response = requests.get(url)
def lencheck(element, length=1):
  if len(element) < length:
    raise RuntimeError, "parse error %s" % (str(element))

f = open('ICML_2016.html','r')
soup = BeautifulSoup( f ) #response.text)
papers = soup.findAll(u"div", attrs={u"class": u"paper"})

lencheck(papers)

f_res = open('icml_papers.txt','wb')

for paper in papers:
  heading = paper.findAll(u"p",attrs={'class':'title'})
  lencheck(heading)
  title = heading[0].text.strip()
  #pauthors = paper.findAll(u"p", attrs={u"class": u"authors"})
  #lencheck(pauthors)
  #authors = pauthors[0].text.strip()
  link = paper.findAll(u"a")
  lencheck(link)
  pdf_link = link[1]['href'].strip()
  if len(link)==2:
    supp_link = ''
  if len(link)==3:
    supp_link = link[2]['href'].strip()
  res = title+'\t'+pdf_link+'\t'+supp_link+'\n'
    
  f_res.write(res.encode('utf-8'))

f_res.close()
f.close()
  #linkurl = link[0]['href'].strip()
  #ret = linkre.search(linkurl)
  #if not ret:
  #  if len(link) < 2:
  #    continue
  #  raise RuntimeError, "link parsing error %s" % (linkurl)
  #papernumber = int(ret.groups()[0])
  #fulllink = burl + "/" + str(papernumber) + u".pdf"
  #outfile = os.path.join(folder, str(papernumber) + " - " + 
  #                       title + " - " + authors + ".pdf")
  #print "downloading %s ..." % (outfile),
  #sys.stdout.flush()
  #if not os.path.exists(outfile):
  #  urllib.urlretrieve(fulllink, outfile)
  #  print "done."
  #else:
  #  print "already there."
#print soup.prettify().encode('utf-8')

