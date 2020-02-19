from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

wd = webdriver.Firefox()
wd.get('https://www.nbp.pl/home.aspx?c=/ascx/archa.ascx')
selects = wd.find_elements_by_xpath("//select")
# rok_select.select_by_visible_text('2005')
accept = wd.find_element_by_id('ctl25_btAscxSubmit')
rok_select = selects[0]
mies_select = selects[1]
print(mies_select.text)

time.sleep(1)

year_select = Select(rok_select)
year_select.select_by_visible_text('2005')

month_select = Select(mies_select)
month_select.select_by_visible_text(' maj ')

time.sleep(1)

accept.click()