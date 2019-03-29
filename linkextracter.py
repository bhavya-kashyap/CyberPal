import re
import Read


print Read.read_email_from_gmail().email_body
link_pattern = re.compile('<a[^>]+href=\'(.*?)\'[^>]*>(.*)?</a>')
search = link_pattern.search(Read.email_body)
if search is not None:
    print("Link found! -> " + search.group(0))
else:
    print("No links were found.")
