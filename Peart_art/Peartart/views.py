from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views.generic import TemplateView

from Peartart.models import *


class DailyReportView(TemplateView):
    template_name = "daily_report.html"

    def get(self, request, *args, **kwargs):
        context = super(DailyReportView, self).get_context_data(**kwargs)

        reports = DailyReport.objects.order_by('report_date')
        context['reports'] = reports

        return render(self.request, self.template_name, context)