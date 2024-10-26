try:
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.common.by import By
except ModuleNotFoundError as e:
    print(e)
    print("try the following codes")
    print("pip install selenium")
    

class tbxYoutube():
    def __init__(self, driverPath):
        

        path_to_extension = fr'./Tbxtube_adblock.crx'
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_extension(path_to_extension)

        #open browser
        headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS  10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36", "Accept":"text/html,application/xhtml+xml,application/xml; q=0.9,image/webp,image/apng,*/*;q=0.8"}
        browser = webdriver.Chrome(driverPath, chrome_options=chrome_options)
        browser.create_options()