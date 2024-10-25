# bu dosyada selenium kütüphanesinin istediği şekillerde import edildiği varsayılmıştır 
# selenium ile çok kulanılan kütüphaneler import edilecektir çok fazla kullanmak istemiyorum ama 
from selenium.webdriver.common.by import By
from time import sleep


class tbxDriver():
    def __init__(self, driver):
        # Bu driver her zaman yeni bir driver olacak
        # NOTE: driver a selenium nesnesi verilip verilmediğini kontrol etmiyorum. çünkü import etmem gerekecek
        # olabildiğince az şeyi import etmek istiyorum olabildiğince kulnıcıya esneklik tanımak istiyorum
 
        self.driver = driver
        
    def nowgoal_get_live_data(self, id:str, baseUrl="https://live.nowgoal.com/", sleep_time=1):
        # baseUrl yasklı ülkeler için
        # NOTE: kod zamanla gelecekte günceliğini yitirecektir. bildirirseniz düzeltirim(bir ara) 
        # TODO: kod potimize şekilde yeniden yazılacak ve dinamik veri çekme özelliği eklenecek 
        now_goal_baseUrl = baseUrl
        data_list = {}
        driver=self.driver
        url = baseUrl+"match/live-"+id

        if url:
            modified_url = url.replace("match/live", "match/h2h")
            driver.get(modified_url)
        else:
            print("No URL entered!")

        vote = driver.find_element(By.ID, "voteTxt").text.splitlines()

        teams = ["1", "x", "2"]
        data_list["topluluk oyları"] = {teams[vote.index(i)]:i for i in vote}

        istatistik = []
        for i in range(1,6):
            try:
                driver.find_element(By.XPATH, f'//span[@id="strengthOptions"]/li[@option="{i}"]').click()
                sleep(sleep_time)
                istatistik.append(driver.find_element(By.XPATH, '//ul[@id="barCompareList"]/li[1]').text.splitlines())
            except:pass

        try:    
            driver.find_element(By.XPATH, '//span[@id="strengthOptions"]/li[@option="6"]').click()
            sleep(sleep_time)
            istatistik += [[i.text.splitlines()[1], i.text.splitlines()[0], i.text.splitlines()[2]] for i in driver.find_elements(By.XPATH, '//ul[@id="barCompareList"]/li')]
        except:pass

        data_list["Güç Karşılaştırması"] = {i[1]: {"1":i[0], "2":i[2]} for i in istatistik}
        driver.get(url)
        sleep(15*sleep_time)
        data_list["canlı veri"] = {i.text.splitlines()[1]:{"1":i.text.splitlines()[0], "2":i.text.splitlines()[2]} for i in driver.find_elements(By.XPATH, '//div[@id="teamTechDiv_detail"]/div/ul/li')}
        
        return data_list
    def nowgoal_get_live_page(self, baseUrl="https://live.nowgoal.com/", sleep_time=10):
        driver=self.driver
        driver.get(baseUrl)
        sleep(sleep_time)
        return [{"text":i.text, "id":i.get_attribute("matchid")} for i in driver.find_elements(By.XPATH, '//tr[@class="tds"]')]
