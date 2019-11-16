'''
Created on 2019. 11. 4.

@author: USER
'''

def best_color (analysis_result1):
    
    if analysis_result1 == 'spring':
        result_name = '봄 웜'
        result = "/static/images/result/spring_warm.PNG"
        result_KS = "/static/images/result/spring_KS.PNG"
        result_t_color = "https://www.w3schools.com/lib/w3-theme-red.css"
        result_text = '''
        <div class="w3-small">
                  봄 색상의 감성축<br>
        <img src="/static/images/result/spring_g1.PNG" style="max-width :200px">
        </div>
        <br>
        <div class="w3-small" style="text-align:left; line-height: 2;"> 
        <li> 따뜻한 색감을 가지고 있는 그룹</li>
        <li>비비드한 톤과 파스텔 톤으로 이루어져 있어 화사하면서 활기찬 느낌</li>
        <li>복숭아빛의 밝고 노란빛의 투명한 피부를 가짐</li>
        <li>눈동자는 반짝반짝거리고 생기가 있는 밝은 갈색빛을 띔</li>
        </div>
        '''
        result_person = "/static/images/result/spring_person.PNG"

    elif analysis_result1 == 'summer':
        result_name = '여름 쿨'
        result = "/static/images/result/summer_cool.PNG"
        result_KS = "/static/images/result/summer_KS.PNG"
        result_t_color = "https://www.w3schools.com/lib/w3-theme-cyan.css"
        result_text = '''
        <div class="w3-small">
                  여름 색상의 감성축<br>
        <img src="/static/images/result/summer_g1.PNG" style="max-width :200px">
        </div>
        <br>
        <div class="w3-small" style="text-align:left; line-height: 2;"> 
                    <li>소프트하고 밝은 컬러, 그레이시한 컬러들로 이루어져 있어 시원하고 화려한 인상</li>
                    <li>핑크빛이 도는 혈색이 좋은 피부 톤</li>
                    <li>차분하고 부드러운 갈색 눈동자와 회갈색을 띠는 머리카락</li>
                    <li>지적이고 세련되며 우아한 인상 </li>
        </div>
        '''
        result_person = "/static/images/result/summer_person.PNG"
    
    elif analysis_result1 == 'winter':
        result_name = '겨울 쿨'
        result = "/static/images/result/winter_cool.PNG"
        result_KS = "/static/images/result/winter_KS.PNG"   
        result_t_color = "https://www.w3schools.com/lib/w3-theme-deep-purple.css"
        result_text = '''
        <div class="w3-small">
                  겨울 색상의 감성축<br>
        <img src="/static/images/result/winter_g1.PNG" style="max-width :200px">
        </div>
        <br>
        <div class="w3-small" style="text-align:left; line-height: 2;"> 
        <li>파란색, 흰색, 검정을 내포하고 있는 차갑고 강렬한 컬러 그룹</li>
        <li>선명하고 강하거나, 아주 여린 아이시한 컬러들이 속함</li>
        <li>모던하고 도회적인 이미지</li>
        <li>창백한 피부와 투명한 피부를 가지고 있거나 아주 검거나 노란 피부를 가진, 경계가 확실한 피부톤</li>
        <li>눈동자는 강렬하며 개성과 카리스마가 있음</li>
        <li>푸른빛이 도는 갈색머리, 흑색 머리를 가지고 있는 것이 특징</li>
        </div>
        '''
        result_person = "/static/images/result/winter_person.PNG"
       
    else :
        result_name = '가을 웜'
        result = "/static/images/result/autumn_warm.PNG"
        result_KS = "/static/images/result/autumn_KS.PNG"
        result_t_color = "https://www.w3schools.com/lib/w3-theme-amber.css"
        result_text = '''
        <div class="w3-small">
                  가을 색상의 감성축<br>
        <img src="/static/images/result/autumn_g1.PNG" style="max-width :200px">
        </div>
        <br>
        <div class="w3-small" style="text-align:left; line-height: 2;"> 
        <li>짙은 황색을 많이 포함하는 색 그룹으로 깊고 강하면서 고급스럽고 편안한 컬러</li>
        <li>어른스럽고 차분한 이미지</li>
        <li>누르스름한 피부톤에 혈색이 있음</li>
        <li>눈동자 색은 짙고 깊이감이 있어 차분하고 혹은 짙은 갈색빛을 지님</li> 
        </div>
        '''
        result_person = "/static/images/result/autumn_person.PNG"     
               
    return result_name, result, result_KS, result_t_color, result_text, result_person


    
def main():
    pass

if __name__ == "__main__":
    main()