import threading

from All_data import All_data
from Algo import bild_list_Fligt, seav_data, seav_data_dec
from Algo_json import Bild_Json, Seve_Json, Read_Json
from Bcc_Articles import dec_HeadTital_Url, Content_extraction, story_Good_bed_Bcc
from __library import table_id
from initialization_Url import i_Url
from selenium.webdriver.common.by import By
import time
from selenium import webdriver

from timeAupdet_Selenium import timeAupdet_Selenium

if __name__ == '__main__':
    driver = i_Url("https://www.bbc.com/")
    time.sleep(1.1)
    list = dec_HeadTital_Url(driver)
    driver.close()
    All_test_data = All_data()
    testHes , data_C =Content_extraction(list)
    All_test_data.add(data_C)
    seav_data_dec(list,"{HeadTital : Url}")
    seav_data_dec(testHes, "{HeadTital : Content}")
    seav_data(All_test_data.getAll(), "All_Content")
    temp_chack = input("Please enter what you want to Search: \n")
    All_test_data.check_infut(temp_chack)
    story_Good_bed_Bcc(list)

    print("----------------------------------Q2------------------------------ ")
  # ----------------------------------Q2------------------------------



    driver_Q2 = i_Url("https://www.iaa.gov.il/airports/ben-gurion/flight-board")
    time.sleep(1.5)
    tableId = driver_Q2.find_element(By.ID, table_id)
    time_ = timeAupdet_Selenium(driver_Q2)
    ferst = True
    index_tab =1
    temp_all_Q2 = All_data()
    while True:
        if time_.timeChanged(driver_Q2) or ferst:
            ferst = False
            temp_s = tableId.text
            temp_all_Q2.add(temp_s)
            list = bild_list_Fligt(temp_s.split("\n"))
            name_file_Json = "fligt_tab"+str(index_tab)
            S_J = Seve_Json(Bild_Json(list), name_file_Json)
            R_J = Read_Json(name_file_Json)
            index_tab =index_tab+1
        temp_chack = input("If you want to search for a word, write Enter 1 or you went out Enter 0: \n")
        if temp_chack == '1':
            temp_chack = input("Please enter what you want to Search: \n")
            temp_all_Q2.check_infut(temp_chack)
        else:
            if temp_chack == '0':
                break
    driver_Q2.close()



