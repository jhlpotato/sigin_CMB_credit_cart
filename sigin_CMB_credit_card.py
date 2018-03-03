#!/usr/bin/env python
# -*- coding: utf-8 -*-
import itchat
from apscheduler.schedulers.blocking import BlockingScheduler

itchat.auto_login(enableCmdQR=2, hotReload=True)

def job():
	mps = itchat.search_mps(name=u'招商银行信用卡')[0]
	mps.send(u'签到')

def job_heartbeat():
	mps = itchat.search_mps(name=u'招商银行信用卡')[0]
	print '1'

sched = BlockingScheduler()
sched.add_job(job, 'interval', hours=24)
sched.add_job(job_heartbeat, 'interval', minutes=1)
sched.start()
