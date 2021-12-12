# QuickInfo
 This is the library that you've all been searching for, it's built for developers and allows for a variety of web scraping tasks like accessing featured snippets, summaries and wikipedia articles of google webpages. It's built on the web scraping module, selenium.


## How to use

Using this module is very easy. Import it by saying - 
```
import quickinfo
```
to import the class directly - 
```
from quickinfo import QuickScrape
```
The first step is to create an instance of the class - 
```
p = quickinfo.QuickScrape()
# OR
p = QuickScrape()
```
QuickScrape takes a parameter and that is the path of your chromedriver.exe file, by default, the path set is "C:\Program Files (x86)\chromedriver.exe". Please change this attribute if your chromedriver file is in a different path.

The next step is to run the process method. It takes an attribute and that is headless. By default, headless is set to True. If set to boolean True, the process of opening the webpage will take place in the background. If set to boolean False, then you can see the process take place.

```
p.process() # Takes arguement True or False
```
Remember to run this process method before you use any webscraping functions.
This module has three basic methods, they are - 

```
wiki_article = p.wiki_article(query)
summary_para = p.summary_para(query)
featured_snippet = p.featured_snippet(query)

print(wiki_article)
print(summary_para)
print(featured_snippet)
```

Please note that sometimes a summary_para or a wiki_article or a featured_snippet may not be available, hence it will return None.
In the end of your program it is very important to say p.end(). This closes the driver and ends the instance.

```
p.end()
```

## Example code 
```
from quickinfo import QuickScrape
p = QuickScrape() # creates instance
p.process() # runs process in the background

query = "programming"

wiki_article = p.wiki_article(query) # gets wiki article for programming
summary_para = p.summary_para(query) # gets summary para for programming
featured_snippet = p.featured_snippet(query) # gets featured snippet for programming

print(wiki_article)
print(summary_para)
print(featured_snippet)

p.end()
```

#### Output
```
Description
Computer programming is the process of designing and building an executable computer program to accomplish a specific computing result or to perform a specific task. Wikipedia
Programming is the process of creating a set of instructions that tell a computer how to perform a task. Programming can be done using a variety of computer programming languages, such as JavaScript, Python, and C++.
Featured snippet from the web
Programming is the process of creating a set of instructions that tell a computer how to perform a task. Programming can be done using a variety of computer programming languages, such as JavaScript, Python, and C++.

What is Programming? (video) | Khan Academy
https://www.khanacademy.org › ... › Intro to programming
```
## Built by
#### DarkSkyProgrammers - 
The programmers of this team are Arya Prabhu and Ananthram Vijayaraj.


# Team logo




![alt text](quickinfo/darkskylogo.jpeg)
