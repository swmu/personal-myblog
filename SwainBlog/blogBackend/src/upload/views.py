# coding=utf-8
import os
import json
from django.http import HttpResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def imageUpload(request):
    if request.method == "POST":  # 请求方法为POST时，进行处理
        myFile = request.FILES.get("img", None)  # 获取上传的文件，如果没有文件，则默认为None
        type = request.POST.get('type')
        if not myFile:
            return HttpResponse("no files for upload!")

        filePath = os.path.join(settings.BASE_DIR, 'uploads')
        filePath = os.path.join(filePath, type)
        if not os.path.exists(filePath):
            os.mkdir(filePath)
        filePath = os.path.join(filePath, myFile.name)
        destination = open(filePath, 'wb+')  # 打开特定的文件进行二进制的写操作
        for chunk in myFile.chunks():  # 分块写入文件
            destination.write(chunk)
        destination.close()
        imgPath = os.path.join('media',type)
        imgPath = os.path.join(imgPath,myFile.name)
        return HttpResponse(json.dumps({"imgPath":imgPath}),{"contentType":"application/json"})