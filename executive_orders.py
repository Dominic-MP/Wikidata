#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests, json, wikitools
from wikitools import wiki, api

geturl = 'https://www.federalregister.gov/api/v1/articles.json?fields%5B%5D=abstract&fields%5B%5D=abstract_html_url&fields%5B%5D=action&fields%5B%5D=agencies&fields%5B%5D=agency_names&fields%5B%5D=body_html_url&fields%5B%5D=cfr_references&fields%5B%5D=citation&fields%5B%5D=comments_close_on&fields%5B%5D=correction_of&fields%5B%5D=corrections&fields%5B%5D=dates&fields%5B%5D=docket_id&fields%5B%5D=docket_ids&fields%5B%5D=document_number&fields%5B%5D=effective_on&fields%5B%5D=end_page&fields%5B%5D=excerpts&fields%5B%5D=executive_order_notes&fields%5B%5D=executive_order_number&fields%5B%5D=full_text_xml_url&fields%5B%5D=html_url&fields%5B%5D=json_url&fields%5B%5D=mods_url&fields%5B%5D=page_length&fields%5B%5D=pdf_url&fields%5B%5D=president&fields%5B%5D=public_inspection_pdf_url&fields%5B%5D=publication_date&fields%5B%5D=raw_text_url&fields%5B%5D=regulation_id_number_info&fields%5B%5D=regulation_id_numbers&fields%5B%5D=regulations_dot_gov_info&fields%5B%5D=regulations_dot_gov_url&fields%5B%5D=significant&fields%5B%5D=signing_date&fields%5B%5D=start_page&fields%5B%5D=subtype&fields%5B%5D=title&fields%5B%5D=toc_doc&fields%5B%5D=toc_subject&fields%5B%5D=topics&fields%5B%5D=type&fields%5B%5D=volume&per_page=1000&order=executive_order_number&conditions%5Bpresidential_document_type%5D%5B%5D=executive_order'
parsed = json.loads(requests.get(geturl).text)
rows = parsed['count']

rownumber = 0
foundnumber = 0
missingnumber = 0
errornumber = 0
errorlist = "\n"
errorurl = "\n      https://www.federalregister.gov/api/v1/articles/"

while rownumber < rows :
	
	executive_order_number = parsed['results'][rownumber]['executive_order_number']
	
	if executive_order_number != 0 :
		wikidataurl = 'http://www.wikidata.org/w/api.php?language=en&format=json&action=wbsearchentities&search=Executive%20Order%20' + str(executive_order_number)
		wikidataparsed = json.loads(requests.get(wikidataurl).text)
		try :
			print "\n" + wikidataparsed['search'][0]['id']
			print executive_order_number
			foundnumber = foundnumber + 1
		except IndexError:
			missingnumber = missingnumber + 1
	elif executive_order_number == 0 :
		errornumber = errornumber + 1
		errorlist = errorlist + "\n    " + parsed['results'][rownumber]['title']
		errorurl = errorurl + parsed['results'][rownumber]['document_number'] + ","
	
	rownumber = rownumber + 1

print "\nFound: " + str(foundnumber)
print "Missing: " + str(missingnumber)
print "Errors: " + str(errornumber)
print errorlist
print errorurl[0:-1] + "\n"
print "Full dataset: " + geturl + "\n"