import xml.dom.minidom as  md
import urllib.request
import os
import sys
from util import dbconnection

db=dbconnection.client.kms

##parser

class InsertDataFromXml:
    
    def __init__(self):
        self.perm_dic={}
    def print_node(self,root):
        if root.childNodes:
            for node in root.childNodes:
                doc={}
                if node.nodeType == node.ELEMENT_NODE :
                    print(self.perm_dic)
                    if node.tagName=="pevz:person":
                        if(self.perm_dic and len(self.perm_dic)>=1) and '_id' in self.perm_dic.keys():                
                            db.personal.insert(self.perm_dic)
                            self.perm_dic={}   
                         
                    if(node.hasAttribute('id')):
                            for m in db.personal.find({"_id":node.attributes['id'].value}):
                                doc=m
                                print('Id already exist'+node.attributes['id'].value)    
                            if( not doc):
                                self.perm_dic['_id']=node.attributes['id'].value
                                print(self.perm_dic['_id'])
                    if (node.childNodes and not doc  and not node.hasAttribute('id')):
                        self.perm_dic[node.tagName]=node.firstChild.data
                    
                    self.print_node(node)
                    
## getting the list of persons
#nameParams=['aa','ab','ac','ad','ae']
alphabets=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
nameParams=[]
x,y=0,0
while x<len(alphabets):
    y=0
    while y<len(alphabets):
        nameParams.append(alphabets[x]+alphabets[y])
        y+=1
    x+=1


##scrap files from ekvv to local
for name in nameParams:
    document ='http://ekvv.uni-bielefeld.de/ws/pevz/PersonKerndaten.xml?name='+name
    urllib.request.urlretrieve (document,"PersonKerndaten/PersonKerndaten"+name+".xml")

##read local xml and store to db
for name in nameParams:
    '''web = urllib.request.urlopen(document)
    get_web = web.read()
    dom = md.parseString(get_web)'''
    dom = md.parse("PersonKerndaten/PersonKerndaten"+name+".xml")
    
    if dom.getElementsByTagName('pevz:person').length>0:
        print('--------------'+name+'-----------------------')
        root = dom.documentElement
        tmp=InsertDataFromXml()
        tmp.print_node(root)


#os.system('mongoexport -d kms -c personal_detail -o /home/bando/Desktop/output.txt')
#db.personal_detail.insert(ast.literal_eval(json.dumps(re[n]))  )
#print(perm_dic)    
#for doc in db.personal_detail.find():
   # print(doc)        