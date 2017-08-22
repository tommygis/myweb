# from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from blog import models
import json
import importlib, sys
importlib.reload(sys)

# Create your views here.
# indexl  &
def index(request):
    return HttpResponseRedirect("http://127.0.0.1:8000/start/")

# 查询数据库中的数据，并构造成json
# @csrf_exempt
def Read_all_SQL(request):
    # 查询数据
    obj_all = models.News.objects.all()
    eaList = []
    for li in obj_all:
        eaList.append({
                     "news_title": li.title,
                     "news_date": li.date,
                     "news_detail_time": li.detail_time,
                     "news_content": li.content,
                     "news_url": li.url,
                     "news_source": li.source,
                     "news_web": li.web,
                     "news_logtime": li.logtime,
                     "news_id": li.id})

    # 将int类型使用dumps()方法转为str类型
    eaList_len = json.dumps(len(eaList))
    # 构造一个字典
    json_data_list = {'rows': eaList, 'total': eaList_len}
    # dumps()将字典转变为json形式,
    easyList = json.dumps(json_data_list)
    # 将json返回去，json的键值对中的键需要与前台的表格field=“X”中的X名称保持一致）
    return HttpResponse(easyList)

# 编辑数据并post方法提交到数据库
def Edit_NewsName(request, id):
    print("这是编辑的："+id)
    print(request.method)
    # 从前端获取到输入的数据
    # POST.get('xxx')这个中的字段是前端表格的<th field="news_title" width="50">新闻标题</th>中的field一致
    if request.method == 'POST':
        title = request.POST.get('news_title')
        date = request.POST.get('news_date')
        detail_time = request.POST.get('news_detail_time')
        content = request.POST.get('news_content')
        url = request.POST.get('news_url')
        source = request.POST.get('news_source')
        web = request.POST.get('news_web')
        logtime = request.POST.get('news_logtime')
        # 构造字典并转成json，这里的键需要与数据库的字段一致
        dic = {
                "title": title,
                "date": date,
                "detail_time": detail_time,
                "content": content,
                "url": url,
                "source": source,
                "web": web,
                "logtime": logtime,
               };
        print(dic)
        models.News.objects.filter(id=id).update(**dic)
        return HttpResponse("Edit_OK")

# 增加数据
# add News_Name  + start_app
# @csrf_exempt
def app_start(request):
    # add_save_News
    if request.method == "POST":
        print("POST")
        print(request.POST)
        title = request.POST.get('news_title')
        date = request.POST.get('news_date')
        detail_time = request.POST.get('news_detail_time')
        content = request.POST.get('news_content')
        url = request.POST.get('news_url')
        source = request.POST.get('news_source')
        web = request.POST.get('news_web')
        logtime = request.POST.get('news_logtime')
        # 构造字典并转成json，这里的键需要与数据库的字段一致
        dic = {
                "title": title,
                "date": date,
                "detail_time": detail_time,
                "content": content,
                "url": url,
                "source": source,
                "web": web,
                "logtime": logtime,
               };
        models.News.objects.create(**dic)
        return HttpResponse("save")
    else:
        print(" is null_!")
    return render(request, 'info.html')

# 移除数据
# @csrf_exempt
def Remove_News_ID(request):
    if request.method == "POST":
        print("REMOVE POST")
        id = request.POST.get('id')
        print(id)
        models.News.objects.filter(id=id).delete()
    return HttpResponse("REMOVE")


