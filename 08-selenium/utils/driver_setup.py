from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service
#from webdriver_manager.microsoft import EdgeChromiumDriverManager
import os

def get_driver():
    edge_options = Options()
    edge_options.add_argument("--start-maximized")

    #service = Service(EdgeChromiumDriverManager().install())
    #driver = webdriver.Edge(service=service, options=edge_options)
    os.environ["SE_DRIVER_MIRROR_URL"] = "https://msedgedriver.microsoft.com"
    driver = webdriver.Edge(options=edge_options)

    return driver


