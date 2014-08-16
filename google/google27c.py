# Embedded file name: google27.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import NoSuchElementException
import re
from datetime import datetime, timedelta
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

executable_path = 'Scripts\\chromedriver.exe'
dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = (
    "Mozilla/5.0 (X11; Linux x86_64; en-US) AppleWebKit/53 "
    "(KHTML, like Gecko) Chrome/15.0.87"
)


driver = webdriver.Chrome(executable_path)#,desired_capabilities=dcap)
driver.set_window_size(1400,1000)
url = """https://www.google.com/maps/search/Adult+Entertainment+Store/@
42.5604535,
-72.7380727"""
driver.get(url)
time.sleep(10)
driver.save_screenshot('screenie.png')
f = open('out.csv', 'wb')
log = open('log.txt', 'wb')

Etime = 0
a = {1}
a.clear()
out = set()
z = open('12345.txt','r')
q = z.read()


def loop():
    for i in range(6,16):
            #try:
        
                print (i-6)
                adresspath="""//*[@id="text-mode-left-content"]/div/div["""+str(i)+']/div[1]/div[4]/span[1]'
                adress = driver.find_element_by_xpath(adresspath)
                if adress.text.encode('utf-8') in q:
                    continue
                if adress.text not in out:
                    titlepath="""//*[@id="text-mode-left-content"]/div/div["""+str(i)+']/div[1]/h3'
                    title = driver.find_element_by_xpath(titlepath)
                    f.write(title.text.replace('\n',' ').encode('utf-8')+';')
                    f.write(adress.text.replace('\n',' ').encode('utf-8')+';')
                    xpath = """//*[@id="text-mode-left-content"]/div/div["""+str(i)+']'
                    elem = driver.find_element_by_xpath(xpath)
                    
                    out.add(adress.text)
                    phonepath="""//*[@id="text-mode-left-content"]/div/div["""+str(i)+']/div[1]/div[4]/span[3]'
                    phone = driver.find_element_by_xpath(phonepath)
                    f.write(phone.text.replace('\n',' ').encode('utf-8')+';')
                    print('found,waiting')
                    time.sleep(0.2)
                    elem.click()
                    print('elem clicking')
                    time.sleep(0.2)
                    wpath = """//*[@id="text-mode-left-content"]/div/div["""+str(i)+']/div[3]/div[1]/span[1]/a'
                    link = driver.find_element_by_xpath(wpath)
                    #print link.text
                    if link.text:
                        f.write('http://'+link.text.replace('\n',' ').encode('utf-8')+';')
                    f.write('\n')
##                
##                t = driver.find_element_by_xpath("""//*[@id="text-mode-left-content"]/div/div["""+str(i)+"""]/div[3]/div[3]/a""")
##                if t.is_displayed():
##                    print('table clicking')
##                    t.click()
##                    time.sleep(0.1)
##                    tpath = """//*[@id="lightbox"]/div/div/div/div/div/div/table/tbody"""
##                    table = driver.find_element_by_xpath(tpath)
##                    #driver.find_element_by_xpath("""//*[@id="lightbox"]/div/div/div/div/div/div/table/tbody/tr[7]""")
##                    time.sleep(0.1)
##                    #print table.text.replace('\n',' ')
##                    f.write(table.text.replace('\n',' ').encode('utf-8'))
##                    time.sleep(0.1)
                
##                time.sleep(0.2)
##
##                print('click head')
##                x = driver.find_element_by_xpath("""//*[@id="text-mode-left-content"]/div/div["""+str(i)+']/div[1]')
##                print(x.text)
##                x.click()
##                print('end elem')
##                time.sleep(1)
            #except Exception:
            #    print('caught exc')
for k in [40,50,60]:
    for j in [-90,-80,-70,-60]:

        url = """https://www.google.com/maps/search/Adult+Entertainment+Store/@"""
        url = url+str(k)+","+str(j)+",7z/am=t?hl=en"
        driver.get(url)
        time.sleep(7)
        print('new url:',url)
        
        print('all 10 done')
        try:
            
             while True:   
                try:
                    time.sleep(0.5)
                    loop()
                    path = """//*[@id="text-mode-left-content"]/div/div[16]/a[2]"""
                    time.sleep(0.5)        
                    print 'looking for button'          
                    #elem = driver.find_element_by_xpath(path)
                    button = driver.find_element_by_xpath(path)
                    time.sleep(1)
                    print (button.text)
                    
                    button.click()
                    print 'founded, clicked'
                    time.sleep(1)
                    
                    
                    

                except (NoSuchElementException):
                    Etime = 0
                    print 'Not found'
                    time.sleep(0.5)
                    button = driver.find_element_by_xpath(path)
                    button.click()
##                    while Etime < 1:
##                        try:
##                            button = driver.find_element_by_xpath(path)
##                            
##                            
##                            
##                            print('try')
##                            break
##                        except (NoSuchElementException, Exception):
##                            Etime += 0.1
##                            time.sleep(0.2)
##                            print('again...')
##                        finally:
##                            if Etime > 1:
##                                raise NoSuchElementException
##                                print 'No button caught'
                    

        except Exception:
            print('Sample ended')



f.close()
log.close()
print 'Done.'
print 'Output: out.csv'
