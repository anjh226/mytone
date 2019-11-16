from django.shortcuts import render

from main_app import analysis as ana # 모듈 : 결과 분석
from main_app import result_contents as rcon # 모듈 : 결과 콘텐츠 매칭


def main_func(request):
    return render(request, 'home.html')

def upload_func(request):
    return render(request, 'pic_upload.html')

def result_func(request):
    return render(request, 'result.html')

def fail_func(request):
    return render(request, 'fail.html')

# 이미지 업로드
from django import forms
from django.core.files.storage import FileSystemStorage

class ImageUploadForm(forms.Form):
    image = forms.ImageField()

# 전처리, 분석
def process(request):
    if request.method == 'POST' :
        form = ImageUploadForm(request.POST, request.FILES)

        if form.is_valid():
            # 이미지 저장 및 경로확인
            imagefile = request.FILES['image']
            fs = FileSystemStorage()
            filename = fs.save(imagefile.name, imagefile)
            uploaded_file_url = fs.url(filename)
            
            # 전처리 (RGB list 리턴)
            face_HSVCbCr = ana.pic_prepocess(uploaded_file_url)
            print(face_HSVCbCr)
            if face_HSVCbCr =='e-preprocess':
                return render(request, "fail.html", {'uploaded_file_url':uploaded_file_url})
            
            # 분석
            analysis_result1 = ana.analysis(face_HSVCbCr)
            print(analysis_result1)
            
            if analysis_result1 =='e-analysis':
                return render(request, "fail.html", {'uploaded_file_url':uploaded_file_url})               
            
            # 분석 결과 매칭 결과차트 값 가져오기
            result_name, color_chart_path, result_KS, result_t_color, result_text, result_person = rcon.best_color(analysis_result1)

            return render(request, "result.html", {'uploaded_file_url':uploaded_file_url, 
                                                   'analysis_result1':analysis_result1, 
                                                   'result_name': result_name,
                                                   'color_chart_path':color_chart_path,
                                                   'result_t_color' :result_t_color,
                                                   'result_text' :result_text,
                                                   'result_person' :result_person,
                                                   'result_KS' :result_KS})
        
        else : 
            return render(request, 'fail.html')
    else :
        return render(request, 'fail.html')