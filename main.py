from Emojify.jpg_to_emoji_convertor import jpg_to_emoji

import gflags
import wget
import os
from google.apputils import app

FLAGS = gflags.FLAGS

gflags.DEFINE_string('src_image',
                     '',
                     'the image you want to transform')
gflags.DEFINE_string('work_location',
                     "/tmp/Emojis",
                     'the location where the emojis will be generated')
gflags.DEFINE_string('output_html',
                     'output.html',
                     'The output html')
gflags.DEFINE_enum('company',
                   'Appl',
                   ["Brow", "Chart",
                    "Appl", "Goog",
                    "Twtr", "One",
                    "FB","FBM",
                    "Sams","Wind",
                    "GMail","SB",
                    "DCM","KDDI"],
                   'the emoji implementation')
gflags.DEFINE_integer('emojis_in_width',
                      60,
                      'Number of emojis to compose',
                      lower_bound=0)
gflags.DEFINE_integer('font_size',
                      5,
                      'The font size in the resulting html',
                      lower_bound=0)
gflags.DEFINE_boolean('do_preprocessing',
                      False,
                      'should you refetch the emojis')

def main(argv):
    if(len(FLAGS.src_image) == 0):
        print "src_image can't be empty"
        return 1;

    if(FLAGS.src_image.startswith("http")):
        # Download image
        tmp_file_name = "/tmp/%s" % (FLAGS.src_image.split("/")[-1])
        wget.download(FLAGS.src_image, out=tmp_file_name);
    else:
        tmp_file_name = FLAGS.src_image

    jpg_to_emoji(
        original_image = tmp_file_name,
        work_location = FLAGS.work_location,
        output_html = FLAGS.output_html,
        company_name = FLAGS.company,
        emojis_in_width = FLAGS.emojis_in_width,
        emoji_font_size = FLAGS.font_size,
        do_preprocessing = FLAGS.do_preprocessing);

    # Write into AWS s3. Used by Saul for debugging.
    os.system("aws s3 cp %s s3://jpg-to-emoji --region us-east-1" %
              FLAGS.output_html);
    link = "https://s3.amazonaws.com/jpg-to-emoji/%s" % FLAGS.output_html
    print "Link to view: %s" % link    

if __name__ == '__main__':
  app.run()
