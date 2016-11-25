import re
import os
import base64
import json

from robobrowser import RoboBrowser

def process_base_64_file(file_name,
                         base64_image):
    with open("%s" % file_name,
              'w') as f:
        f.write(base64.b64decode(base64_image));        

def company_names():
    return ["Brow", "Chart",
            "Appl", "Goog",
            "Twtr", "One",
            "FB","FBM",
            "Sams","Wind",
            "GMail","SB",
            "DCM","KDDI"]

def get_company_name(i):
    return company_names()[i - 2];

def create_work_directory(work_location):
    os.system("mkdir %s" % work_location)
    for company in company_names():
        os.system("mkdir %s/%s" % (work_location,company));

# Crawls the unicode website to get all images.
def fetch_from_the_unicode_website(work_location):
    bs = RoboBrowser(history=True,
                     parser="html.parser")
    bs.open('http://unicode.org/emoji/charts/full-emoji-list.html')
    table_rows = bs.find_all("tr");
    print "Number of Rows %d" % len(table_rows);
    meta_data_dictionary = {};
    for row in table_rows:

        row_cols = row.find_all("td");
        if len(row_cols) == 0:
            continue;
        
        unicode_name = row_cols[1].find("a").attrs["name"];

        meta_data_dictionary[unicode_name] = {
            'actual_name': row_cols[16].contents[0],
            'year_introduced': row_cols[17].contents[0][:4],
            'key_words': map(lambda x : x.contents[0].encode(
                'ascii', 'ignore'),
                             row_cols[18].find_all("a"))
            }

        for i in range(2,len(row_cols)):
            images = row_cols[i].find_all("img");
            if len(images) == 0:
                continue;
            img = images[0];
            base64_value = img.attrs['src'].split(",")[1];
            process_base_64_file(
                "%s/%s/%s.png" % (work_location,
                                  get_company_name(i),
                                  unicode_name) , 
                base64_value);

    # Write Cross Company MetaData to file.
    with open("%s/MetaDataInfo.json" % work_location,
              "w") as f_meta:
        f_meta.write(json.dumps(
            meta_data_dictionary,
            sort_keys = True,
            indent = 4));

    # Convert all Images to RGB .jpg.
    for company in company_names():
        os.system("mogrify -flatten -format jpg %s/%s/*.png -quality 99"
                  % (work_location, company))
        os.system("rm %s/%s/*.png" % (work_location, company))
        os.system("mogrify -colorspace sRGB -type truecolor %s/%s/*.jpg"
                  % (work_location, company))

        

def fetch_files(work_location):
    create_work_directory(work_location)
    fetch_from_the_unicode_website(work_location);
        
if __name__ == "__main__":
    print "Fetching"
    fetch_files("/tmp/Emojis");
