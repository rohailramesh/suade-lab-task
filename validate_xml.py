'''
Suade Lab Task - Author : @Rohail Ramesh
'''

from lxml import etree
from pathlib import Path

def validate_submission(xsd_schema_path, xml_submission_path):
    # Get the script directory and construct relative paths
    script_dir = Path(__file__).resolve().parent
    xsd_schema_path = script_dir / xsd_schema_path
    xml_submission_path = script_dir / xml_submission_path
    # Created an XMLSchema object and an XMLParser
    fsa_schema = etree.XMLSchema(etree.parse(xsd_schema_path))
    xml_parser = etree.XMLParser(schema=fsa_schema)

    #try to parse the xml and raise an exception if it fails
    try:
        etree.parse(xml_submission_path, xml_parser) 
        print("Submission Validated Successfully")
    except Exception as error:
        print(f"Submission Validation Failed: \n{error}")

if __name__ == "__main__":
    xsd_schema_path = "CommonTypes-Schema.xsd" 
    xml_submission_path = "FSA029-Sample-Full.xml"  
    validate_submission(xsd_schema_path, xml_submission_path)