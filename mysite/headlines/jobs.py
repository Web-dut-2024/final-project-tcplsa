import requests
from bs4 import BeautifulSoup
import re
import json
import os

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
}

import os
os.chdir(os.path.dirname(__file__))




def get_headlines():
    url = "https://blog.csdn.net/phoenix/web/blog/hot-rank?page=0&pageSize=25&type="
    response = requests.get(url, headers=headers)
    json_html = json.loads(response.text)
    return json_html['data']

def get_tags(url):
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    script_tag = soup.find('script', string=re.compile("toolbarSearchExt"))
    if script_tag:
        script_text = script_tag.string
        c = script_text.split('=')[1]
        c = c.rstrip().rstrip(';').rstrip("'").lstrip().lstrip("'")
        json_data = json.loads(c)
        return json_data.get('tag', [])
    else:
        return []

def save_article_to_json(article, directory):
    # 创建保存文章的目录
    if not os.path.exists(directory):
        os.makedirs(directory)

    # 生成文件名，替换不合适的字符
    title1 = article['title'].replace('/', '-').replace('\\', '-').replace(':', '-').replace('|', '-')
    filename = f"{directory}/{title1}.json"

    # 将文章信息转换为 JSON 格式
    json_data = json.dumps(article, indent=4, ensure_ascii=False)

    # 保存 JSON 数据到文件
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(json_data)


def save_todayarticle_to_json(article, directory="../today_entries"):
    # 创建保存文章的目录
    if not os.path.exists(directory):
        os.makedirs(directory)

    

    # 生成文件名，替换不合适的字符
    title1 = article['title'].replace('/', '-').replace('\\', '-').replace(':', '-').replace('|', '-')
    filename = f"{directory}/{title1}.json"

    # 将文章信息转换为 JSON 格式
    json_data = json.dumps(article, indent=4, ensure_ascii=False)

    # 保存 JSON 数据到文件
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(json_data)
 
def clear_folder(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)
        elif os.path.isdir(file_path):
            clear_folder(file_path)
            os.rmdir(file_path)


def github():
    url="https://github.com/trending"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
    # 使用BeautifulSoup解析HTML内容
        soup = BeautifulSoup(response.text, 'html.parser')
    
        # 找到包含仓库信息的div
        repositories = soup.find_all('article', class_='Box-row')
    
        # 遍历仓库信息并打印
        for repo in repositories:
            # 获取仓库名称
            repo_nameo = repo.find('a',class_="Link").text.strip()
            repo_name=''
            for i in repo_nameo:
                if (ord(i)>32 and ord(i) !=47) or i == "/":
                   repo_name += i


            # repo_name=repo_fa_name+repo_name
            # 获取仓库描述
            repo_description = repo.find('p', class_='col-9 color-fg-muted my-1 pr-4').text.strip()
            # 获取语言
            language = repo.find('span', class_='d-inline-block ml-0 mr-3').text.strip()
            # 打印仓库信息
            repo_url="https://github.com/"+repo_name
            print(f"Name: {repo_name}\nDescription: {repo_description}\nLanguage: {language}\nURL: {repo_url}")
            pakage = {
                'title' : repo_name,
                'url' : repo_url,
                'tags' : [language],
                'description' : repo_description,
                'pic' : "https://pic4.zhimg.com/v2-341e1d3b2845db15bceeff70d3fe228b_r.jpg"
            }
            save_article_to_json(pakage,"../GIT")
            save_article_to_json(pakage,"../entries")
            save_todayarticle_to_json(pakage)
    
    else:
        print("请求失败")


# articles_data = get_headlines()
# for item in articles_data:
#         article = {
#             'title': item['articleTitle'],
#             'url': item['articleDetailUrl'],
#             'pic': item['picList'][0] if item['picList'] else None,
#             'tags': get_tags(item['articleDetailUrl'])
#         }
#         save_article_to_json(article,"../entries")
#         save_article_to_json(article,"../CSDN")

def main():
    articles_data = get_headlines()
    clear_folder("../today_entries")
    for item in articles_data:
        article = {
            'title': item['articleTitle'],
            'url': item['articleDetailUrl'],
            'pic': item['picList'][0] if item['picList'] else None,
            'tags': get_tags(item['articleDetailUrl'])
        }
        save_article_to_json(article,"../entries")
        save_article_to_json(article,"../CSDN")
        save_todayarticle_to_json(article)
    github()
    


if __name__ == "__main__":
    main()
