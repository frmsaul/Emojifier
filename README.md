# Emojifier
You can use Emojifier to turn your images into beautiful "Emoji Mosaics".

The Emojifier works as follows: Images are divided to a grid, and finds the "best fit" emoji for each square in the grid using an Octree 🐙🌲.

# Install

1. Install python and pip

2. Install packages (specified at requirements.txt)
   You can install everything by running ```pip install -r requirements.txt```

3. Install Install the ImageMagick CLI.

If you have trouble installing, talk to me (@frmsaul). I always have trouble
setting up software too, so would love to help a fellow straggler. 

# Usage
You can emojify by running:

```python emoji.py [FLAGS]```

Where the flags are specified here:
```
  --company: <Brow|Chart|Appl|Goog|Twtr|One|FB|FBM|Sams|Wind|GMail|SB|DCM|KDDI>: the
    emoji implementation
    (default: 'Appl')
  --emoji_size: The font size in the resulting html.May also be the size in pixels of
    each emoji.outputed by the converter.
    (default: '10')
    (a positive integer)
  --emojis_in_width: Number of emojis to compose
    (default: '60')
    (a non-negative integer)
  --output_file: The output file, can be either .png or .html
    (default: 'output.html')
  --src_image: the image you want to transform, it may be either a local image or an
    image from the world wide web
    (default: '')
  --[no]use_kd_tree: Use kd_tree instead of brute force.
    (default: 'true')
  --work_location: the location where the emojis will be generated
    (default: '/tmp/Emojis')
```
## Usage Examples:

### Produce a .jpg:

```python emoji.py --src_image https://s3.amazonaws.com/jpg-to-emoji/RealPink.png --output_file DarkSide.png```

### Produce an .html:

```python emoji.py --src_image https://s3.amazonaws.com/jpg-to-emoji/RealPink.png --output_file DarkSide.html```

### Higher Emojis in width:

```python emoji.py --src_image https://s3.amazonaws.com/jpg-to-emoji/RealPink.png --output_file DarkSide.html --emojis_in_width 130```

### Large Emoji Size:

```python emoji.py --src_image https://s3.amazonaws.com/jpg-to-emoji/RealPink.png --output_file DarkSide.png --emojis_in_width 130 --emoji_size 50```

