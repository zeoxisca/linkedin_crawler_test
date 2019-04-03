# linkedin_crawler_test
a test edition of crawling linkedin.[Just for learning :-)]

This project is for learning the Selenium lib of python^3.5. Written at 2018/11.

*Linkedin is a very strong website to defend autocrawling tools that I had failed to find ways to get large mount of data. Lastly, with banning by linkedin, I upended the project.*

Here is the intruduction of functions.

> re_captcha()
Get the capthca code and write by hand.

> login()
Simulate the login behavior like human.

> get_link()
Find all relative links about the key words from Google.

> get_search_link()
Design the search link for Google with using the words form users inpution.

> search()
Simulate the google-searching behavior.

> read_profile()
Refresh all the page and ready to save the profile page.

All crawled data would be stored in the *saved* file. And crawled ID would be stored in the *crawled.txt* file.
