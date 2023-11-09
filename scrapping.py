from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


driver_path = ChromeDriverManager().install()

service = Service(driver_path)

options = webdriver.ChromeOptions()
options.add_argument("--headless") 

driver = webdriver.Chrome(service=service, options=options)


url = "https://news.yahoo.co.jp/comment-timeline/"

driver.get(url)

html_content = driver.page_source


soup = BeautifulSoup(html_content, "html.parser")
button_tags = soup.find_all("button", class_="ViolationButton__Button-fbEoqd jaimVy", attrs={"data-cl-params": True})
cm_ids = []


for element in button_tags:
    data_cl_params = element["data-cl-params"]
    data_cl_params = data_cl_params.replace(";",",")
    split_text = data_cl_params.split(",")
    for pair in split_text:
        split = pair.split(':')
        if split[0] == "cmt_id":
            cm_ids.append(split[1])



print(cm_ids)




# div_tags = soup.find_all("div", class_="sc-gPVtyz bpeoSO")
# categories = []

# for span_tag in div_tags:
# 	span_tags = span_tag.find_all("span")

# 	for span_tag in span_tags:
# 		categories.append(span_tag.text)
# 		# print(span_tag.text)

# print(categories)

# div_tags = soup.find_all("p", class_="sCommentBlock__CommentText-kyLszc jHlOo")
# print(div_tags)