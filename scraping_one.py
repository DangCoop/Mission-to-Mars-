def mars_news(browser):

# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import datetime as dt

def scrape_all():
    #Initiate haedless driver for deployment
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)

    news_title, news_paragraph = mars_news(browser)

    #Run all scraping functions and store results in a dictionary
    data = {
        "news_title": news_title,
        "news_paragraph": news_paragraph,
        "featured_image": featured_image(browser),
        "facts": mars_facts(),
        "last_modified": dt.datetime.now()
    }

    #Stop webdriver and return data
    browser.quit()
    return data

def mars_news(browser):

    # Visit the mars nasa news site
    url = 'https://redplanetscience.com'
    browser.visit(url)

    # Optional delay for loading the page
    browser.is_element_present_by_css('div.list_text', wait_time=1)

    #Convert the browser HTML to a soup object and then quit the browser 
    html = browser.html
    news_soup = soup(html, 'html.parser')

    #Add try/exept for error handling
    try:

        slide_elem = news_soup.select_one('div.list_text')
        # Use the parent element to find the first `a` tag and save it as `news_title`
        news_title = slide_elem.find('div', class_='content_title').get_text()  
        # Use the parent element to find the paragraph text
        news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
        
    except AttributeError:
        return None, None    

    return news_title, news_p

# ### JPL Space Images Featured Image

def featured_image(browser):

    # Visit URL
    url = 'https://spaceimages-mars.com'
    browser.visit(url)

    # Find and click the full image button
    full_image_elem = browser.find_by_tag('button')[1]
    full_image_elem.click()

    # Parse the resulting html with soup
    html = browser.html
    img_soup = soup(html, 'html.parser')
    
    #Add try/exept for error handling
    try:

        # Find the relative image url
        img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
    
    except AttributeError:
        return None

    # Use the base URL to create an absolute URL
    img_url = f'https://spaceimages-mars.com/{img_url_rel}'
    

    return img_url


def mars_facts():

    try:

        #Create a new DataFrame from the HTML table. 
        #Function "read.html" - specifically searches for and returns a list of tables found in the HTML
        #By specifying index of [0] we're telling Pandas to pull only the first table it encounters, 
        #or the first item in the list. Then, it turns the table into a DataFrame
        df = pd.read_html('https://galaxyfacts-mars.com')[0] 
    except BaseException:
        return None    

    #Assign columns to the new DataFrame for additional clarity
    df.columns=['description', 'Mars', 'Earth']
    #By using the ".set_index()" function, we're turning the Description column into the DataFrame's index
    #"inplace=True" means that the updated index will remain in place, wiyhout having to reassign the DataFrame to a new variable
    df.set_index('description', inplace=True)
    
    #Convert our DataFrame back into HTML-ready code using the .to_html() function
    return df.to_html(classes="table table-striped")

# #Turning off a light switch. Stop webdriver and return data
# browser.quit()
# return data

if __name__ == '__main__':
    # If running as script, ptint csraped data
    print(scrape_all())






