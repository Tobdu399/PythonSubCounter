from selenium import webdriver
import selenium
import time
import os

green = "\u001b[32m"
yellow = "\u001b[33;1m"
red = "\u001b[31m"
reset = "\u001b[0m"

def header():
    os.system("clear")
    print(yellow + "- Python Sub Counter -\n" + reset)

def main():
    loading = True

    try:
        header()
        print(green + "Loading... Please wait" + reset)

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")

        browser = webdriver.Chrome(os.getcwd() + "/chromedriver", options=chrome_options)

        # PewDiePie https://subscribercounter.com/channel/UC-lHJZR3Gqxm24_Vd_AJ5Yw
        # jacksepticeye https://subscribercounter.com/channel/UCYzPXprvl5Y-Sf0g4vX-m6g
        # Davie504 https://subscribercounter.com/channel/UCgFvT6pUq9HLOvKBYERzXSQ
        # More links here --> https://subscribercounter.com

        browser.get("https://subscribercounter.com/channel/UCgFvT6pUq9HLOvKBYERzXSQ") # <-- Paste your link here

        while True:
            loading = False

            header()
            print(green + "Channel: " + reset + browser.find_element_by_class_name("index__channelName--J7TfO").text)
            print(green + "Subscribers: " + reset + browser.find_element_by_class_name("index__lineAmountBottom--3zJDz").text)
            print(red + "\n======================\n" + reset)
            time.sleep(15)

    except(KeyboardInterrupt):
        if not loading:
            browser.quit()

        os.system("clear")    


main()