# Examples: 
If you are using a small screen (like on a phone), these might not look too good because of break lines. If this is the case, I recommend checking this out on a larger screen. Meanwhile enjoy this [html example](https://s3.amazonaws.com/jpg-to-emoji/like.html), and this image:

![alt text](https://s3.amazonaws.com/jpg-to-emoji/smile.png "Warhol soup can")

## Google 
🌩🌩🌩🌩🌩🌩🌩🌩🌩🌩🌩🌩🌩🌩🌩🌩🌩🌩🌩🌩🌩🌩🌩🌩🌩🌩🌩🌩🌩🌩  
🌩🌩🌩🌩🌩🌩🌩🌩🌩🌩🌩🌩🐖🚨🌺🌺❌📌🌩🌩🌩🌩🌩🌩🌩🌩🌩🌩🌩🌩  
🌩🌩🌩🌩🌩🌩🌩🌩🌩🌩🌩📮🆘🆘🆘🆘🆘🆘🔴💉🌩🌩🌩🌩🌩🌩🌩🌩🌩🌩  
🌩🌩🌩🌩🌩🌩🌩🌩🌩🌩❌🆘🆘🆘🔴🔴🆘🆘🌺💭🌩🌩🌩🌩🌩🌩🌩🌩🌩🌩  
🌩🌩🌩🌩🌩🌩🌩🌩🌩⛱🆘🆘🔴🐖🌩🌩🍸🚫💭🌩🌩🌩🌩🌩🌩🌩🌩🌩🌩🌩  
🌩🌩🌩🌩🌩🌩🌩🌩🌩📴📳🆘🔖🌩🌩🌩🌩🌩🌩🌩🌩🌩🌩🌩🌩🌩🌩🌩🌩🌩  
🌩🌩🌩🌩🌩🌩🌩🌩🌩📳📳🤗🌩🌩🌩💙💙💙💙💙💙🌬🌩🌩🌩🌩🌩🌩🌩🌩  
🌩🌩🌩🌩🌩🌩🌩🌩🌩📳📳🤔🌩🌩🌩🛄🚹🚹🚹🚹🚹🌧🌩🌩🌩🌩🌩🌩🌩🌩  
🌩🌩🌩🌩🌩🌩🌩🌩🌩📳📳👩🌩🌩🌩💙💙💙🛄🚹🛂🌬🌩🌩🌩🌩🌩🌩🌩🌩  
🌩🌩🌩🌩🌩🌩🌩🌩🌩🌕🖼💹🏌🌩🌩🌩🌩🌬🛄🚹🛄🌩🌩🌩🌩🌩🌩🌩🌩🌩  
🌩🌩🌩🌩🌩🌩🌩🌩🌩🏝✅✅💹🏄🌩🌩🗡📘🚹🚹🌀🌩🌩🌩🌩🌩🌩🌩🌩🌩   
🌩🌩🌩🌩🌩🌩🌩🌩🌩🌩♻✅✅✅💹💹✅✅🏧🛄🌬🌩🌩🌩🌩🌩🌩🌩🌩🌩   
🌩🌩🌩🌩🌩🌩🌩🌩🌩🌩🌩🌲💹✅✅✅✅✅🚛🗯🌩🌩🌩🌩🌩🌩🌩🌩🌩🌩   
🌩🌩🌩🌩🌩🌩🌩🌩🌩🌩🌩🌩🗯🌲♻♻♻🏌🌩🌩🌩🌩🌩🌩🌩🌩🌩🌩🌩🌩🌩   

## Facebook 
🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱   
🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱   
🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱   
🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🆕🚈🚈⏩🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱   
🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🚆🌌🎦🔠🌌🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱   
🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🌌🎣🖱🖌🌌🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱   
🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱⛴🌌🖱🌩🛰🌑🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱   
🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🌌⛴🖱🍴🚈⏩🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱   
🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🎣🌌🖱🖱💬🌃🎦🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱   
🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖲🚆🖱🖱🗡🌃🎦🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱    
🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🛬🌌🖱🖱🖱🔧🌃🎦🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱   
🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🌃🔄🖱🖱🖱🍴🚈🌌🌌🌌🌌🌃🛫🖱🖱🖱🖱🖱    
🖱🌌⚫⚫⚫⚫⚫⚫🖲🖱🌨🌃🌑🖱🖱🖱🖱🖱🖱🍬🍬🍬🍬🔄🌌🍬🖱🖱🖱🖱    
🖱🌌🌃🌃🌃🌃🌃🌃🌌🌃🌌🚈🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🌌🎐🖱🖱🖱🖱    
🖱🌌🌃🌃🌃🌃🌃🌃🌌👥🍬🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🌌🎐🖱🖱🖱🖱    
🖱🌌🌌🌌🌌🌌🌌🌌🌌🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🌌🎐🖱🖱🖱🖱    
🖱🌌🌌🌌🌌🌌🌌🌌🌌🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🌌🎐🖱🖱🖱🖱    
🖱🌌🌌🌌🌌🌌🌌🌌🌌🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🌌🎐🖱🖱🖱🖱    
🖱🌌🌌🌌🌌🌌🌌🌌🌌🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🌌🎐🖱🖱🖱🖱     
🖱🌌🌌🌌🌌🌌🌌🌌🌌🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🌌🎐🖱🖱🖱🖱    
🖱🌌🌌🌌🌌🌌🌌🌌🌌🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🚽🌌🎐🖱🖱🖱🖱    
🖱🌌🌌🌌🌌🌌🌌🌌🌌🍶🍶🍶🍶🍽🖱🖱🖱🖱🖱🖱🖱🖱💬🍶🌌🎐🖱🖱🖱🖱    
🖱🌌🌌🌌🌌🌌🌌🌌🌌🔢🔢🆓🔠🔨🍶🏳⛏⛏⛏⛏⛏🍶🍶📖🌌🎐🖱🖱🖱🖱    
🖱🌌🌌🌌🌌🌌🌌🌌🌌🚈🚈🆕🌑🌌📖🍶🍶🍶🍶🍶🍶🍶🗜🌌⤴🖱🖱🖱🖱🖱   
🖱🌌⚫⚫⚫⚫⚫⚫🖲🖱🖱🖱🖱🔢🌌🌑🌑🌑🌑🌑🌑🌑🌌🚆🖱🖱🖱🖱🖱🖱   
🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱📐📨📨📨📨📨📨📨🛫🖱🖱🖱🖱🖱🖱🖱   
🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱   

## Twitter 
🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🌨🐳🎽🛃🛅🎽💦🖱🖱🖱🖱💧🖱    
🖱💧🐬🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱💧🛄🛃🛃🛃🛃🛃🛃🎽💧🐳🛄💎🖱   
🖱🐳🛃💦🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🌨♿🛃🛃🛃🛃🛃🛃🛃🛃🛃🛃🐳🖱🌨   
🖱🎽🛃🛃🌀🖱🖱🖱🖱🖱🖱🖱🖱🖱🐳🛃🛃🛃🛃🛃🛃🛃🛃🛃🛃🎽🐳🎽💧   
🖱🎽🛃🛃🛃🎽🌧🖱🖱🖱🖱🖱🖱🖱🛄🛃🛃🛃🛃🛃🛃🛃🛃🛃🛃🛃🛅💧🖱    
🖱🐳🛃🛃🛃🛃🛅🐳🌨🖱🖱🖱🖱🖱🛃🛃🛃🛃🛃🛃🛃🛃🛃🛃🛃🛄🌧🖱🖱    
🖱💧🛃🛃🛃🛃🛃🛃🛃🎽🐬🌧🖱🖱🛃🛃🛃🛃🛃🛃🛃🛃🛃🛃🛃🎽🖱🖱🖱    
🖱🖱🎽🛃🛃🛃🛃🛃🛃🛃🛃🛃🛅🎽🛃🛃🛃🛃🛃🛃🛃🛃🛃🛃🛃🐳🖱🖱🖱    
🖱🐳💦🎽🛃🛃🛃🛃🛃🛃🛃🛃🛃🛃🛃🛃🛃🛃🛃🛃🛃🛃🛃🛃🛃🐳🖱🖱🖱    
🖱🎽🛃🛃🛃🛃🛃🛃🛃🛃🛃🛃🛃🛃🛃🛃🛃🛃🛃🛃🛃🛃🛃🛃🛃🐬🖱🖱🖱    
🖱🐬🛃🛃🛃🛃🛃🛃🛃🛃🛃🛃🛃🛃🛃🛃🛃🛃🛃🛃🛃🛃🛃🛃🛃🌧🖱🖱🖱     
🖱🖱🎽🛃🛃🛃🛃🛃🛃🛃🛃🛃🛃🛃🛃🛃🛃🛃🛃🛃🛃🛃🛃🛃🛄🖱🖱🖱🖱     
🖱🖱🌧🎽🛃🛃🛃🛃🛃🛃🛃🛃🛃🛃🛃🛃🛃🛃🛃🛃🛃🛃🛃🛃🐳🖱🖱🖱🖱    
🖱🖱🖱🖱🐳🛄🛃🛃🛃🛃🛃🛃🛃🛃🛃🛃🛃🛃🛃🛃🛃🛃🛃🛃🌧🖱🖱🖱🖱    
🖱🖱🖱🐳🎽🛅🛃🛃🛃🛃🛃🛃🛃🛃🛃🛃🛃🛃🛃🛃🛃🛃🛃🎽🖱🖱🖱🖱🖱   
🖱🖱🖱🌧🅿🛃🛃🛃🛃🛃🛃🛃🛃🛃🛃🛃🛃🛃🛃🛃🛃🛃🛅🌧🖱🖱🖱🖱🖱    
🖱🖱🖱🖱💦🛃🛃🛃🛃🛃🛃🛃🛃🛃🛃🛃🛃🛃🛃🛃🛃🛃🐬🖱🖱🖱🖱🖱🖱    
🖱🖱🖱🖱🖱📏🎽🛃🛃🛃🛃🛃🛃🛃🛃🛃🛃🛃🛃🛃🛃🐳🖱🖱🖱🖱🖱🖱🖱    
🖱🖱🖱🖱🖱🖱🖱🌧🎽🛃🛃🛃🛃🛃🛃🛃🛃🛃🛃🛃🎽🖱🖱🖱🖱🖱🖱🖱🖱    
🖱🖱🖱🖱🖱🌨🐳🛅🛃🛃🛃🛃🛃🛃🛃🛃🛃🛃🛃🐳🖱🖱🖱🖱🖱🖱🖱🖱🖱    
💧💎🐬🐳🎽🛃🛃🛃🛃🛃🛃🛃🛃🛃🛃🛃🛃🛅🐬🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱    
🖱🌀🛄🛃🛃🛃🛃🛃🛃🛃🛃🛃🛃🛃🛃🛅🐳🌨🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱    
🖱🖱🖱💎🐳🎽🛃🛃🛃🛃🛃🛃🛄🎽🐬🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱   

## Snapchat 
⬛⚫📳📳📳📳📳📳📳📳📳📳📳📳📳📳📳📳📳📳📳📳📳📳📳📳🌰⬛⬛   
⚫📳📳📳📳📳📳📳📳📳📳📳📳📳📳📳📳📳📳📳📳📳📳📳📳📳📳📳⬛   
📳📳📳📳📳📳📳📳📳📳📳📳📳📳📳📳📳📳📳📳📳📳📳📳📳📳📳📳👪    
📳📳📳📳📳📳📳📳📳📳📳📳📳🌕🌕📳📳📳📳📳📳📳📳📳📳📳📳📳📳    
📳📳📳📳📳📳📳📳📳📳🌕👃🖱🖱🖱🖱✨🌕📳📳📳📳📳📳📳📳📳📳📳    
📳📳📳📳📳📳📳📳📳🌕🖱🖱🖱🖱🖱🖱🖱🖱👃📳📳📳📳📳📳📳📳📳📳    
📳📳📳📳📳📳📳📳📳💡🖱🖱🖱🖱🖱🖱🖱🖱🖱🌝📳📳📳📳📳📳📳📳📳    
📳📳📳📳📳📳📳📳🌝🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱📳📳📳📳📳📳📳📳📳    
📳📳📳📳📳📳📳📳🌙🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🌕📳📳📳📳📳📳📳📳    
📳📳📳📳📳📳📳📳✨🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🌕📳📳📳📳📳📳📳📳    
📳📳📳📳📳📳📳📳⚡🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🌕📳📳📳📳📳📳📳📳    
📳📳📳📳📳📳📳📳🌙🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🌕📳📳📳📳📳📳📳📳    
📳📳📳📳📳🌕🌟🌝✨🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱👂👃👃📳📳📳📳📳📳    
📳📳📳📳📳🌕✨🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱👃📳📳📳📳📳📳    
📳📳📳📳📳📳📳🌕🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🌟🌕📳📳📳📳📳📳📳   
📳📳📳📳📳📳📳📳🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱😶📳📳📳📳📳📳📳📳    
📳📳📳📳📳📳📳🌕🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱✨📳📳📳📳📳📳📳📳    
📳📳📳📳📳📳🌕🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖐📳📳📳📳📳📳📳    
📳📳📳📳📳🌕✨🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖐📳📳📳📳📳📳    
📳📳📳🌕👃🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱✨🌝📳📳📳📳    
📳📳📳🌝🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱💫📳📳📳📳    
📳📳📳📳📳🌕✨🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🖱🌝🌕📳📳📳📳📳    
📳📳📳📳📳📳🌝🌟👂🌟🖱🖱🖱🖱🖱🖱🖱🖱✨👃👃🌟📳📳📳📳📳📳📳   
📳📳📳📳📳📳📳📳📳📳🌕🌙🖱🖱🖱🖱🖱🌝📳📳📳📳📳📳📳📳📳📳📳   
📳📳📳📳📳📳📳📳📳📳📳📳🌕👂👂🌝📳📳📳📳📳📳📳📳📳📳📳📳📳   
📳📳📳📳📳📳📳📳📳📳📳📳📳📳📳📳📳📳📳📳📳📳📳📳📳📳📳📳📳   
🌰📳📳📳📳📳📳📳📳📳📳📳📳📳📳📳📳📳📳📳📳📳📳📳📳📳📳📳⬛   
⬛📳📳📳📳📳📳📳📳📳📳📳📳📳📳📳📳📳📳📳📳📳📳📳📳📳📳⚫⬛   
