## This piece of software process the emoji images and records their meta data.
## The metadata is later used in the image processing software

# Implement the following two methods:
# 1. get_emojis_in_folder
# 2. get_image_meta_data
# You can run this by typing: python pre_processor into your terminal

from ImageMetaData import ImageMetaData


## Given a folder name, return a list with PATHS to the image files in this folder
## Just google how to do it.
def get_emojis_in_folder(folder_name):
    return ["Image1", "ETc."];


## This function returns the image meta data given the image's address (on your computer) 
## To get the metadata, you would have to use a library that can process the image file
## I suggest using OpenCV
def get_image_meta_data(image_address):
    red = 0.0 #?
    blue = 0.0 #?
    green = 0.0 #?
    return ImageMetaData(image_address, 0.5, 0.2, 0.3);


def main():
    emoji_folder = "./Emojis/TwitterEmojis/"
    emoji_files_address = get_emojis_in_folder(emoji_folder);
    MetaData = map(get_image_meta_data, emoji_files_address);
    
    print(MetaData);


if __name__ == "__main__":
    main();
