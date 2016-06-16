import glob
import os

f = open('icml_papers_1.txt')
p_dict = {}
for line in f:
  #print line
  line = line.strip('\r\n').split('\t')
  #print len(line)
  if len(line)<2:
    continue
  title = line[0]
  pdf = line[1].split('/')[-1]

  supp = ''
  if len(line)==3:
    if len(line[2])>1:
      supp = line[2].split('/')[-1]
  #p_dict['title'] = title
  p_dict[pdf] = title
  #p_dict[pdf].append(title)
  if supp != '':
    p_dict[supp] = title
  #p_dict[supp] = supp

#print len(p_dict)

for filename in glob.glob('./*.pdf'):
  filename = filename.strip('.\\')
  #print filename
  if not filename in p_dict.keys():
    continue
  if 'supp' in filename:
    changed_name = '16'+p_dict[filename]+' '+ filename
    try:
      os.rename(filename, changed_name)
    except:
      print filename, ' ', changed_name
  else:
    changed_name = '16'+p_dict[filename]+' '+ filename
    try:
      os.rename(filename, changed_name)
    except:
      print filename,' ',changed_name
    


