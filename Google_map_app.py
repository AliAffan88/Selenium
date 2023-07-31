import streamlit as st
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys


def searchplace(driver, place):
    search_box = driver.find_element(By.ID, 'searchboxinput')
    search_box.send_keys(place)
    search_box.send_keys(Keys.RETURN)


def directions(driver):
    sleep(10)
    directions_button = driver.find_element(By.XPATH, '/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[4]/div[1]/button/span/span')
    directions_button.click()


def find(driver, destination):
    sleep(6)
    search_box = driver.find_element(By.XPATH, '/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/div[1]/div/input')
    search_box.click()
    search_box.send_keys(destination)
    search_box.send_keys(Keys.RETURN)
    sleep(2)


def get_kilometers(driver):
    sleep(5)
    total_kilometers = driver.find_element(By.XPATH, '/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[4]/div[1]/div[1]/div/div[1]/div[2]/div')
    return total_kilometers.text


# Create a Streamlit application
def main():
    # Initialize the Selenium driver
    driver = webdriver.Firefox()
    driver.get('https://www.google.com/maps')
    sleep(3)

    # Get input from the user
    place = st.text_input("Enter the initial place:")
    destination = st.text_input("Enter the destination:")

    # Execute the Selenium code based on user input
    if place:
        searchplace(driver, place)

    if st.button("Get Distance"):
        directions(driver)

    if destination:
        find(driver, destination)
        st.write("Total Kilometers of Best Route:", get_kilometers(driver))

    # Cleanup after the execution
    driver.quit()


if __name__ == "__main__":
    main()
