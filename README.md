# Mission-to-Mars

![](/Images/mars.png)

___
***Everything that is further from us is becoming more interesting for us!***
___

This time we raise our heads up, since our task is to create a web application on the research of Mars. We must collect the necessary information from different Internet sources and with the help of the Splinter and Beautifulsoup program we will scrape and save it in the Mongodb database created. When all the data is ready, we will create a html page to show its audience, and so that the view is more presentable, we use the Bootstrap module.
### Resourses
___
+ Software
   - [X] MongoDB 
   - [X] Splinter 
   - [X] BeautifulSoup 
   - [X] Flask-PyMongo
+ Web pages screped:
  + https://marshemispheres.com  
  + https://spaceimages-mars.com
  + https://redplanetscience.com

### Summary
___

The final product was a fully-functional web application creted with Flask that included images, a table with information about Mars in comparison to Earth, and the latest article title and short description scraped from the NASA's webpage. Each time we click on the "Scrape New Data" button new information will be updated on both the website and the MongoDB. Our application is also completely compatible with any mobile device and tablets.
![](/Images/Picture3.png)

***Viewing from IPhone12Pro***

![](/Images/Picture4.png)

***Two Versions of images in app***
#### **Version 1**
![](/Images/Picture1.png%20.png)

#### **Version 2**
![](/Images/Picture2.png)

## Code
___
To see the code:
 + [App script: app.py](./app.py)
 + [Scraping script: scraping.py](./scraping.py) 
 + [HTML code: index.html](./templates/index.html)
___

***Cosmos is beautiful if only because there are no people there.***

![](/Images/Mars,_Earth_size_comparison.png)

``` 
Denis Antonov August 19, 2022
```



