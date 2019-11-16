'''
Created on 2019. 11. 4.

@author: USER
'''
import os
import cv2
import imutils # pip install imutils
from main_app import preprocess as pre # 모듈 : 사진 전처리
import pickle
          
def analysis (face_HSVCbCr):
    try :    
        data = face_HSVCbCr
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        
        #웜, 쿨 분류 모형 수행
        path = BASE_DIR + '/main_app/ml_model/Mytone.sav'
        model = pickle.load(open(path, 'rb'))
        pred = model.predict(data)
        
        #예측 후 계절 값 추출
        if pred =='warm':
            path = BASE_DIR + '/main_app/ml_model/Mytone_warm.sav'
            model_warm = pickle.load(open(path, 'rb'))
            pred = model_warm.predict(data)
        else :
            path = BASE_DIR + '/main_app/ml_model/Mytone_cool.sav'
            model_cool = pickle.load(open(path, 'rb'))
            pred = model_cool.predict(data)
            
        return pred # spring, summer, fall, winter
    
    except Exception :
        return 'e-analysis' 

# 전처리 (이미지 to HSVCbCr)
def pic_prepocess (uploaded_file_url):
    
    try :    
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
         
        img_path = BASE_DIR +'/' + uploaded_file_url
        img = cv2.imread(img_path)
    
        # 분석 코드 영역
        haarcascade_path = BASE_DIR +'//main_app//ml_model//haarcascade_frontface.xml'
        face_cascade = cv2.CascadeClassifier(haarcascade_path)
        # image_size = 250
        
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3,5)
        
        # crop
        for (x,y,w,h) in faces:
            cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,255), 5)        
            cropped = img[y+2:y + h-1, x+2:x + w-1]
                
        cv2.imwrite(os.path.join(os.path.join(BASE_DIR, 'media') , 'face_detect.jpg'), img)
        
        # 250의 너비로 이미지 크기 조정
        image = imutils.resize(cropped, width=250)
        # 크롭이미지 지정경로 저장
        cv2.imwrite(os.path.join(os.path.join(BASE_DIR, 'media') , 'crop.jpg'), image)
           
        # 피부만 적용
        skin = pre.extractSkin(image)
        
        # 색상정보 추출
        dominantColors = pre.extractDominantColor(skin, hasThresholding=True)
        
        # 컬러바 생성 (※※※)
        # color_bar = pre.plotColorBar(dominantColors)
        # 컬러바 지정경로 저장
        # cv2.imwrite(os.path.join(os.path.join(BASE_DIR, 'media') , 'color_bar.jpg'), color_bar)
        
        #가장 많은 색상 추출
        sam1 = dominantColors[0]
        
        #RGB각 추출
        R = float(sam1['color'][0])
        G = float(sam1['color'][1])
        B = float(sam1['color'][2])
        
        #RGB 에서 HSV로 변환
        hsv = pre.rgb2hsv(R,G,B)
        H = hsv[0]
        S = hsv[1]
        V = hsv[2]
        #RGB 에서 YCbCr로 변환
        ycc = pre.rgb2ycc(R,G,B)
        #Y = ycc[0]
        Cb = ycc[1]
        Cr = ycc[2]        
        
        # RGB=[]     
        # RGBHSV=[]
        
        # RGB.append([R,G,B])    
        # RGBHSV.append([R,G,B,H,S,V])
        
        # HSVCbCr
        HSVCbCr=[]
        HSVCbCr.append([H,S,V,Cb,Cr])
    
        return HSVCbCr

    except Exception :
        return 'e-preprocess'
    

def main ():
    pass

if __name__ == "__main__":
    main()