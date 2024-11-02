import re
import json
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
import os

import re

from django.core.files.base import ContentFile
from django.core.files.storage import default_storage


def list_entries():
    """
    Returns a list of all names of encyclopedia entries.
    """
    _, filenames = default_storage.listdir("entries")
    return list(sorted(re.sub(r"\.json$", "", filename)
                for filename in filenames if filename.endswith(".json")))

def list_entries_with_urls():
    """
    Returns a list of dictionaries containing the names and 'url' values
    of all encyclopedia entries.
    """
    _, filenames = default_storage.listdir("today_entries")
    entries_with_urls = []
    for filename in filenames:
        if filename.endswith(".json"):
            file_path = os.path.join("today_entries", filename)
            # 读取 JSON 文件内容
            file_content = default_storage.open(file_path).read()
            # 解析 JSON 文件内容
            entry_data = json.loads(file_content)
            # 创建一个字典，包含条目标题和 url 值
            entry_info = {
                'title': entry_data.get('title', ''),
                'url': entry_data.get('url', ''),  # 获取 url 字段，如果不存在则返回空字符串
                'pic': entry_data.get('pic', ''), 
                'tags': entry_data.get('tags', ''),
                'description': entry_data.get('description','')
            }
            entries_with_urls.append(entry_info)
    # 对结果列表按标题排序
    return sorted(entries_with_urls, key=lambda x: x['title'])

def list_entries_with_urls_CSDN():
    """
    Returns a list of dictionaries containing the names and 'url' values
    of all encyclopedia entries.
    """
    _, filenames = default_storage.listdir("CSDN")
    entries_with_urls = []
    for filename in filenames:
        if filename.endswith(".json"):
            file_path = os.path.join("CSDN", filename)
            # 读取 JSON 文件内容
            file_content = default_storage.open(file_path).read()
            # 解析 JSON 文件内容
            entry_data = json.loads(file_content)
            # 创建一个字典，包含条目标题和 url 值
            entry_info = {
                'title': entry_data.get('title', ''),
                'url': entry_data.get('url', ''),  # 获取 url 字段，如果不存在则返回空字符串
                'pic': entry_data.get('pic', ''), 
                'tags': entry_data.get('tags', ''),
                'description': entry_data.get('description','')
            }
            entries_with_urls.append(entry_info)
    # 对结果列表按标题排序
    return sorted(entries_with_urls, key=lambda x: x['title'])

def list_entries_with_urls_GIT():
    """
    Returns a list of dictionaries containing the names and 'url' values
    of all encyclopedia entries.
    """
    _, filenames = default_storage.listdir("GIT")
    entries_with_urls = []
    for filename in filenames:
        if filename.endswith(".json"):
            file_path = os.path.join("GIT", filename)
            # 读取 JSON 文件内容
            file_content = default_storage.open(file_path).read()
            # 解析 JSON 文件内容
            entry_data = json.loads(file_content)
            # 创建一个字典，包含条目标题和 url 值
            entry_info = {
                'title': entry_data.get('title', ''),
                'url': entry_data.get('url', ''),  # 获取 url 字段，如果不存在则返回空字符串
                'pic': entry_data.get('pic', ''), 
                'tags': entry_data.get('tags', ''),
                'description': entry_data.get('description','')
            }
            entries_with_urls.append(entry_info)
    # 对结果列表按标题排序
    return sorted(entries_with_urls, key=lambda x: x['title'])


def list_entries_with_urls_search(tag):
    """
    Returns a list of dictionaries containing the names and 'url' values
    of all encyclopedia entries.
    """
    _, filenames = default_storage.listdir("entries")
    entries_with_urls = []
    for filename in filenames:
        if filename.endswith(".json"):
            file_path = os.path.join("entries", filename)
            # 读取 JSON 文件内容
            file_content = default_storage.open(file_path).read()
            # 解析 JSON 文件内容
            entry_data = json.loads(file_content)
            
            if tag in [item.lower() for item in entry_data.get('tags','')]:
                # 创建一个字典，包含条目标题和 url 值
                entry_info = {
                    'title': entry_data.get('title', ''),
                    'url': entry_data.get('url', ''),  # 获取 url 字段，如果不存在则返回空字符串
                    'pic': entry_data.get('pic', ''), 
                    'tags': entry_data.get('tags', ''),
                    'description': entry_data.get('description','')
                }
                entries_with_urls.append(entry_info)
            elif re.search(tag.lower(), entry_data.get('title', '').lower()) is not None:
                # 创建一个字典，包含条目标题和 url 值
                entry_info = {
                    'title': entry_data.get('title', ''),
                    'url': entry_data.get('url', ''),  # 获取 url 字段，如果不存在则返回空字符串
                    'pic': entry_data.get('pic', ''), 
                    'tags': entry_data.get('tags', ''),
                    'description': entry_data.get('description','')
                }
                entries_with_urls.append(entry_info)
            elif re.search(tag.lower(), entry_data.get('description', '').lower()) is not None:
                # 创建一个字典，包含条目标题和 url 值
                entry_info = {
                    'title': entry_data.get('title', ''),
                    'url': entry_data.get('url', ''),  # 获取 url 字段，如果不存在则返回空字符串
                    'pic': entry_data.get('pic', ''), 
                    'tags': entry_data.get('tags', ''),
                    'description': entry_data.get('description','')
                }
            
        
    # 对结果列表按标题排序
    return sorted(entries_with_urls, key=lambda x: x['title'])