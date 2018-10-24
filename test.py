from PIL import Image
from pytesseract import image_to_string as iToStr
from pytesseract import image_to_boxes as iToBx

class word:
    chars = ''
    pos = [0, 0]

pdfFile = 0
jpegFile = 'test.jpeg'

string = iToStr(Image.open(jpegFile))
# REAL CODE

# Create a list for all word objects read from string
words = []
i = 0 #iterator for words
nWord = False
words.append(word())

for char in string:
#    print(i)
    if ord(char) == 10 or char == ' ':
#        print('new line')
        if nWord == False:
            nWord = True
            i += 1
    else:
        if nWord == True:
#            print('New word created')
            words.append(word())
        words[i].chars += char
        nWord = False

for j in words:
    print(j.chars)
