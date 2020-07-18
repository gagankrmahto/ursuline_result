
from typing import SupportsIndex
from selenium import webdriver
# import time
# import random
import json
marksheet = []
def_roll_code=11066
curr_roll_number=10000
driver = webdriver.Chrome("chromedriver.exe")
def result(curr_roll_number):
    try:
        driver.get("https://www.jacresults.com/science/index.php")

        roll_code = driver.find_element_by_xpath("/html/body/form/div/div/div/div/div[1]/table/tbody/tr[2]/td[2]/input")
        roll_code.send_keys(def_roll_code)
        roll_no = driver.find_element_by_xpath("/html/body/form/div/div/div/div/div[1]/table/tbody/tr[3]/td[2]/input")
        roll_no.send_keys(curr_roll_number)

        submit = driver.find_element_by_xpath("/html/body/form/div/div/div/div/div[2]/div[1]/button")
        submit.click()
        # Marksheet gen
        S_name = driver.find_element_by_xpath("/html/body/form/div/div/div[1]/table/tbody/tr[3]/td[2]")
        F_Name = driver.find_element_by_xpath("/html/body/form/div/div/div[1]/table/tbody/tr[4]/td[2]")
        Institute = driver.find_element_by_xpath("/html/body/form/div/div/div[1]/table/tbody/tr[6]/td[2]")
        Marks = driver.find_element_by_xpath("/html/body/form/div/div/div[2]/table/tbody/tr[7]/td[2]")
        Result = driver.find_element_by_xpath("/html/body/form/div/div/div[2]/table/tbody/tr[8]/td[2]")
    
        marks={"Roll No.":curr_roll_number,
        "Student's Name":S_name.text,
        "Father's Name":F_Name.text,
        "Institution":Institute.text,
        "Total Marks":Marks.text,
        "Result":Result.text,
        }
        marksheet.append(marks)

    except Exception as e:
        print(e)
def Topper(num):
    try:
        topper=sorted(marksheet, key=lambda k: k['Total Marks'],reverse=True)[-num]
        # print(topper)
        return topper
    except Exception as e:
        print(e)
    
if __name__ == "__main__":
    for i in range(10001,10799):
        result(i)
    
    with open('reports/ursuline.json', 'w') as f:
        json.dump(Topper(-1),f)
        json.dump(Topper(-2),f)
        json.dump(Topper(-3),f)
        json.dump(marksheet, f)
        
    print("Done...")
