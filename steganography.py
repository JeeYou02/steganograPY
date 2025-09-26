import cv2

def str_to_bin(msg):
    bin_msg = ""
    for c in msg:
        bin_msg = bin_msg + format(ord(c), '08b')
    
    return bin_msg

def bin_to_str(bin_msg):
    out_msg = ""
    for i in range(0, len(bin_msg), 8):
        bin_char = bin_msg[i:i+8]
        out_msg = out_msg + chr(int(bin_char, 2))

    return out_msg

def set_LSB(pxl_val, bit):
    if(pxl_val % 2 == bit):     #bit already set
        return pxl_val

    if(pxl_val % 2 == 0):       #setting bit to 1
        return pxl_val + 1

    if(pxl_val % 2 == 1):       #setting bit to 0
        return pxl_val - 1

def steganography_hide_msg(img, msg):
    bin_msg = str_to_bin(msg + "###")

    out_img = img.copy()

    assert len(bin_msg) <= img.shape[0]*img.shape[1]*img.shape[2], "The message is too long for the provided image..."

    for i in range(len(bin_msg)):
        row = i // (img.shape[1]*3)
        column = (i // 3) % img.shape[1]
        channel = i % 3

        out_img[row][column][channel] = set_LSB(img[row][column][channel], int(bin_msg[i]))

    return out_img

def steganography_reveal_msg(img):
    bin_msg = ""
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            for k in range(img.shape[2]):
                bin_msg = bin_msg + str(img[i][j][k] % 2)
    
    full_msg = bin_to_str(bin_msg)
    index = full_msg.find("###")

    if(index == -1):
        return -1

    return full_msg[0:index]
