# Web-Scrapping-Module
This is Web Scrapping Module, which offers many more NLP features<br>
This module offers:-<br>
<b>1.</b> Web Scrapping:- Offered by function called <b>"load_url"</b>, which takes only one argument, the link, also handles "link-broken", "link-not-found" cases<br><br>
<b>2.</b> Saving File:- Save the scrapped data into .txt file by using function <b>"save_it"</b>. Takes three arguments:- text to be stored, filename as which to be stored, address where to store(default is current directory). Also handles cases like "Address not found"<br>
<br><b>3.</b> Loading File:- <b>"load_file"</b> function is used for this. Does basic loading file job, if addresses to a .txt file and a valid path. Else print error message<br><br>
<b>4.</b>Check For words:- <b>check_for_words_before_link</b> checks for words before loading URL. Takes two arguments link to be scrapped and words which should not be in the link <b>check_for_words_after_link</b> checks for words after scraping. Takes two arguments, text that has been scrapped and words that should not be in text
<br><br>
<b>5.</b>Preprocess:- <b>preprocess</b> does all the basic preprocessing required in NLP and returns a list of all the words.<br><br>
<b>6.</b>wordcloud:- <b>cloud_it</b> makes the word cloud of text or list
<br><br>
<b>7.</b>keyword_extraction:-<b>extract_it</b> It extracts the keyword in text or list.<br>
<br><b>8.</b>Named Entity Recognition:-<b>named_entity_recog</b> is the name of function takes one argument, the text, and give the result<br><br>
<b>9.</b>Topic Modelling:-<b>topic_model</b> is the name of function, takes two arguments, the text and the number of topics you want to be displayed on the screen
<br><br><br>
Function Names are:-<br><br><br>load_file<br>save_it<br>load_url<br>check-for_words_before_link<br>check_for_words_after_link<br>preprocess<br>cloud_it<br>extract_it<br>topic_model<br>named_entity_recog

