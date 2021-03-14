from PIL import Image
import collections

def hex_from_pixel(pixel):
    r=pixel[0]
    g=pixel[1]
    b=pixel[2]
 
    r=r&0xf8
    g1=g
    g2=g
    g1=g1 >>5
    g2=g2 & 0xe0
    b=b>>3
    b=b&0x1f

    byte1=r|g1
    byte2=g2|b
    return [hex(byte1), hex(byte2)]

def dump_pixels(im):
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

cgif=collections.namedtuple("cgif", "height width frames")

def gif_to_c(fname):
    frames=[]
    with Image.open(fname) as im:
        width, height = im.size
        try:
            while 1:
                pixels=dump_pixels(im.convert("RGB"))
                frames.append(pixels)
                #frames.append("static const uint8_t image_1_f{}[{}] = {{ {} }};".format(frame,total_pixels*2, ",".join(pixels)))
                #frame_names.append("image_1_f{}".format(frame))
                im.seek(im.tell()+1)
                #frame=frame+1
        except EOFError:
            pass # end of sequence
    
    return cgif(height, width, frames)

image_data=gif_to_c("spongebob-small.gif")

generate_hfile("img", "spongebob")
generate_cfile(image_data, "img", "spongebob")
