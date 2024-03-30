import os
import matplotlib.pyplot as plt
import numpy as np
import random
from PIL import Image
from wordcloud import STOPWORDS, WordCloud

def grey_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    return "hsl(0, 0%%, %d%%)" % random.randint(60, 100)

curr_dir_path = os.path.dirname(os.path.abspath(__file__))
file_path = curr_dir_path + '/userlib_txt/alice.txt'
print(file_path)
text = open(file_path).read()

file_path = curr_dir_path + '/userlib_pic/alice_mask.png'
alice_mask = np.array(Image.open(file_path))

stopwords = set(STOPWORDS)
stopwords.add("said")

# plt.figure(figsize=(4,4))
# plt.imshow(alice_mask, cmap=plt.cm.gray, interpolation='bilinear')
# plt.axis("off")
# plt.show()

wc = WordCloud(background_color="white", max_words=2000, mask=alice_mask, stopwords=stopwords)
wc = wc.generate(text)
# print(wc.words_)

# plt.figure(figsize=(4,4))
# plt.imshow(wc, interpolation='bilinear')
# plt.axis("off")
# plt.show()

plt.figure(figsize=(6,6))
plt.imshow(wc.recolor(color_func=grey_color_func, random_state=3), interpolation='bilinear')
plt.axis("off")
plt.show()