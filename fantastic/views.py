from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')
    
# 이쪽에서 지금 redering을 해주고 있어요 home 이라는 곳으로 request (요청) 이들어오면
# home.html 을 사용자에게 보여주는거에요, 즉 home.html 이라는 이름만 보여주는거에요
# 그런데 지금 templates 폴더에 보시면 index.html밖에 없죠
# 지금 장고로 서버를 키면 오류가 날겁니다. 선아님이 돌리신 방법은 html만 띄워주어서 정상적으로 보였지만
# 사실 장고를 이용해서 띄운 것을 아닙니다.넵 그래서 지금 방법은 두가지가 있는데,
# 한가지는 home.html 을 index.html로 바꾸어주는 것이고 다른 방법은 index.html  을 home.html 로 변경해주는 거에요
# 그런데 이미 views 에서 함수이름이 home 이기 때문에 단순히 html 파일 이름을 변경시켜줄게요