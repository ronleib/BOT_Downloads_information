from __library import updating_Time


class timeAupdet_Selenium:
    time="";

    def __init__(self,driver):
        self.time=driver.find_element_by_id(updating_Time).text

    def timeAupdet(self,driver):
        return driver.find_element_by_id(updating_Time).text


    def timeChanged(self,driver):
        new_time=self.timeAupdet(driver)
        if self.time != new_time:
            self.time=new_time
            return True
        else:
            return False