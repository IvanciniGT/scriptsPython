# docker container create --name selenium -p 4444:4444 -p 7900:7900 --shm-size="2g" selenium/standalone-firefox:4.0.0-rc-1-prerelease-20210713
# docker start selenium
# pip3 install selenium
# Extensión chropath
from selenium import webdriver

navegador=webdriver.Remote(
    command_executor="http://localhost:4444/wd/hub",
    desired_capabilities={
        "browserName": "firefox"
    }
)

try:
    navegador.get("https://es.wikipedia.org")
    print(navegador.title)
    
    # Localizar un elemento de nuestra página                       y ejecutar una acción sobre él.
    navegador.find_element_by_xpath("//a[span[contains(text(),'Ayuda')]]")                        .click()
    print(navegador.title)
    navegador.find_element_by_xpath("//a[span[contains(text(),'Trabajando con otros')]]")         .click()
    navegador.find_element_by_xpath("//input[@id='searchInput']")                                 .send_keys("selenium")
    navegador.find_element_by_xpath("//input[@id='searchButton']")                                .click()
    print(navegador.title)

    contenido=navegador.find_element_by_xpath("//div[@id='mw-content-text']//p")                  .text
    print(contenido)    
    
finally:
    navegador.quit()
    