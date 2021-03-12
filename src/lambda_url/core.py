from typing import List

from django.conf.urls.i18n import i18n_patterns
from django.urls import path as base_path

__all__ = [
    'URLPatterns',
    'path',
]


def path(route, view, *args, i18n=False, **kwargs):
    return base_path(route, view, *args, **kwargs), i18n


class URLPatterns:
    urls = []

    _patterns = []
    _i18n_patterns = []

    def __new__(cls, *urls: List[path], **kwargs):
        for (url_path, is_i18n) in (cls.urls + list(urls)):
            cls._i18n_patterns.append(url_path) if is_i18n else cls._patterns.append(url_path)
        if cls._i18n_patterns:
            return cls._patterns + i18n_patterns(*cls._i18n_patterns)
        return cls._patterns
