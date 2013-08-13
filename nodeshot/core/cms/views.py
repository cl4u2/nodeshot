import simplejson as json

from django.utils.translation import ugettext_lazy as _
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from rest_framework import generics, authentication
from rest_framework.response import Response

from nodeshot.core.base.mixins import ACLMixin

from .serializers import *
from .models import *


class PageList(ACLMixin, generics.ListAPIView):
    """
    ### GET
    
    Retrieve the list of pages.
    """
    authentication_classes = (authentication.SessionAuthentication,)
    queryset = Page.objects.published()
    serializer_class = PageListSerializer
    
    @method_decorator(cache_page(86400))  # cache for 1 day
    def dispatch(self, *args, **kwargs):
        return super(self.__class__, self).dispatch(*args, **kwargs)
    
page_list = PageList.as_view()


class PageDetail(ACLMixin, generics.RetrieveAPIView):
    """
    ### GET
    
    Retrieve specified page.
    """
    authentication_classes = (authentication.SessionAuthentication,)
    queryset = Page.objects.published()
    serializer_class = PageDetailSerializer
    
    @method_decorator(cache_page(86400))  # cache for 1 day
    def dispatch(self, *args, **kwargs):
        return super(self.__class__, self).dispatch(*args, **kwargs)
    
page_detail = PageDetail.as_view()


# ------ Menu ------ #


class MenuList(ACLMixin, generics.ListAPIView):
    """
    ### GET
    
    Retrieve the list of pages.
    """
    authentication_classes = (authentication.SessionAuthentication,)
    queryset = MenuItem.objects.published()
    serializer_class = MenuSerializer
    
    @method_decorator(cache_page(86400))  # cache for 1 day
    def dispatch(self, *args, **kwargs):
        return super(self.__class__, self).dispatch(*args, **kwargs)
    
menu_list = MenuList.as_view()