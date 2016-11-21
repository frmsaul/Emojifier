from scipy import misc
import numpy as np
from numpy import linalg as LA

import json
import os

### Useful s3 commands
### aws s3 cp workfile2.html s3://jpg-to-emoji --region us-east-1
### aws s3 ls s3://jpg-to-emoji --region us-east-1
### Read from s3
### https://s3.amazonaws.com/jpg-to-emoji/workfile.html

def get_all_emojis():
    with open("Emojis/Images/Appl/EmojisMetaData.json","r") as f:
        emoji_dict = json.load(f);
    return emoji_dict;

def l2_metric(v1, v2):
    return ((v1[0] - v2[0])**2
            + (v1[1] - v2[1])**2
            + (v1[2] - v2[2])**2)

def l1_metric(v1, v2):
    return (abs(v1[0] - v2[0])
            + abs(v1[1] - v2[1])
            + abs(v1[2] - v2[2]))

def get_rgb_hex(color_array):
    hex_array = map(lambda num:
                    hex(int(num * 255))[2:],
                    color_array)
    concat = reduce(
        lambda x,y: x + y, hex_array);
    return concat

def get_dominant_color_text(img,
                            emoji_dict = get_all_emojis(),
                            verbose = False):
    total_image_size = img.shape[0] * img.shape[1];
    color_sums = np.sum(img, axis=(0,1));

    channel_values  = (color_sums / (float(total_image_size) * 255.0) );
    ## Find best emoji index
    min_emoji = min(
        emoji_dict["emojis"],
        key = lambda x:
           l1_metric(x["channel_values"], channel_values)
    )
    if verbose:
        rgb_channel_values = get_rgb_hex(channel_values)
        print rgb_channel_values
        print channel_values
        print "Min Emoji"
        print get_rgb_hex(min_emoji["channel_values"])
        print json.dumps(min_emoji,
                         indent = 4)
        print "============="
    
    return (min_emoji["actual_name"],
            min_emoji["html_name"])

def process_image_to_text(original,
                          horizontal_grid_size,
                          mapping):
    height, width, rgb_channels = original.shape
    print (height, width, rgb_channels)
    square_size = width / horizontal_grid_size;
    result_text = "";
    for row in range(height / square_size):
        for col in range(horizontal_grid_size):
            grid_section = original[
                row * square_size : (row + 1) * square_size,
                col * square_size : (col + 1) * square_size,
                ::]
            result_text += ("""<span class = \"emoji\" 
                                     title = \"%s\">
                                %s 
                               </span>""" % mapping(grid_section));

        result_text += "<br />"
    return result_text; 

def text_to_html_file(text,
                      file_name,
                      font_size = 10):
    with open(file_name, 'w') as f:
        f.write("<html>");

        css = """
                 div {
                    overflow: scroll;
                    white-space:nowrap
                 }
                 span.emoji {
                   font-size: %dpx;
                   vertical-align: middle;
                   line-height: 1.5;
                 }""" % font_size
        
        f.write("<head>")
        f.write("<style> %s </style>" % css)
        f.write("</head>")

        f.write("<body> <div>")
        #        print text[306900 - 200: 306900 + 200]
        f.write(text.encode('ascii', 'ignore'));
        f.write("</div> </body>")
        f.write("</html>")

def upload_file(name):
    f = misc.imread('Resources/%s.jpg' % name);

    def emoji_isnt_too_new(emoji):
        return emoji["year_introduced"] != "2016";

    def emoji_isnt_blood_type(emoji):
        return "blood type" not in emoji["key_words"]
    
    emoji_list = filter(
        lambda x:
        emoji_isnt_too_new(x) and
        emoji_isnt_blood_type(x),
        get_all_emojis()["emojis"]);
    valid_emojis_dict = {}
    valid_emojis_dict["emojis"] = emoji_list;
    
    text = process_image_to_text(f,
                                 240,
                                 lambda x:
                                 get_dominant_color_text(
                                     x,
                                     emoji_dict = valid_emojis_dict))
    #    print text
    text_to_html_file(text, name + ".html");
    os.system("aws s3 cp %s.html s3://jpg-to-emoji --region us-east-1" % name);
    link = "https://s3.amazonaws.com/jpg-to-emoji/%s.html" % name
    print "Link to view: %s" % link
        
def main():
    upload_file("Poland");
    
if __name__ == "__main__":
    main();
