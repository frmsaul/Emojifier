from os import listdir
from os.path import isfile, join
from scipy import misc
import numpy as np
import os
import json

import EmojiFetcher

def get_channel_values(img):
    total_image_size = img.shape[0] * img.shape[1];
    color_sums = np.sum(img, axis=(0,1));
    average_color = (color_sums / float(total_image_size)) / 255.0;
    if (average_color.size == 1):
        return average_color * np.ones(3)
    return average_color

def get_emoji_meta_dictionary(work_location):
    with open("%s/MetaDataInfo.json" % work_location,
              "r") as f_meta:
        emoji_meta_info = json.loads(f_meta.read());
        return emoji_meta_info;

def produce_metadata(work_location,
                     path_to_emoji_files):
    emoji_files = [f for f in listdir(path_to_emoji_files) if
                   isfile(join(path_to_emoji_files, f))
                   and f.endswith(".jpg")]

    print ("Number of Emojis in %s: %d" % (path_to_emoji_files,
                                           len(emoji_files)))
    
    emoji_dictionary = {};
    emoji_meta_info = get_emoji_meta_dictionary(work_location);
    emoji_dictionary["emojis"] = [];
    for file_name in emoji_files:
        file_path = path_to_emoji_files + "/" + file_name;
        number_of_combined_emojis = len( file_name.split("_") )
        img = misc.imread(file_path);
        channel_values = get_channel_values(img)
        file_name_no_extension = file_name[:-4];
        unicode_list = file_name_no_extension.split("_");
        html_name = reduce(lambda x,y : x + y, 
                           map(lambda unicode_emoji:
                               "&#x000" + unicode_emoji,
                               unicode_list))
        emoji_dictionary["emojis"].append(
            {"html_name": html_name,
             "size": img.shape[0:2],
             "channel_values": channel_values.tolist(),
             "number_of_combined_emojis": number_of_combined_emojis,
             "file_path" : file_path,
             "actual_name": emoji_meta_info[file_name_no_extension]
                     ["actual_name"],
             "key_words": emoji_meta_info[file_name_no_extension]
                     ["key_words"],
             "year_introduced": emoji_meta_info[file_name_no_extension]
                     ["year_introduced"]
            }
        )
    with open(path_to_emoji_files + "/EmojisMetaData.json", "w") as f:
        f.write(json.dumps(emoji_dictionary, indent=4));

def get_immediate_subdirectories(a_dir):
    return [name for name in os.listdir(a_dir)
            if os.path.isdir(os.path.join(a_dir, name))]

def preprocess_emojis(work_location):
    EmojiFetcher.fetch_files(work_location)
    paths_to_files = map(lambda x : "%s/%s" % (work_location, x),
                         get_immediate_subdirectories(work_location))
    for path_to_files in paths_to_files:
        print path_to_files;
        produce_metadata(work_location,
                         path_to_files);
    
if __name__ == "__main__":
    preprocess_emojis("/tmp/Emojis");
