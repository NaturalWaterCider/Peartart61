from django.db import models

# Create your models here.

class DailyReport(models.Model):

    # 日付
    report_date = models.DateField()

    # 出勤時間
    in_time = models.DateTimeField()

    # 退勤時間
    out_time = models.DateTimeField()

    # とど
    do_list = models.CharField(max_length=512)

    # やったこと
    did_list = models.CharField(max_length=512)

    # 学んだこと
    learnings = models.CharField(max_length=1024, null=True, blank=True)

    # 自由
    free_writing = models.CharField(max_length=1024, null=True, blank=True)

