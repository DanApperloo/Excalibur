from Utilities.LoggingUtilities.LoggingUtil import *
from xml.dom.minidom import parse, parseString
import xml.etree.ElementTree as ET
from lxml import etree
class Factory(object):

    logger = LoggingUtil("Factory")
    
    def __init__(self, schemaIn):
        fschema = open(schemaIn)
        schema_doc = etree.parse(fschema)
        self.schema = etree.XMLSchema(schema_doc)             
        self.elementa = ""
        self.elementb = ""
        
        
    def Getelement(self,filename,element):
        self.element =filename.__getattribute__(element)

    def Compareelemnet(self,filename3,element,filename4,element2):
            self.elementa = filename3.getattribute(element)
            self.elementb = filename4.getattribute(element2)
             
            if self.elementa == self.elementb :
                    return True
            else :
                    return False
        

    def printfile(self):
        print(self.filetxt)
        print(self.filetxt1)
        
        
    def Schemavalidate(self,xml):
       
        fsource = open(xml)
        try:
            doc = etree.parse(fsource)
            return [self.schema.validate(doc),doc]
        except etree.XMLSyntaxError as e:
            # this exception is thrown on schema validation error
            print e


