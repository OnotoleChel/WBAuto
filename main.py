# main.py
import sys
from selenium.webdriver.common.keys import Keys
from edge_system_checker import check_system_compatibility
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from logger_module import log_v2

log_v2("Начало проверки системной совместимости", "info")
bIsSystemReady = check_system_compatibility()

if bIsSystemReady:
    sTargetUrl = "https://www.wildberries.ru/"
    iWaitSeconds = 5
    
    log_v2("Запуск браузера MSEdge", "info")
    oDriver = webdriver.Edge()
    
    log_v2(f"Открытие URL: {sTargetUrl}", "info")
    oDriver.get(sTargetUrl)
    
    log_v2(f"Ожидание {iWaitSeconds} секунд", "info")
    time.sleep(iWaitSeconds)
    
    #проверяем готовность к логину, если нет - всё ок
    try:
        WebDriverWait(oDriver, iWaitSeconds).until(
            EC.presence_of_element_located((By.XPATH, "//a[@class='navbar-pc__link j-main-login j-wba-header-item']"))
        )
        log_v2("Элемент 'Войти' найден, требуется логин через SMS", "info")
        #input("Press Enter после авторизации")
    except:
        log_v2("Проверяю залогинен ли", "info")
    
    """    
    #проверяем залогиненость, если нет - прерывает код
    try:
        WebDriverWait(oDriver, iWaitSeconds).until(
            EC.presence_of_element_located((By.XPATH, "//a[@class='navbar-pc__icon navbar-pc__icon--profile']"))
        )
        log_v2("Залогинен, продолжаю работу", "info")
    except:
        log_v2("Не залогинен, требуется прервать исполнение", "error")
        #sys.exit()
    """
    
    # Ввод в поле поиска и нажатие Enter
    try:
        log_v2("Поиск поля ввода поиска", "info")
        oSearchInput = WebDriverWait(oDriver, iWaitSeconds).until(
            EC.presence_of_element_located((By.ID, "searchInput"))
        )
        oSearchInput.clear()
        oSearchInput.send_keys("телевизор")
        oSearchInput.send_keys(Keys.RETURN)
        log_v2("Выполнен поиск по запросу 'телевизор'", "info")
    except:
        log_v2("Ошибка при выполнении поиска", "error")
    
    # НОВЫЙ БЛОК: Клик по кнопке "Готово"
    try:
        log_v2("Поиск кнопки 'Готово'", "info")
        oDoneButton = WebDriverWait(oDriver, iWaitSeconds).until(
            EC.element_to_be_clickable((By.XPATH, 
                "//button[contains(@class, 'filter-btn__main') and contains(., 'Готово')]"
            ))
        )
        oDoneButton.click()
        log_v2("Кнопка 'Готово' успешно нажата", "info")
    except:
        log_v2("Не удалось найти/нажать кнопку 'Готово'", "error")
        
    """
    # Клик по элементу "Бренд" (по data-link)
    try:
        log_v2("Поиск элемента 'Бренд' по data-link", "info")
        oBrandFilter = WebDriverWait(oDriver, iWaitSeconds).until(
            EC.element_to_be_clickable((By.XPATH, 
                "//div[contains(@data-link, 'model.toggleSwitcherFilter')]"
            ))
        )
        oBrandFilter.click()
        log_v2("Элемент 'Бренд' успешно кликнут", "info")
    except:
        log_v2("Не удалось найти/кликнуть элемент 'Бренд'", "error")
    """
    
    # НОВЫЙ БЛОК: Клик по кнопке фильтра
    try:
        log_v2("Поиск кнопки фильтра сортировки", "info")
        oFilterButton = WebDriverWait(oDriver, iWaitSeconds).until(
            EC.element_to_be_clickable((By.XPATH, 
                "//button[contains(@class, 'sorter-mobile__filter') and contains(@data-link, 'filtresModel.showMobileFilters')]"
            ))
        )
        oFilterButton.click()
        log_v2("Кнопка фильтра сортировки успешно нажата", "info")
    except:
        log_v2("Не удалось найти/нажать кнопку фильтра сортировки", "error")
    
    # НОВЫЙ БЛОК: Клик по производителю "Xiaomi"
    try:
        log_v2("Поиск элемента 'Xiaomi' в фильтре производителей", "info")
        oXiaomiFilter = WebDriverWait(oDriver, iWaitSeconds).until(
            EC.element_to_be_clickable((By.XPATH, 
                "//li[contains(@class, 'filter__slide-item')]//button[contains(@class, 'filter__slide-btn') and contains(., 'Xiaomi')]"
            ))
        )
        oXiaomiFilter.click()
        log_v2("Фильтр 'Xiaomi' успешно выбран", "info")
    except:
        log_v2("Не удалось найти/выбрать фильтр 'Xiaomi'", "error")
    
    # НОВЫЙ БЛОК: Клик по размеру "50"
    try:
        log_v2("Поиск элемента '50' в фильтре размеров", "info")
        oSizeFilter = WebDriverWait(oDriver, iWaitSeconds).until(
            EC.element_to_be_clickable((By.XPATH, 
                "//li[contains(@class, 'filter__slide-item')]//button[contains(@class, 'filter__slide-btn') and contains(., '50')]"
            ))
        )
        oSizeFilter.click()
        log_v2("Фильтр '50' успешно выбран", "info")
    except:
        log_v2("Не удалось найти/выбрать фильтр '50'", "error")
    
    # НОВЫЙ БЛОК: Клик по "оригинальный товар"
    try:
        log_v2("Поиск кнопки 'оригинальный товар'", "info")
        oOriginalFilter = WebDriverWait(oDriver, iWaitSeconds).until(
            EC.element_to_be_clickable((By.XPATH, 
                "//button[contains(@class, 'btn-switch__btn') and contains(@class, 'j-filter-switch')]"
            ))
        )
        oOriginalFilter.click()
        log_v2("Фильтр 'оригинальный товар' успешно активирован", "info")
    except:
        log_v2("Не удалось найти/активировать фильтр 'оригинальный товар'", "error")
    
    # НОВЫЙ БЛОК: Ввод цены "от"
    try:
        log_v2("Ввод цены 'от 10'", "info")
        oMinPrice = WebDriverWait(oDriver, iWaitSeconds).until(
            EC.presence_of_element_located((By.NAME, "startN"))
        )
        oMinPrice.clear()
        oMinPrice.send_keys("10")
        log_v2("Цена 'от 10' успешно введена", "info")
    except:
        log_v2("Ошибка при вводе цены 'от'", "error")
    
    # НОВЫЙ БЛОК: Ввод цены "до"
    try:
        log_v2("Ввод цены 'до 1000'", "info")
        oMaxPrice = WebDriverWait(oDriver, iWaitSeconds).until(
            EC.presence_of_element_located((By.NAME, "endN"))
        )
        oMaxPrice.clear()
        oMaxPrice.send_keys("1000")
        log_v2("Цена 'до 1000' успешно введена", "info")
    except:
        log_v2("Ошибка при вводе цены 'до'", "error")
    
    input("Press Enter")