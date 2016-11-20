import re
import os
import base64
import json

HTML_FOLDER = "BrowserPreProcessing/HTML_FILES"
# Fetch from varius browsers
def fetch_from_browsers():
    def get_all_emojis():
        with open("Images/Safari/EmojisMetaData.json","r") as f:
            emoji_dict = json.load(f);
            return map(
                lambda x: x["html_name"],
                emoji_dict["emojis"]
            );
    
    def produce_html_emojis_file(emojis_per_shard = 1,
                                 row_length = 10,
                                 font_size  = 30):
        
        def produce_emoji_shard_file(emojis,
                                     number = 1):
            with open(HTML_FOLDER + "/Emojis%d.html" % number,
                      "w") as f:
                emoji_number = 0;
                f.write("<html>");
                css = """span.emoji {
                           font-size: %dpx;
                           vertical-align: middle;
                           line-height: 1.5;
                         }""" % font_size
                f.write("<head> <style> %s </style> </head>" % css)

            
                f.write("<body>");
                f.write("\n");
                f.write("<table>")
                f.write("<tr>")
                while (emoji_number < len(emojis)) :
                    f.write("<tr>");
                    for i in range(row_length):
                        if (emoji_number + i >= len(emojis)):
                            break;
                        f.write("<td> <span class = \"emoji\"> %s </td>\n" %
                                emojis[emoji_number + i]);
                    emoji_number += row_length;
                    f.write("</tr>")
                f.write("</table>")
                f.write("</body> </html>");
                
        all_emojis = get_all_emojis();
        shard = 0
        while shard * emojis_per_shard < len(all_emojis):            
            produce_emoji_shard_file(
                all_emojis[shard * emojis_per_shard :
                           (shard + 1) * emojis_per_shard],
                shard);
            shard += 1;

        # Takes Care of reminder of emojis.        
        print "Emojis per shard %s" % emojis_per_shard
        print "number of shards %d" % shard

    # remove existing files
    os.system("rm " + HTML_FOLDER + "/Emojis*");
    
    produce_html_emojis_file(emojis_per_shard = 2000,
                             row_length = 40,
                             font_size = 30);

def update_safari_emoji_list():
    pass;


if __name__ == "__main__":
    print "Fetching"
    fetch_from_browsers();
