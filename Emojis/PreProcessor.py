from os import listdir
from os.path import isfile, join
from scipy import misc
import matplotlib.pyplot as plt
import numpy as np
import os
import json

def get_channel_values(img):
    total_image_size = img.shape[0] * img.shape[1];
    color_sums = np.sum(img, axis=(0,1));
    average_color = (color_sums / float(total_image_size)) / 255.0;
    return average_color

def produce_metadata(path_to_emoji_files):
    emoji_files = [f for f in listdir(path_to_emoji_files) if
                   isfile(join(path_to_emoji_files, f))
                   and f.endswith(".jpg")]

    print ("Number of Emojis in %s: %d" % (path_to_emoji_files,
                                           len(emoji_files)))
    
    emoji_dictionary = {};
    emoji_dictionary["emojis"] = [];
    for file_name in emoji_files:
        file_path = path_to_emoji_files + "/" + file_name;
        number_of_combined_emojis = len( file_name.split("_") )
        img = misc.imread(file_path);
        channel_values = get_channel_values(img)
        file_name_no_extension = file_name[:-4].split("_");
        html_name = reduce(lambda x,y : x + y, 
                           map(lambda unicode_emoji:
                               "&#x000" + unicode_emoji,
                               file_name_no_extension))
        emoji_dictionary["emojis"].append(
            {"html_name": html_name,
             "size": img.shape[0:2],
             "channel_values": channel_values.tolist(),
             "number_of_combined_emojis": number_of_combined_emojis,
             "file_path" : file_path
            }
        )
    with open(path_to_emoji_files + "/EmojisMetaData.json", "w") as f:
        f.write(json.dumps(emoji_dictionary, indent=4));

def get_immediate_subdirectories(a_dir):
    return [name for name in os.listdir(a_dir)
            if os.path.isdir(os.path.join(a_dir, name))]

def main():
    paths_to_files = map(lambda x : "Images/%s" % x,
                         get_immediate_subdirectories("Images"))
    for path_to_files in paths_to_files:
        produce_metadata(path_to_files);

    
if __name__ == "__main__":
    main();



## ______DATA EXAMPLE________
## HTML_UNICODE: STR
## FILE_LOCATION: STR
## NUMBER_OF_COMBINED_EMOJIS: INT
## RBG: [R, B, G]
