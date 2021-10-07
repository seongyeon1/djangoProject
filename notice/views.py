from django.views.generic import View, ListView, DetailView, FormView, CreateView
from .models import Notice
from django.db.models import Q
from django.contrib import messages


# 공지사항 게시판 권한
# level 2,3 = READ
# level 1 관리자 = CREATE, READ + 본인 글 UPDATE, DELETE
# level 0 개발자 = CREATE, READ, UPDATE, DELETE

# 공지사항 리스트 뷰
class NoticeList(ListView):
    model = Notice
    paginate_by = 15
    template_name = 'notice/notice_list.html'  # DEFAULT : <app_label>/<model_name>_list.html
    context_object_name = 'notice_list'  # DEFAULT : <app_label>_list

    def get_queryset(self):
        search_keyword = self.request.GET.get('q', '')
        search_type = self.request.GET.get('type', '')
        notice_list = Notice.objects.order_by('-id')

        if search_keyword:
            if len(search_keyword) > 1:
                if search_type == 'all':
                    search_notice_list = notice_list.filter(
                        Q(title__icontains=search_keyword) | Q(content__icontains=search_keyword) | Q(
                            writer__user_id__icontains=search_keyword))
                elif search_type == 'title_content':
                    search_notice_list = notice_list.filter(
                        Q(title__icontains=search_keyword) | Q(content__icontains=search_keyword))
                elif search_type == 'title':
                    search_notice_list = notice_list.filter(title__icontains=search_keyword)
                elif search_type == 'content':
                    search_notice_list = notice_list.filter(content__icontains=search_keyword)
                elif search_type == 'writer':
                    search_notice_list = notice_list.filter(writer__user_id__icontains=search_keyword)

                # if not search_notice_list :
                #     messages.error(self.request, '일치하는 검색 결과가 없습니다.')
                return search_notice_list
            else:
                messages.error(self.request, '검색어는 2글자 이상 입력해주세요.')
        return notice_list

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
        search_type = self.request.GET.get('type', '')
        notice_fixed = Notice.objects.filter(top_fixed=True).order_by('-registered_date')

        if len(search_keyword) > 1:
            context['q'] = search_keyword
        context['type'] = search_type
        context['notice_fixed'] = notice_fixed

        return context

class NoticeDetail(DetailView):
    model = Notice
    template_name = 'notice/notice_detail.html'