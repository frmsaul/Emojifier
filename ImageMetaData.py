class ImageMetaData:
    def __init__(self, image_location, red_value, blue_value, green_value):
        self.image_location = image_location;
        self.red_value      = red_value;
        self.blue_value     = blue_value;
        self.green_value    = green_value;
        
    def __str__(self):
        return ("ImageMetaData(%s, %f, %f, %f)" % 
                (self.image_location,
                 self.red_value,
                 self.blue_value,
                 self.green_value,));
    
    __repr__ = __str__
