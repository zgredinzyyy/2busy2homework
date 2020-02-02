# 2busy2homework 🙊

**2busy2homework** is a tool that allows sending POST request to code.org for automatic exercises completion. 
Using selenium it's capable of sending Form Data with *random* generated values of attempts, completion time and lines of code.  

Installation
------------

###### Requires Python 3.6.X

**Clone repo:**

  `$ git clone https://github.com/zgredinzyyy/2busy2homework`
  
**Install requirements:**

  `$ pip install requirements.txt`
  
**Download chromedriver.exe for your version of chrome:**
 
 * [Chrome Version](https://www.whatismybrowser.com/detect/what-version-of-chrome-do-i-have)
 * [chromedriver.exe](https://chromedriver.chromium.org/)

Usage
-----

  1. Go to the course
  2. Enter any exercise
  3. Open developer console
  4. Enter **Network** tab
  5. Check **Preserve Log**
  6. Start execution of code (on code.org)
  7. Look for POST request as shown on the picture
  ![img](https://github.com/zgredinzyyy/2busy2homework/blob/master/img/help.png)
  * **ID** = First digits
  * **Before** = Second digits
  * **After** = Third digits
  8. Look for appName at the end of request
  ![app](https://github.com/zgredinzyyy/2busy2homework/blob/master/img/app.png)
  * **app_name** = app
  9. Type in value for how many excercises you need to do. (Type +/- 3 because sometimes links are little bit apart)
  10. Finally type in your login and password into variables with same name.
  11. Run in your shell:

  `$ python ./main.py`
  
  12. Let it run 😮
