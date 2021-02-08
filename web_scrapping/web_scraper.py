from urllib.request import urlopen
import re

url = "http://olympus.realpython.org/profiles/poseidon"

# returns html details
page = urlopen(url)

# read the page
html_bytes = page.read()
html = html_bytes.decode("utf-8") # returns HTML format

title_index = html.find("<title>")
start_index = title_index + len("<title>")
end_index = html.find("</title>")
title = html[start_index:end_index]

# practicing regular expressions
# a = re.findall("ab*c", "Ac") # returns empty list
a = re.findall("ab*c", "Ac", re.IGNORECASE)

# re.sub() function
string = "Everything is <replaced> if it's in <tags>."
# string = re.sub("<.*>","ELEPHANTS", string) # greedy method
string = re.sub("<.*?>", "ELEPHANTS", string) # non-greedy method

# EXPLANATION
# <title.*?> matches the opening tag from the html
# .*? non-greedily matches all the text after the opening <title> tag
# </title.*?> matches the closing tag
PATTERN = "<title.*?>.*?</title.*?>"
SUB_PATTERN = "<.*?>"
match_results = re.search(PATTERN, html, re.IGNORECASE)
title = match_results.group()
title = re.sub(SUB_PATTERN, "", title)

# EXERCISE
url = "http://olympus.realpython.org/profiles/dionysus"
html = urlopen(url)
page = html.read()
html_open = page.decode("utf-8") 

for string in ["Name: ", "Favorite Color: "]:
    print(string)
    string_start_index = html_open.find(string) + len(string)
    text_start_index = string_start_index 
    
    next_html_tag_offset = html_open[text_start_index:].find("<")
    text_end_index = text_start_index + next_html_tag_offset
    
    
    raw_text = html_open[text_start_index : text_end_index]
    clean_text = raw_text.strip(" \r\n\t")