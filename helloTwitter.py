from splinter.browser import Browser

print "hello twitter"
handle = raw_input('twitter handle:')
#pw = raw_input('password:')

browser = Browser('firefox')
browser.visit('https://twitter.com/')



loginbutton = browser.find_by_text('Log In')
loginbutton.first.click()
#works up till here


usernamebox = browser.find_by_id('signin-email')
#passwordbox = browser.find_by_id('signin-password')
if len(usernamebox)==0:
    print "no username boxes found =^["
browser.fill(usernamebox.first, handle)
#browser.fill(passwordbox.first, pw)
