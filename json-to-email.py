import json
import urllib.parse
# Load the companies from the JSON file
with open('companies.json') as f:
    companies = json.load(f)

# Define your email template
email_template = """Dear {company_name},

We are pleased to inform you that your company has been selected for a special offer. 
Please find attached the details of the offer.

Best regards,
Your Company"""
email_name=urllib.parse.quote("Give us money please!!!!")

# Generate emails for each company
for company in companies:
    email = urllib.parse.quote(email_template.format(company_name=company['name']))
    email_link = "mailto:" + f"{company['email']}?subject={email_name}&body={email}"
    # print(f"<a href=\"{email_link}\"> text</a>")
    print(email_link)
    

