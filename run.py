import streamlit as st
import streamlit.components.v1 as components
import crawlingByFruitName_kurly as kurly
import crawlingByFruitName_gmarket as gmarket
import showCrawled as show
import time

item = st.text_input('과일을 입력해주세요: ', placeholder='ex) 사과, 바나나')

if item:
    kurly_dict = kurly.crawl(item)
    gmarket_dict = gmarket.crawl(item)
    item = None
    # print(f'kurly: {kurly_dict}')
    # print(f'gmarket: {gmarket_dict}')
    show.showCrawled(kurly_dict, gmarket_dict)


