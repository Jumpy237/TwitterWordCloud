#!/usr/bin/env python
# -*- coding: utf-8 -*-


from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from pymongo import MongoClient
import re

collectionName = input("Enter collection name: ")

#connect mongodb
client = MongoClient()
db = client.myProject
#set collection
collection = db[collectionName]

text = ""
for tweet in collection.find():
    text += tweet["text"]
text = re.sub("(https\S*|RT)","",text)
#print(text)

wordcloud = WordCloud(font_path="angsana.ttc",
                      relative_scaling = 1.0,
                      min_font_size=1,
                      background_color="white",
                      width=800,
                      height=800,
                      scale=1,
                      #mask=mask,
                      font_step=1,
                      regexp=r"[\u0E00-\u0E7Fa-zA-Z']+",
                      collocations=False,
                      margin=4,
                      max_words=1000
                      ).generate(text)

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()


