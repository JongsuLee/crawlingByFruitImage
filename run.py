import streamlit as st
import streamlit.components.v1 as components
import crawlingByFruitName_kurly as kurly
import crawlingByFruitName_gmarket as gmarket
import fruitClassifier as classifier
import showCrawled as show
from PIL import Image
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

item = st.text_input('과일을 입력해주세요: ', placeholder='ex) 사과, 바나나')
imgFile = st.file_uploader('과일🍅사진을 올려주세요', type=['jpeg', 'png', 'jpg'])

if item:
    kurly_dict = kurly.crawl(item)
    gmarket_dict = gmarket.crawl(item)
    item = None
    show.showCrawled(kurly_dict, gmarket_dict)

if imgFile:
    img = Image.open(imgFile).resize((224, 224))
    saved_img_path = './uploaded/' + imgFile.name
    
    with open(saved_img_path, 'wb') as f:
        f.write(imgFile.getbuffer())
        f.close()
    st.image(img)

    item = classifier.classify(saved_img_path)
    kurly_dict = kurly.crawl(item)
    gmarket_dict = gmarket.crawl(item)
    item = None
    show.showCrawled(kurly_dict, gmarket_dict)


