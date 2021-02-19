from django.db import models

import datetime
import time
from StoreScript.Configuration.Base.cnfclass import DBcnf, Order
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class AddOrder(models.Model):
	print(f'AddOrder datetime.datetime.now() : {datetime.datetime.now()}')
	order_store_key = models.CharField(max_length=DBcnf.maxCharLen)
	order_title = models.CharField(max_length=DBcnf.maxCharLen) # 길이제한 있는 문자열 / textfield() 객체 다수 사용시 성능저하
	order_number = models.IntegerField(default=DBcnf.orderNumber)
	order_state_index = models.IntegerField(default=DBcnf.orderStateIndex)
	order_rcv_time = models.DateTimeField(auto_now_add=True) # 해당 레코드 생성시 현재시간 자동저장
	order_updated_time = models.DateTimeField(auto_now=True) # 해당 레코드 갱신시 현재시간 자동저장

	def __str__(self):
		return '매장키: {}\n' \
			   '주문명: {}\n' \
			   '주문개수: {}\n' \
			   '주문상태: {}\n' \
			   '주문시간: {}\n' \
			   '주문작업마지막로그: {}\n' \
			   ''.format(self.order_store_key,
						 self.order_title,
						 self.order_number,
						 self.order_state_index,
						 self.order_rcv_time,
						 self.order_updated_time
						 )

	def recent_orders(self):
		return self.order_updated_time >= timezone.now() - datetime.timedelta(days=1)

	class Meta:
		#app_label = BASE_DIR / 'db.sqlite3'
		app_label = 'storeapp'


class RobotState(models.Model):
	print(f'RobotState datetime.datetime.now() : {datetime.datetime.now()}')
	robot_key = models.CharField(max_length=DBcnf.maxCharLen)
	robot_state_index = models.IntegerField(default=DBcnf.robotStateIndex)
	robot_updated_time = models.DateTimeField(auto_now=True)

	def __str__(self):
		return '로봇키: {}\n' \
			   '로봇상태: {}\n' \
			   '로봇작업마지막로그: {}\n' \
			   ''.format(self.robot_key,
						 self.robot_state_index,
						 self.robot_updated_time
						 )

	class Meta:
		#app_label = BASE_DIR / 'db.sqlite3'
		app_label = 'storeapp'





	# class Meta:
	# 	app_label = 'collectapp'