from selenium import webdriver

# Set up the webdriver
driver = webdriver.Chrome()

# Navigate to the website
driver.get("https://www.example.com")

title = driver.title

# Close the webdriver
driver.quit()

# Save the title to a file
with open('webpage_title.txt', 'w') as file:
    file.write(title)
