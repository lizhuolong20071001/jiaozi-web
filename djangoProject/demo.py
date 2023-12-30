from django.shortcuts import HttpResponse, render


def index(request):
    return render(request,'index.html')


def version_api(request):
    global now_version
    if request.method == 'GET':
        now_version = request.GET.get('now_version')
    now_version = str(now_version)
    if now_version == "12.0.1Public-A":
        # 如果对比结果符合 返回为i -》int
        return HttpResponse(1)
    else:
        # 如果返回结果不符合 返回0 -》int
        return HttpResponse(0)

def download_api(request):
    if request.method == 'GET':
        download_name = request.GET.get('download_name')
        path = f'/home/jiaozi/PycharmProjects/djangoProject/templates/{download_name}'
        with open(path) as f:
            c = f.read()
        return HttpResponse(c)



