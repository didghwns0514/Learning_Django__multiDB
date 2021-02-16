from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import AddOrder
from datetime import datetime

def index(request):
	"""
	참조 >>>
	https://lqez.github.io/blog/django-queryset-basic.html
	https://velog.io/@devzunky/TIL-no.66-Django-Basic-19-%EB%8D%B0%EC%9D%B4%ED%84%B0-%EC%A1%B0%ED%9A%8C%ED%95%98%EA%B8%B0

	:param request:
	:return:
	"""

	#todaySales_list = AddOrder.objects.order_by('-pub_date')
	todaySales_list = AddOrder.objects.filter(order_rcv_time__day=datetime.today().day)

	tmp_sum = 0 if not todaySales_list \
		else sum([ ob.order_number for ob in todaySales_list ])

	return HttpResponse(tmp_sum)