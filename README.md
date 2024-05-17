# Email Generator

## Installation
Go to [zip](https://github.com/roboblazers7617/2024Robot/archive/refs/heads/main.zip). Or go to Code > download zip

## Setup
Run `setup.sh` (can be run by simply double-clicking on the file)
### Set up the Google API
Follow the guide at https://developers.google.com/gmail/api/quickstart/python#set_up_your_environment to generate OAuth2 credentials, and, when you are at the step to configure the OAuth consent screen, add the `gmail.compose` scope so the script can edit drafts. Download them into `.credentials/credentials.json` (you will have to create this directory yourself, and show hidden files to see it on MacOS).
### Set up the template
- update the email template in `email_generator/email_creator.py`
- put the file paths to any attachments in the `attachment_paths` list in `email_generator/__main__.py`

## Usage
### Prepare data
- copy and paste the table into `email-template.txt`
- make sure there is nothing else in the file
- save it
### Run the program
Run `run.sh` (can be run by double-clicking as well)
The first time it is run, you will need to authenticate with the account that you want to upload the drafts to. A browser window should be opened automatically to do this in (if it is not, copy and paste the URL from the terminal window into your browser). The authentication flow may not work in Firefox or other Gecko-based browsers, so try Chrome, Safari, or another Chromium- or Webkit-based browser if it doesn't work for you.