# 웹스크랩핑 테스트 준비
import requests
from bs4 import BeautifulSoup

url = 'https://www.naver.com/'

resp = requests.get(url)

html = """
<nav class="menu-box-1" id="menu-box">
  <ul>
    <li>
      <a href="https://www.naver.com">네이버로 이동</a>
    </li>
    <li>
      <a href="https://www.daum.net">다음으로 이동</a>
    </li>
    <li>
      <a href="https://www.google.com">구글로 이동</a>
    </li>
  </ul>
</nav>
"""

bs = BeautifulSoup(html, 'html.parser')

a_tags = bs.select('a')

#  해당 엘리먼트가 품고 있는 텍스트 추출
for tags in a_tags:
  print(tags.get_text())

# 해당 엘리먼트가 가지고 있는 속성 추출
for tags in a_tags:
  print(tags.get('href'))