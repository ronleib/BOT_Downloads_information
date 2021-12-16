import time

from Algo import story_Good_bed
from __library import *
from initialization_Url import i_Url


def dec_HeadTital_Url(driver):
    Url_Articles_List={}
    table_ids = driver.find_elements_by_class_name(getArticlesAll)
    time.sleep(1.1)

    for x in table_ids:

       try:
           temp_url=x.find_element_by_class_name(clasArticles_media).get_attribute(getUrl)
           head_Tital = x.find_element_by_class_name(clasArticles_media).text
           Url_Articles_List.update({head_Tital:temp_url})
           #print(x.find_elements_by_class_name('media__link')[0].get_attribute("href"))
       except:
           pass

       finally:
        try:
            temp_url=x.find_element_by_class_name(clasArticles_reel).get_attribute(getUrl)
            head_Tital = x.find_element_by_class_name(clasArticles_reel).text
            Url_Articles_List.update({head_Tital:temp_url})
           #print(x.find_elements_by_class_name('reel__link')[0].get_attribute("href"))
        except:
            pass

    return Url_Articles_List


def Content_extraction(list):
    Url_Articles_Content={}
    All_text_Articles=""
    index_Articles =1;
    for Articles in list:
        driver = i_Url(list[Articles])
        All_text=""
        Skipping_In(driver)

        Contents =Contents_Get_class(driver)
        time.sleep(1.1)

        for Content in Contents:
            All_text = All_text + Content.text
        All_text_Articles = All_text_Articles +"|Articles_"+ str(index_Articles)+"| "+ All_text
        Url_Articles_Content.update({Articles : All_text})
        driver.close()
    return Url_Articles_Content,All_text_Articles

def Contents_Get_class(driver):
    listadres=listContents
    for x in listadres:
        temp = Get_driver_lo(driver,x)
        if(temp != 1):
            return temp
    return []


def Get_driver_lo(driver,adres):
    try:
        return driver.find_elements_by_class_name(adres)
    except:
        return 1

def Skipping_In(driver):
    try:
        no_button = driver.find_element_by_class_name(Button_close)
        no_button.click()
        #print("yes Skipping..")
    except:
        #print("No Skipping..")
        pass

def story_Good_bed_Bcc(list):
    print("The emotion classification of the articles")
    for Articles in list:
        temp = story_Good_bed(Articles)["compound"]
        if temp >= 0:
            print(Articles +":"+"Good")
        else:
            print(Articles + ":" + "bed")

