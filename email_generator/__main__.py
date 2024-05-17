import json
import concurrent.futures
import fileinput

import gmail
import mail_util
import email_creator

# File paths
# TODO: Move these to global paths
google_token_path = ".credentials/token.json"
google_oauth_credentials_path = ".credentials/credentials.json"
# TODO: Pull attachments from a directory
attachment_paths = []

if __name__ == "__main__":
	# Load the companies from the JSON file
	print("Processing input data")
	json_data = ""
	for line in fileinput.input():
		json_data += line
	companies = json.loads(json_data)

	# Authenticate with Google
	print("Authenticating")
	creds = gmail.get_creds(google_token_path, google_oauth_credentials_path)

	# Build all of the attachments
	print("Processing attachments")
	attachments = []
	with concurrent.futures.ProcessPoolExecutor() as executor:
		for attachment_path in attachment_paths:
			attachments.append(mail_util.build_attachment(attachment_path))

	print("Generating and uploading E-mails")
	with concurrent.futures.ProcessPoolExecutor() as executor:
		for company in companies:
			gmail.create_draft(creds, email_creator.create_email_body(company, attachments))