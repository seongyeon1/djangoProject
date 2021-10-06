from django.shortcuts import render, get_object_or_404

from django.views.generic import ListView, DetailView
from .models import Page, File
from django.contrib import messages
from django.db.models import Q

class FileListView(ListView):
    model = File
    paginate_by = 8
    template_name = 'mysite/file_list.html'  #DEFAULT : <app_label>/<model_name>_list.html
    context_object_name = 'file_list'        #DEFAULT : <model_name>_list

    def get_queryset(self):
        search_keyword = self.request.GET.get('q', '')
        file_list = File.objects.order_by('-id')

        if search_keyword:
            if len(search_keyword) > 1:
                search_file_list = file_list.filter(
                    Q(file_name__icontains=search_keyword)
                )
                return search_file_list
            else:
                messages.error(self.request, '검색어는 2글자 이상 입력해주세요.')
        return file_list

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

class FilePageListView(DetailView):
    model = File
    paginate_by = 8
    template_name = 'mysite/page_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_list'] = Page.objects.all()

        print(context['page_list'])
        return context


# class FilePageListView(ListView):
#     model = Page
#     template_name = 'mysite/page_list.html'  #DEFAULT : <app_label>/<model_name>_list.html
#     context_object_name = 'page_list'        #DEFAULT : <model_name>_list
#
#     def get_queryset(self):
#         self.file = get_object_or_404(File, file_name=self.kwargs['file'])
#         return Page.objects.filter(file=self.file)
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['file'] = self.file
#         return context

class PageDetailView(DetailView):
    model = Page
    template_name = 'mysite/page_detail.html'
