# executive_orders.py
===============

This is a little script created to take data from the Federal Register 2.0 API's executive orders dataset to search Wikidata's API for executive order titles. It will print out a list of Wikidata items (Q-numbers) for matching EO numbers, then tally totals for how many were found or are missing from Wikidata. Finally, it prints a list of all EOs it comes across in the FR2 dataset which have malformed EO numbers and couldn't be searched, along with an API query URL which would bring up all of these EOs to look at manually.