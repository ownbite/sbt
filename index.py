import json

from google_spreadsheet.api import SpreadsheetAPI
from flask import Flask, render_template, url_for


app = Flask(__name__)

@app.route('/')
def index():
	jsonarray = 'yolo'

	return render_template('startpage.html', 
								data=jsonarray, 
								js_file_klass=url_for('static', filename='js/klass.js'))


def test():
	api = SpreadsheetAPI('sbt.testperson@gmail.com', 'mintkaka2010', '')

	spreadsheets = api.list_spreadsheets()
	print spreadsheets
	 
	worksheets = api.list_worksheets(spreadsheets[0][1])
	print worksheets

	sheet = api.get_worksheet(spreadsheets[0][1], worksheets[3][1])
	return sheet.get_rows()


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80, debug=True)











# from gdata.spreadsheet.service import SpreadsheetsService, ListQuery
# import xml.dom.minidom




# # Create a client class which will make HTTP requests with Google Docs server.
# client = SpreadsheetsService()

# # Authenticate using your Google Docs email address and password.
# client.ClientLogin('sbt.testperson@gmail.com', 'mintkaka2010')

# # Query the server for an Atom feed containing a list of your documents.
# spreadsheet_feed = client.GetSpreadsheetsFeed()

# # print spreadsheet_feed

# # String -> String
# # produce the id from url
# def extract_id(s):
# 	return s.split('/')[-1]


# # # # Loop through the feed and extract each document entry.
# for spreadsheet_feed in spreadsheet_feed.entry:

#  	# Display the title of the document on the command line.
#  	# result = client.GetListFeed( '1_TDNusJah6VSKah-jiH7rlsKWtQc82LGTV62DJ5NErc' ) 
#  	print spreadsheet_feed.content.text
#  	print spreadsheet_feed.id.text
 	
#  	for w in client.GetWorksheetsFeed( extract_id(spreadsheet_feed.id.text) ).entry:

#  		print extract_id(w.id.text)

#  		extract_id(w.id.text)

#  		print w.content.text

#  		if w.content.text == 'Reklamytor':
 				
# 			print type(client.GetListFeed( extract_id(spreadsheet_feed.id.text), extract_id(w.id.text) )) 			

#  			for row in client.GetListFeed( extract_id(spreadsheet_feed.id.text), extract_id(w.id.text) ).entry:
#  				print type(row.content)
#  				print row.content.text



# # 	print type(result)
# # 	pprint.pprint(result) 
	 
	
# # for l in client.GetListFeed( '1_TDNusJah6VSKah-jiH7rlsKWtQc82LGTV62DJ5NErc' ).entry:


	
# # 	print l.content.text

