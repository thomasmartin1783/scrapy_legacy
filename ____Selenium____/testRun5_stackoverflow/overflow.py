from encodings import utf_8
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

import pandas as pd

output_file = "output.xlsx"
sheet_name = 'Sheet1'

df = pd.DataFrame([['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ]],
                  index=["row1"]
                  )
df.to_excel(output_file, sheet_name=sheet_name)


website_1 = "https://stackoverflow.com/questions/tagged/multithreading?sort=MostVotes&page=1&pagesize=50"

s = Service("C:\webdrivers\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get(website_1)

try:
    cookies = driver.find_element(By.XPATH, '/html/body/div[4]//button[1]')
    cookies.click()
    # print("clicked")
except:
    print("="*50)


for i in range(0, 50):
    try:
        question_link = driver.find_element(
            By.XPATH, f'//div[@id="questions"]//div[{i+1}]//div[@class="s-post-summary--stats-item has-answers has-accepted-answer"]')

        link = driver.find_element(
            By.XPATH, f'//div[@id="questions"]//div[{i+1}]//div[@class="s-post-summary--content"]//a')
        link_text = link.get_attribute('href')
        print(link_text)
        link.click()

        question = driver.find_element(
            By.XPATH, '//a[@class="question-hyperlink"]')
        question_text = question.text
        print(question_text)

        question_body = driver.find_element(
            By.XPATH, '//div[@class="s-prose js-post-body"]')
        question_body_text = question_body.text
        # print(question_body.text)
        print("======question body")

        answer_count = driver.find_element(
            By.XPATH, '//span[@itemprop="answerCount"]')
        answer_count_value = answer_count.get_attribute('innerHTML')
        print(answer_count_value)

        accepted_answer = driver.find_element(
            By.XPATH, '//div[@id="answers"]//div[@class="answer js-answer accepted-answer js-accepted-answer"]//div[@class="s-prose js-post-body"]')
        accepted_answer_text = accepted_answer.text

        print("accepted  ")
        # global a
        a = [" "]*23

        if(int(answer_count_value) > 20):
            print("entered")
            for i in range(0, 20):
                all_answers = driver.find_element(
                    By.XPATH, f'//div[@id="answers"]//div[@class="answer js-answer"][{i+1}]//div[@class="s-prose js-post-body"]')
                # print(all_answers.text)
                a[i] = all_answers.text
                # print("all text printed")
                print(i, end="\t")
        else:
            print("entered else")
            for i in range(0, int(answer_count_value)):
                all_answers = driver.find_element(
                    By.XPATH, f'//div[@id="answers"]//div[contains(@class,"answer js-answer")][{i+1}]//div[@class="s-prose js-post-body"]')
                a[i] = all_answers.text
                print(i, end="\t")

        df3 = pd.DataFrame([[question_text, question_body_text, accepted_answer_text,
                            a[0], a[1], a[2], a[3], a[4], a[5], a[6], a[7], a[8], a[9], a[10], a[11], a[12], a[13], a[14], a[15], a[16], a[17], a[18], a[19]]],
                           index=[link_text],
                           )

        with pd.ExcelWriter(output_file, mode='a', if_sheet_exists="overlay") as writer:
            df3.to_excel(writer, sheet_name=sheet_name,
                         startrow=writer.sheets[sheet_name].max_row, header=None)

        print(len(a))

        # driver.execute_script("window.history.go(-1)")
        time.sleep(1)
        driver.back()
        time.sleep(2)

    except:
        print("="*20, "> doesn't exist")
        continue


# print(link)

# time.sleep(2)
# bangla = driver.find_element(
#     By.XPATH, '//input[@id="sl_list-search-box"]')
# bangla.send_keys("bangla" + Keys.ENTER)


# input_text = driver.find_element(
#     By.XPATH, '//textarea[@id="tw-source-text-ta"]')
# time.sleep(1)
# out_csv = []
# output_csv_file = "output_xl5.csv"

# # for i in range(len(var1)):
# for i in range(len(var1)):
#     out_csv = []
#     # print(i)
#     try:
#         input_text.clear()
#         input_text.send_keys(var1[i])

#         # output_text = driver.find_element(
#         #     By.XPATH, '//div[@id="tw-target-text-container"]//span')
#         # print("*"*50, output_text.text)
#         time.sleep(1)
#         output_text = driver.find_element(
#             By.XPATH, '//div[@id="gt-src-is"]//div[@class="gt-is-lb"]/div')
#         # By.XPATH, '//div[@id="tw-target-text-container"]//span')
#         output_text_value = output_text.text
#         # print("*"*50, output_text_value)
#         print(
#             f"{i} ==> {type(output_text_value)}  |  {output_text_value[:15]}")

#         out_csv.append(output_text_value)

#         # for i in out_csv:
#         #     with open("output_xl5.csv", "ab") as file:
#         #         foo = f"\"{i}\",\n"
#         #         file.write(foo.encode('utf-8'))

#         with open(output_csv_file, "ab") as file:
#             foo = f"\"{out_csv[0]}\",\n"
#             file.write(foo.encode('utf-8'))

#         time.sleep(.3)

#     except:
#         print(f"{i} ==> expection", "="*20)
#         with open(output_csv_file, "ab") as file:
#             foo = f"\"\",\n"
#             file.write(foo.encode('utf-8'))
#         continue


# time.sleep(300)
