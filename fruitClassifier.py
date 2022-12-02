from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.models import load_model
import numpy as np


model1 = load_model("FV_224.h5", compile=True)
labels = {0: '가지', 1: '감', 2: '구아바', 3: '귤', 4: '대추', 5: '딸기', 6: '땅콩', 7: '라임', 
           8: '람부탄', 9: '레몬', 10: '리치', 11: '마카다미아', 12: '망고', 13: '망고 스틴', 14: '멜론', 
           15: '모과', 16: '무화과', 17: '바나나', 18: '배', 19: '블랙베리', 20: '블루베리', 21: '사과', 
           22: '산딸기', 23: '살구', 24: '석류', 25: '수박', 26: '아보카도', 27: '아사이베리', 28: '오렌지', 
           29: '올리브', 30: '유자', 31: '자몽', 32: '체리', 33: '키위', 34: '토마토', 35: '파인애플', 
           36: '패션후르트', 37: '포도', 38: '피망', 39: '할라피뇨', 40: '호박'}

def classify(img):
    fruitImage = load_img(img, target_size=(224, 224, 3))
    fruitImage = img_to_array(fruitImage)
    fruitImage = fruitImage / 255
    fruitImage = np.expand_dims(fruitImage, [0])
    answer = model1.predict(fruitImage)
    y_class = answer.argmax(axis=-1)   # 인덱스에서 제일 높은 것 찾기?
    y = " ".join(str(x) for x in y_class)
    y = int(y)
    res = labels[y]
    
    return res
