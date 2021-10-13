from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy

from .forms import SetThresholdForm
from .models import SetThreshold

from django.contrib.auth.decorators import login_required

class ThresholdView(CreateView):
    model = SetThreshold				# 연결할 클래스 or table명
    context_object_name = 'threshold'   # context 변수명 지정
    form_class = SetThresholdForm       # 우리가 만든 폼 클래스를 form_class에 할당!
    success_url = reverse_lazy('uploader:uploader')                # 성공시 연결할 페이지
    template_name = 'threshold/threshold.html'

# @login_required
# def setThreshold(request):
#     if request.method == 'POST':
#         threshold = request.POST['threshold']
#         set_date = request.POST['set_date']
#
#         setThreshold = SetThreshold(
#             threshold = threshold,
#             set_date = set_date,
#         )
#         setThreshold.save()
#         return redirect('threshold:threshold')
#     else:
#         setThresholdForm = SetThresholdForm
#         context = {
#             'setThresholdForm': setThresholdForm,
#         }
#         return render(request, 'threshold/threshold.html', context)