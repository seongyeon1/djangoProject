from django.views.generic import ListView, DetailView
from .models import *
from django.contrib import messages
from django.db.models import Q

class SanctionListView(ListView):
    model = SanctionMain
    paginate_by = 8
    template_name = 'sanction/sanction_list.html'  #DEFAULT : <app_label>/<model_name>_list.html
    context_object_name = 'sanction_list'        #DEFAULT : <model_name>_list

    def get_queryset(self):
        search_keyword = self.request.GET.get('q', '')
        sanction_list = SanctionMain.objects.order_by('ent_num')

        if search_keyword:
            if len(search_keyword) > 1:
                search_sanction_list = sanction_list.filter(
                    Q(sdn_name__icontains=search_keyword)
                )
                return search_sanction_list
            else:
                messages.error(self.request, '검색어는 2글자 이상 입력해주세요.')
        return sanction_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = context['paginator']
        page_numbers_range = 5
        max_index = len(paginator.page_range)

        page = self.request.GET.get('page')
        current_page = int(page) if page else 1

        start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range
        end_index = start_index + page_numbers_range
        if end_index >= max_index:
            end_index = max_index

        page_range = paginator.page_range[start_index:end_index]
        context['page_range'] = page_range

        search_keyword = self.request.GET.get('q', '')

        if len(search_keyword) > 1:
            context['q'] = search_keyword

        return context