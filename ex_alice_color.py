import os
import matplotlib.pyplot as plt
import numpy as np
import random
from PIL import Image
from wordcloud import STOPWORDS, WordCloud, ImageColorGenerator

def grey_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    return "hsl(0, 0%%, %d%%)" % random.randint(60, 100)

curr_dir_path = os.path.dirname(os.path.abspath(__file__))
file_path = curr_dir_path + '/userlib_txt/alice.txt'
text = open(file_path).read()

file_path = curr_dir_path + '/userlib_pic/alice_color_mask.png'
alice_mask = np.array(Image.open(file_path))

stopwords = set(STOPWORDS)
stopwords.add("said")

wc = WordCloud(background_color="white", max_words=2000, mask=alice_mask, stopwords=stopwords, max_font_size=40, random_state=42)
wc = wc.generate(text)
image_colors = ImageColorGenerator(alice_mask)

# plt.figure(figsize=(6,6))
# plt.imshow(wc, interpolation='bilinear')
# plt.axis("off")
# plt.show()

# plt.figure(figsize=(6,6))
# plt.imshow(alice_mask, cmap=plt.cm.gray, interpolation='bilinear')
# plt.axis("off")
# plt.show()

plt.figure(figsize=(6,6))
plt.imshow(wc.recolor(color_func=image_colors), interpolation='bilinear')
plt.axis("off")
plt.show()