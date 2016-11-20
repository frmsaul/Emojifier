import re
import os
import base64
import json

from robobrowser import RoboBrowser

def process_base_64_file(file_name,
                         base64_image):
    with open("Images/%s.jpg" % file_name, 'w') as f:
        f.write(base64.b64decode(base64_image));        

def get_company_name(i):
    names = ["Brow", "Chart",
             "Appl", "Goog",
             "Twtr", "One",
             "FB","FBM",
             "Sams","Wind",
             "GMail","SB",
             "DCM","KDDI"]
    return names[i - 2];

# Crawls the unicode website to get all images.
def fetch_from_the_unicode_website():
    bs = RoboBrowser(history=True,
                     parser="html.parser")
    bs.open('http://unicode.org/emoji/charts/full-emoji-list.html')
    table_rows = bs.find_all("tr");
    print "Number of Rows %d" % len(table_rows);
    for row in table_rows:

        row_cols = row.find_all("td");
        if len(row_cols) == 0:
            continue;

        print "number of Cols: %d" % len(row_cols);
        
        unicode_name = row_cols[1].find("a").attrs["name"];
        print unicode_name
        for i in range(2,len(row_cols)):
            images = row_cols[i].find_all("img");
            if len(images) == 0:
                continue;
            img = images[0];
            base64_value = img.attrs['src'].split(",")[1];
            process_base_64_file(
                "%s/%s" % (get_company_name(i), unicode_name) , 
                base64_value);


if __name__ == "__main__":
    print "Fetching"
    fetch_from_unicode_website();
