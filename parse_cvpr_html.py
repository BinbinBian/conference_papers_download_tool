# coding = utf-8
from bs4 import BeautifulSoup
#import requests

#url = 'http://jmlr.org/proceedings/papers/v48/'
#response = requests.get(url)
def lencheck(element, length=1):
  if len(element) < length:
    raise RuntimeError, "parse error %s" % (str(element))

f = open('CVPR_2016.html','r')
soup = BeautifulSoup( f ) #response.text)
papers = soup.findAll(u"div", attrs={u"id": u"content"})
lencheck(papers)

headings = papers[0].findAll(u"dt",attrs={u'class': u'ptitle'})
lencheck(headings)
titles = []
for heading in headings:
  title = heading.text.strip()
  title = title.replace(':','')
  title = title.replace('\"','')
  title = title.replace('/','-')
  title = title.replace('\\','-')
  title = title.replace('?',' ')
  title = title.replace(',',' ')
  titles.append(title)

pdfs=[]
links = papers[0].findAll(u"dd")
for link in links:
  if 'pdf' in link.text:
    a_s = link.findAll(u'a')
    pdf_link = a_s[0]['href'].strip()
    pdfs.append(pdf_link)

#print len(pdfs)==len(titles)
#True
f_res = open('cvpr_papers.txt','wb')

for i in xrange(len(pdfs)):
  pdf = pdfs[i]
  title = titles[i]

  res = title +'\t'+pdf+'\n'
  f_res.write(res.encode('utf-8'))
  #pauthors = paper.findAll(u"p", attrs={u"class": u"authors"})
  #lencheck(pauthors)
  #authors = pauthors[0].text.strip()
  
  #lencheck(link)
 # pdf_link = link[1]['href'].strip()
  
  #res = title+'\t'+pdf_link+'\n'
    
  #f_res.write(res.encode('utf-8'))

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

