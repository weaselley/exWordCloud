import os
import matplotlib.pyplot as plt
import numpy as np
import random
from PIL import Image
from wordcloud import STOPWORDS, WordCloud

def grey_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    return "hsl(0, 0%%, %d%%)" % random.randint(60, 100)

curr_dir_path = os.path.dirname(os.path.abspath(__file__))
file_path = curr_dir_path + '/userlib_txt/a_new_hope.txt'
text = open(file_path).read()

text = text.replace("HAN", "Han")
text = text.replace("LUKE'S", "Luke")

file_path = curr_dir_path + '/userlib_pic/vader_mask.png'
vader_mask = np.array(Image.open(file_path))

stopwords = set(STOPWORDS)
stopwords.add("int")
stopwords.add("ext")

wc = WordCloud(max_words=1000, mask=vader_mask, stopwords=stopwords, margin=10, random_state=1).generate(text)
default_colors = wc.to_array()

# plt.figure(figsize=(6,6))
# plt.title("Default colors")
# plt.imshow(default_colors, interpolation='bilinear')
# plt.axis("off")
# plt.show()

plt.figure(figsize=(6,6))
plt.title("Custom colors")
plt.imshow(wc.recolor(color_func=grey_color_func, random_state=3), interpolation='bilinear')
plt.axis("off")
plt.show()