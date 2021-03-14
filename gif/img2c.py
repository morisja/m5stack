from PIL import Image
import collections
import click
cimg=collections.namedtuple("cimg", "height width frames")



def generate_hfile(name, varname):
    with open("{}.h".format(name),"w") as out:
        print("extern const uint8_t *{}[];".format(varname), file=out)

def generate_cfile(dat, name, varname):
    total_pixels=dat.height * dat.width
    frame_names=[]

    with open("{}.c".format(name),"w") as out:
        print("#include <stdint.h>", file=out)
        print("#include \"{}.h\"".format(name), file=out)

        for num,frame in enumerate(dat.frames):
            print("static const uint8_t {}_f{}[{}] = {{ {} }};".format(name,num,total_pixels*2, ",".join(frame)), file=out)
            frame_names.append("{}_f{}".format(name,num))
        print("const uint8_t *{}[] = {{ {} }};".format(varname,",".join(frame_names)), file=out)


def hex_from_pixel(pixel):
    r=pixel[0]
    g=pixel[1]
    b=pixel[2]
 
    # We start with 3, 8 bit values
    # the format is R5 G6 B5, giving us 16 bit as follows:
    # RRRRRGGG GGGBBBBB

    # Extract the first 5 bits of red
    r=r&0xf8
    # Save two copies of green as these split across two final bytes
    g1=g
    g2=g
    #Shift the first green 5bits right, to leave us with 00000GGG
    g1=g1 >>5
    #Mask the other green to get the other bits
    g2=g2 & 0xe0
    # Shift Blue to get 000BBBBB
    b=b>>3
    # Empty the first bits to make space for green
    b=b&0x1f

    # Or things together
    # r : RRRRR000
    # g1: 00000GGG
    # g2: GGG00000
    # b : 000BBBBB
    byte1=r|g1
    byte2=g2|b
    return [hex(byte1), hex(byte2)]

def frame_to_hex(im):
    all_pixels=[]
    pixels=im.load()
    width, height = im.size
    total_pixels=width*height
    for y in range(height):
        row=[]
        for x in range(width):
            cpixel = pixels[x, y]
            all_pixels.extend(hex_from_pixel(cpixel))
    return all_pixels

def gif_to_c(fname):
    frames=[]
    with Image.open(fname) as im:
        width, height = im.size
        try:
            while 1:
                frames.append(frame_to_hex(im.convert("RGB")))
                im.seek(im.tell()+1)
        except EOFError:
            pass # end of sequence

    return cimg(height, width, frames)

def img_to_c(fname):
    frames=[]
    with Image.open(fname) as im:
        width, height = im.size
        pixels=frame_to_hex(im.convert("RGB"))
        frames.append(pixels)
        return cimg(height, width, frames)



@click.command()
@click.option('--infile', help='input file', required=True)
@click.option('--outfile', help='input file', default="img")
@click.option('--outvarname', help='output var naming', required=True)
def convert(infile, outfile, outvarname):
    if "gif" in infile:
        dat = gif_to_c(infile)
    else:
        dat = img_to_c(infile)

    generate_hfile(outfile, outvarname)
    generate_cfile(dat, outfile, outvarname)



if __name__ == '__main__':
    convert()


