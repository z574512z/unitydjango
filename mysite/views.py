from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return render(request,"index.html",locals())

# def page(request,pno):
#     	authors=['王曉明','111','222','333']
# 		if pno>=0 and pno<len(authors):
# 		author=authors[pno]
# 		else:
# 		author="未知成員"
# 		return HttpResponse("成員簡介:{}".format(author))

# Create your views here.
