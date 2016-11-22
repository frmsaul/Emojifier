from scipy import misc
import numpy as np
from numpy import linalg as LA

import json
import os

import PreProcessor.PreProcessor as PreProcessor

## Uses a Brute force solution to find the single emoji that most
## resembles the image.
def get_closest_emoji(img,
                      emoji_dict = None,
                      verbose = False):

    def l2_metric(v1, v2):
        return ((v1[0] - v2[0])**2
                + (v1[1] - v2[1])**2
                + (v1[2] - v2[2])**2)

    def l1_metric(v1, v2):
        return (abs(v1[0] - v2[0])
                + abs(v1[1] - v2[1])
                + abs(v1[2] - v2[2]))

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
        # Used for Debugging
        def get_rgb_hex(color_array):
            hex_array = map(lambda num:
                            hex(int(num * 255))[2:],
                            color_array)
            concat = reduce(
                lambda x,y: x + y, hex_array);
            return concat

        rgb_channel_values = get_rgb_hex(channel_values)
        print rgb_channel_values
        print channel_values
        print "Min Emoji"
        print get_rgb_hex(min_emoji["channel_values"])
        print json.dumps(min_emoji,
                         indent = 4)
        print "============="
    
    return (min_emoji["actual_name"].encode('ascii', 'ignore'),
            min_emoji["html_name"].encode('ascii', 'ignore'))

# Given an image, the function returns a two dimensional array
# of emojis that ressemble the image.
def image_to_emoji_grid(original,
                        horizontal_grid_size,
                        mapping):
    height, width, rgb_channels = original.shape
    print (height, width, rgb_channels)
    square_size = width / horizontal_grid_size;
    emoji_grid = []
    for row in range(height / square_size):
        emoji_grid.append([])
        for col in range(horizontal_grid_size):
            grid_section = original[
                row * square_size : (row + 1) * square_size,
                col * square_size : (col + 1) * square_size,
                ::]
            emoji_grid[row].append(mapping(grid_section))
    return emoji_grid; 

def emoji_grid_to_html_file(emoji_grid,
                            file_name,
                            font_size):
    with open(file_name, 'w') as f:
        f.write("<html>");
        css = """
                 div {
                    overflow: scroll;
                    white-space:nowrap;
                    font-family: monospace;
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
        for row in emoji_grid:
            for emoji in row:
                f.write("""<span class = \"emoji\" title = \"%s\">%s</span>""" %
                        emoji);
            f.write("<br />")

        f.write("</div> </body>")
        f.write("</html>")

def get_filtered_emoji_list(work_location,
                            company_name):
    def emoji_isnt_too_new(emoji):
        return emoji["year_introduced"] != "2016";

    def emoji_isnt_blood_type(emoji):
        return "blood type" not in emoji["key_words"]
    
    with open("%s/%s/EmojisMetaData.json" %
              (work_location, company_name),
              "r") as f:
        all_emojis = json.load(f);
    
        return filter(lambda x:
                      emoji_isnt_too_new(x) and
                      emoji_isnt_blood_type(x),
                      all_emojis["emojis"]);

def jpg_to_emoji(
        original_image,
        work_location,
        output_html,
        company_name,
        emojis_in_width,
        emoji_font_size):
    
    emoji_list = get_filtered_emoji_list(work_location, company_name)
    valid_emojis_dict = {"emojis": emoji_list};

    emoji_grid = image_to_emoji_grid(misc.imread(original_image),
                                     emojis_in_width,
                                     lambda x:
                                     get_closest_emoji(
                                         x,
                                         emoji_dict = valid_emojis_dict))
   
    # Write into local html file.
    emoji_grid_to_html_file(emoji_grid,
                            output_html,
                            emoji_font_size);

    # Write into AWS s3
    os.system("aws s3 cp %s s3://jpg-to-emoji --region us-east-1" % output_html);
    link = "https://s3.amazonaws.com/jpg-to-emoji/%s" % output_html
    print "Link to view: %s" % link    
    
def main():
    current_work_location = "/tmp/Emojis";
    do_preprocessing = True;
    if (do_preprocessing):
        PreProcessor.preprocess_emojis(current_work_location);
    
    jpg_to_emoji(original_image = "../Resources/Israel.jpg",
                 work_location = current_work_location,
                 output_html = "Israel.html",
                 company_name = "Appl",
                 emojis_in_width = 60,
                 emoji_font_size = 5);
                 
    # upload_file("Poland");
    
if __name__ == "__main__":
    main();
