from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException


class NoSeleniumWebdriverFound(Exception):
    pass

class ProcessingNotDone(Exception):
    pass


class QuickScrape:
    def __init__(self, path_of_selenium_chrome_driver="C:\Program Files (x86)\chromedriver.exe"):
        try:
            self.path = path_of_selenium_chrome_driver
        except:
            raise NoSeleniumWebdriverFound("The selenium chrome driver was not found")

    def process(self, headless=True):
        # put headless=False for different results
        chrome_options = Options()
        chrome_options.headless = headless

        self.driver = webdriver.Chrome(self.path, options=chrome_options)

    def featured_snippet(self, text):
        if isinstance(text, str) == False:
            raise TypeError("Text Has to be a string")
        else:
            try:
                self.driver.get(f"https://www.google.com/search?q={text}")
                self.driver.implicitly_wait(5)

                featured_snippet = self.driver.find_element_by_xpath(
                    '//*[@id="rso"]/div[1]/div/div[1]/div')
                return featured_snippet.text
            except AttributeError:
                raise ProcessingNotDone('Please run process method before ending')
            except NoSuchElementException as e:
                print("No featured snippet")

    def summary_para(self, text):
        if isinstance(text, str) == False:
            raise TypeError("Text Has to be a string")
        else:
            try:
                self.driver.get(f"https://www.google.com/search?q={text}")
                self.driver.implicitly_wait(5)

                summary_para = self.driver.find_element_by_class_name('hgKElc')
                return summary_para.text
            except AttributeError:
                raise ProcessingNotDone('Please run process method before ending')
            except NoSuchElementException as e:
                print("No summary para")


    def wiki_article(self, text):
        if isinstance(text, str) == False:
            raise TypeError("Text Has to be a string")
        else:
            try:
                self.driver.get(f"https://www.google.com/search?q={text}")
                self.driver.implicitly_wait(5)

                wiki = self.driver.find_element_by_class_name('kno-rdesc')
                return wiki.text
            except AttributeError:
                raise ProcessingNotDone('Please run process method before ending')
            except NoSuchElementException as e:
                print("No wikipedia article")


    def end(self):
        try:
            self.driver.close()
        except:
            raise ProcessingNotDone('Please run process method before ending')


