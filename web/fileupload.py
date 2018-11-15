import datetime
import os
import time

from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods


@csrf_exempt
@require_http_methods(["POST"])
def uploadFiles(request):
    try:
        user = request.session.get('user')
        allFimeNames = ""
        # 获取所有上传文件
        files = request.FILES.getlist("file")
        for file in files:
            # 获取文件名 解析文件后缀 获取新文件名
            oldName = file.name
            filename = str(int(time.time() * 10)) + "." + oldName.split(".")[1]
            now = datetime.now()
            filePath = os.path.join("developmentTask", str(user.get("userId")) + "-" + now.strftime('%Y-%m-%d'))
            dirpath = os.path.join(settings.UPLOADFILES_DIRS, filePath)
            # 写入服务器
            if not os.path.exists(dirpath):
                os.makedirs(dirpath)
            newFilePath = os.path.join(dirpath, filename)
            with open(newFilePath, 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
            # 返回新文件名 多个用逗号隔开
            allFimeNames = os.path.join(filePath, filename)
    except Exception:
        return JsonResponse(data={'error': "系统异常"}, status=400)
    return JsonResponse(data={'filePath': allFimeNames})
