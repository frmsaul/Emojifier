from scipy import misc
import numpy as np
from numpy import linalg as LA

import json

import PreProcessor.PreProcessor as PreProcessor
import EmojiMapper

# Given an image, the function returns a two dimensional array
# of emojis that ressemble the image.
def image_to_emoji_grid(original,
                        horizontal_grid_size,
                        emoji_mapper):
    height, width, rgb_channels = original.shape
    print (height, width, rgb_channels)
    square_size = width / horizontal_grid_size;
    vertical_grid_size = height / square_size

    # Pre allocated list 
    squares_to_process = [original[
        row * square_size : (row + 1) * square_size,
        col * square_size : (col + 1) * square_size,
        ::]
                            for col in range(horizontal_grid_size)
                            for row in range(vertical_grid_size)]
    
    emojis = map(emoji_mapper.get_closest_emoji, squares_to_process);
    print "Done Peralllel"
    
    # We now need to reshape the emojis.
    emoji_grid = [[None for col in range(horizontal_grid_size)]
                  for row in range(vertical_grid_size)]

    for row in range(vertical_grid_size):
        for col in range(horizontal_grid_size):
            emoji_grid[row][col] = (
                emojis[col * vertical_grid_size + row])

    print len(emoji_grid), len(emoji_grid[0])
    print vertical_grid_size, horizontal_grid_size
            
    return emoji_grid; 

# Given a grid of emojis, this will produce an html file in the file_name
# location. The emoji font size would be set to font_size.
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
                f.write("<span class = \"emoji\""
                        "title = \"%s\">%s</span>" %
                        (emoji["actual_name"].encode('ascii', 'ignore'),
                         emoji["html_name"].encode('ascii', 'ignore')));
            f.write("<br />")

        f.write("</div> </body>")
        f.write("</html>")

# Return a list of filtered emojis. Some emojis didn't make the list, either
# because they look ugly, or they arent widely supported. 
def get_filtered_emoji_list(work_location,
                            company_name):
    def emoji_isnt_too_new(emoji):
        return emoji["year_introduced"] != "2016";
    
    def emoji_isnt_too_old(emoji):
        return emoji["year_introduced"] != "1995";
    
    def emoji_isnt_blood_type(emoji):
        return "blood type" not in emoji["key_words"]

    def emoji_isnt_a_square(emoji):
        return (emoji["actual_name"] != "white small square" and
                emoji["actual_name"] != "black medium square" and
                emoji["actual_name"] != "black small square" and
                emoji["actual_name"] != "white medium square")
    
    def emoji_isnt_japanese_alphabet(emoji):
        return ("katakana" not in emoji["key_words"] and
                "ideograph" not in emoji["key_words"])
    
    def emoji_isnt_bullshit(emoji):
        return ("information" != emoji["actual_name"] and
                "warning" != emoji["actual_name"] and
                "baseball" != emoji["actual_name"])

    def emoji_isnt_punctioation(emoji):
        return "punctuation" not in emoji["key_words"]
    
    with open("%s/%s/EmojisMetaData.json" %
              (work_location, company_name),
              "r") as f:
        all_emojis = json.load(f);
    
        return filter(lambda x:
                      emoji_isnt_too_new(x) and
                      emoji_isnt_blood_type(x) and
                      emoji_isnt_a_square(x) and
                      emoji_isnt_too_old(x) and
                      emoji_isnt_japanese_alphabet(x) and
                      emoji_isnt_bullshit(x) and
                      emoji_isnt_punctioation(x),
                      all_emojis["emojis"]);

# Most important function in this file.
# Takes care of the conversion process. 
def jpg_to_emoji(
        original_image,
        work_location,
        output_html,
        company_name,
        emojis_in_width,
        emoji_font_size,
        do_preprocessing):
    
    if (do_preprocessing):
        PreProcessor.preprocess_emojis(work_location);
    
    emoji_list = get_filtered_emoji_list(work_location, company_name)
    valid_emojis_dict = {"emojis": emoji_list};


    emoji_mapper = EmojiMapper.EmojiMapper(emoji_dict = valid_emojis_dict)
    emoji_grid = image_to_emoji_grid(misc.imread(original_image),
                                     emojis_in_width,
                                     emoji_mapper)
   
    # Write into local html file.
    emoji_grid_to_html_file(emoji_grid,
                            output_html,
                            emoji_font_size);    
