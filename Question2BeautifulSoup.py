#-------------------------------------------------------------------------
# AUTHOR: Tim Hsieh
# FILENAME: Question5BeautifulSoup.py
# SPECIFICATION: Uses beautiful soup to grab specific elements of an HTML file.
# FOR: CS 4250- Assignment #3
# TIME SPENT: 5 hours
#-----------------------------------------------------------*/

from bs4 import BeautifulSoup

html_content = '''
<html>
<head>
<title>My first web page</title>
</head>
<body>
<h1>My first web page</h1>
<h2>What this is tutorial</h2>
<p>A simple page put together using HTML. <em>I said a simple page.</em>.</p>
<ul>
<li>To learn HTML</li>
<li>
To show off
<ol>
<li>To my boss</li>
<li>To my friends</li>
<li>To my cat</li>
<li>To the little talking duck in my brain</li>
</ol>
</li>
<li>Because I have fallen in love with my computer and want to give her some HTML loving.</li>
</ul>
<h2>Where to find the tutorial</h2>
<p><a href="http://www.aaa.com"><img src=http://www.aaa.com/badge1.gif></a></p>
<h3>Some random table</h3>
<table>
<tr class="tutorial1">
<td>Row 1, cell 1</td>
<td>Row 1, cell 2<img src=http://www.bbb.com/badge2.gif></td>
<td>Row 1, cell 3</td>
</tr>
<tr class="tutorial2">
<td>Row 2, cell 1</td>
<td>Row 2, cell 2</td>
<td>Row 2, cell 3<img src=http://www.ccc.com/badge3.gif></td>
</tr>
</table>
</body>
</html>
'''

# parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# the title of the HTML page
title = soup.find('title').get_text()
print("a) " + title + "\n")

# the second li element below "To show off"
second_li = soup.select('ul > li')[1].find('ol').find_all('li')[1].get_text()
print("b) " + second_li + "\n")

# all of the cells of Row 2
row_2_cells = soup.find_all(class_='tutorial2')[0].find_all('td')
row_2_data = [cell.get_text() for cell in row_2_cells]
print("c) ")
print(row_2_data)
print("\n")

# all h2 headings that include the word "tutorial"
tutorial_h2_headings = soup.find_all('h2', string=lambda string: string and 'tutorial' in string.lower())
for heading in tutorial_h2_headings:
    print("d) " + heading.get_text())
print("\n")

# all text that inclues the word "HTML"
html_text = soup.find_all(string=lambda text: 'HTML' in text)
for text in html_text:
    print("e) " + text)
    print("\n")

# all cells' data from the first row of the table
first_row_cells = soup.find('table').find('tr').find_all('td')
first_row_data = [cell.get_text() for cell in first_row_cells]
print("f) ")
print(first_row_data)
print("\n")

# all images from the table
table_images = soup.find('table').find_all('img')
for img in table_images:
    print("g) " + img['src'])
print("\n")
