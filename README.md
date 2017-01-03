#####################################INTRO#####################################

ImgToEmoji Converter

The

####################################INSTALL#####################################
You can install the software by running: 
bash install.sh

#####################################HOW TO USE#################################

The command lines are specified as follows: 
  --company: <Brow|Chart|Appl|Goog|Twtr|One|FB|FBM|Sams|Wind|GMail|SB|DCM|KDDI>: the
    emoji implementation
    (default: 'Appl')
  --[no]do_preprocessing: should you refetch the emojis
    (default: 'false')
  --emoji_size: The font size in the resulting html.May also be the size in pixels of
    each emoji.outputed by the converter.
    (default: '5')
    (a non-negative integer)
  --emojis_in_width: Number of emojis to compose
    (default: '60')
    (a non-negative integer)
  --output_file: The output file
    (default: 'output.html')
  --src_image: the image you want to transform
    (default: '')
  --[no]use_kd_tree: Use kd_tree instead of brute force.
    (default: 'false')
  --work_location: the location where the emojis will be generated
    (default: '/tmp/Emojis')
