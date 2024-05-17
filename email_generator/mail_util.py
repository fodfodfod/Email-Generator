import os
import mimetypes

# Builds an attachment into an array of values so it can be passed around as an object
def build_attachment(path):
	type_subtype, _ = mimetypes.guess_type(path)
	maintype, subtype = type_subtype.split("/")

	with open(path, "rb") as fp:
		attachment_data = fp.read()
	
	return {
		'data': attachment_data,
		'name': os.path.basename(path),
		'maintype': maintype,
		'subtype': subtype,
	}