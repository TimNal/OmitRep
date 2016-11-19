'''
Created on 13.11.2016

@author: Someone / Timo
'''


#import os, os.path, sys
import sys
import glob
from sys import argv
from xml.etree import ElementTree


def main(argv):
    path = argv[1]
    xml_files = glob.glob(path +"/*.xml")
    xml_element_tree = None
    for xml_file in xml_files:
        data1 = ElementTree.parse(xml_file)
        data = data1.getroot()
        # print ElementTree.tostring(data)
        for result in data.iter('filters'):
            if xml_element_tree is None:
                xml_element_tree = data 
                insertion_point = xml_element_tree.findall("./filters")[0]
            else:
                insertion_point.extend(result) 
    if xml_element_tree is not None:
        print(ElementTree.tostring(xml_element_tree))
        
if __name__ == '__main__':
    sys.exit(main(argv))
      
        