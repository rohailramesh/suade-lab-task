# Suade Labs Challenge Task - Rohail Ramesh

This script validates FSA029 XML against specified schema.

## Requirements

Before using this script:

1. Ensure Python is installed on your system

2. Install lxml library (can be found in requirements.txt)

   ```bash
   pip install lxml
   ```

## Executing Script

Run the script as follows:

```bash
python validate_xml.py
```

If submission is validated successfully "Submission Validated Successfully" will be displayed. Else, "Submission Validation Failed" and the error too.

## Answers to the extra mile questions

(a) **What causes it to fail schema validation? Why do you think the regulator has
included a valid file in their examples?**
It is very likely that the regulator would have mismatched the types, or not add elements where it was required to. Looking at the error printed, it would also be possible that the root element does not have a matching global declaration in the schema. By doing so, this would reflect how the validation script handles errors and ensure it detects mismatches in schema definitions.

(b) **How would you fix the file to pass schema validation?**
   Ensuring that the root element and any other elements in the XML file match the declarations defined in the provided XSD schema.

(c) **Why do you think the regulator has included an invalid file in their examples?**
   It help users such as businesses or individuals such as developers and testers to understand schema requirements and common mistakes. This serves as a learning resource, allowing filers to improve accuracy and avoid similar errors in their submissions but also to write documentation for future reference.


---
