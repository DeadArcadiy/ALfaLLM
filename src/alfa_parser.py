from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd
from tqdm import tqdm
import time
 
def get_info(n,driver):
    url = 'https://infocenter.alfabank.by/article/' + str(n)

    driver.get(url)

    try:
        element = WebDriverWait(driver, 1).until(
        EC.presence_of_element_located((By.CLASS_NAME, "Layout_content__95Ydx")))
        time.sleep(0.2)
        html = driver.page_source    
        soup = BeautifulSoup(html, 'html.parser')
        

        if soup.find_all('div',class_='Layout_content__95Ydx')[0].text == 'Статья не найдена':
            return pd.DataFrame()
        else:

            WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "ArticleCard_body__M8mdJ"))
    )

            time.sleep(2)
            all = soup.find_all('span')

            previous = '-'
            current_field = ''
            dict = {'Вопрос':[''],'Окружение':[''],'Ответ':['']}

            for a in all: 
                if previous[:len(a.text)] != a.text:
                    if a.text == 'Вопрос':
                        current_field = 'Вопрос'
                    elif a.text == 'Окружение':
                        current_field = 'Окружение'
                    elif a.text == 'Ответ':
                        current_field = 'Ответ'
                    else:
                        dict[current_field][0] += a.text
                previous = a.text

            return pd.DataFrame(dict)
    except:
        return pd.DataFrame()




if __name__ == '__main__':
    driver = webdriver.Safari()
    data = pd.DataFrame({'Вопрос':[],'Окружение':[],'Ответ':[]})
    for i in tqdm(range(1,5000)):
        newdata = get_info(i,driver)
        if not newdata.empty:
            data = pd.concat([data, newdata], ignore_index=True)

    print('FINISHED')

    data.to_csv('data/result.csv')
    data = data.dropna()
    driver.quit()
