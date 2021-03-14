# gifs

## why
I wanted to understand rendering images, and then gifs on m5 hardware

## how
Identify the gif
```
$ identify spongebob.gif 
spongebob.gif[0] GIF 400x287 400x287+0+0 8-bit sRGB 256c 0.000u 0:00.000
...
spongebob.gif[18] GIF 400x287 400x287+0+0 8-bit sRGB 256c 795974B 0.010u 0:00.009
```
The unit I'm using has an 80x160 display, resize using imagemagik, a couple of useful stackoverflow posts
- https://askubuntu.com/a/101527
- https://askubuntu.com/a/257848

```
gifsicle --resize-height 80 spongebob-large.gif -o spongebob-small.gif
```
Verify
```
$ identify spongebob-small.gif 
spongebob-small.gif[0] GIF 111x80 111x80+0+0 8-bit sRGB 256c 0.010u 0:00.000
...
spongebob-small.gif[18] GIF 111x80 111x80+0+0 8-bit sRGB 256c 55442B 0.000u 0:00.010
```
Make a venv
```
$ python3 -m venv venv
$ source env/bin/activate
$ pip3 install pillow
```
Underestimate the amount of time you need to figure out bitmaks
## Image format
M5 needs images in the R5G6B5 format, 16 bits in total, 2 adjacent bytes.
Pillow can be told to return an RGB tuple, this needs to be shifted and built into 2 bytes, the `hex_from_pixel` function in `img2c.py` takes care of this.
This script is now updated to support gif and jpg formats, returning an array of frames (length 1 in the case of jpg)

## Continue..
Generate both the c and h files for the image, include in gif.ino.