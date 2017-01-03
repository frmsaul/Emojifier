import numpy as np
import scipy.spatial as sp

def l2_metric(v1, v2):
    return ((v1[0] - v2[0])**2
            + (v1[1] - v2[1])**2
            + (v1[2] - v2[2])**2)

def l1_metric(v1, v2):
    return (abs(v1[0] - v2[0])
            + abs(v1[1] - v2[1])
            + abs(v1[2] - v2[2]))

class EmojiMapper:
    def __init__(self,
                 emoji_dict,
                 use_kd_tree):
        self.emoji_dict = emoji_dict
        self.use_kd_tree = use_kd_tree
        if(use_kd_tree):
            data_points = map(lambda x: x["channel_values"],
                              self.emoji_dict["emojis"])
            self.kd_tree = sp.KDTree(data_points)
    
    # Given an image, returns the emoji that most ressembles it.
    def get_closest_emoji(self,
                          img,
                          verbose = False):

        total_image_size = img.shape[0] * img.shape[1];
        color_sums = np.sum(img, axis=(0,1));
        if total_image_size == 0:
            channel_values = [0,0,0]
        else:
            channel_values  = (color_sums / (float(total_image_size) * 255.0) );
        
        ## Find best emoji.
        if self.use_kd_tree:
            distance_to_best, best_index = self.kd_tree.query(
                channel_values[:3])
            min_emoji = self.emoji_dict["emojis"][best_index]
        else:
            min_emoji = min(
                self.emoji_dict["emojis"],
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

        return min_emoji
