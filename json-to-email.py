import json
import urllib.parse
# Load the companies from the JSON file
with open('companies.json') as f:
    companies = json.load(f)

# Define your email template
with open("template.txt") as f:
    email_template = f.read()
with open("subject.txt") as f:
    email_name=urllib.parse.quote(f.read())

# Generate emails for each company
for company in companies:
    email = urllib.parse.quote(email_template.format(company_name=company['name']))
    email_link = "mailto:" + f"{company['email']}?subject={email_name}&body={email}"
    # print(f"<a href=\"{email_link}\"> text</a>")
    print(email_link)
    

