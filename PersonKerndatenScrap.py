import xml.dom.minidom as  md
import urllib.request


def print_node(root):
	if root.childNodes:
		for node in root.childNodes:
			if node.nodeType == node.ELEMENT_NODE:
				if node.childNodes and not node.hasAttribute('id'):
						print(node.tagName,"has value:",  node.firstChild.nodeValue)
				else:
					if node.tagName=="pevz:person":
						print(node.tagName)
				print_node(node)


nameParams=['aa','ab','ac']

for name in nameParams:
	document ='http://ekvv.uni-bielefeld.de/ws/pevz/PersonKerndaten.xml?name='+name
	urllib.request.urlretrieve (document, "PersonKerndaten/PersonKerndaten"+name+".xml")

for name in nameParams:
	'''web = urllib.request.urlopen(document)
	get_web = web.read()
	dom = md.parseString(get_web)'''
	dom = md.parse("PersonKerndaten/PersonKerndaten"+name+".xml")
	if dom.getElementsByTagName('pevz:person').length>0:
		print('--------------'+name+'-----------------------')
		root = dom.documentElement
		print_node(root)