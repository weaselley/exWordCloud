import os
import matplotlib.pyplot as plt
from wordcloud import WordCloud

curr_dir_path = os.path.dirname(os.path.abspath(__file__))
file_path = curr_dir_path + '/userlib_txt/constitution.txt'

text = open(file_path).read()
# wordcloud = WordCloud().generate(text)
wordcloud = WordCloud(max_font_size=40).generate(text)
# print(wordcloud.words_)

plt.figure(figsize=(6, 6))
plt.imshow(wordcloud, interpolation = 'bilinear')
plt.axis("off")
plt.show()