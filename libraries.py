import sys
import os
import datetime
import time
import html

print("sys.platform gives: ", sys.platform)
print("os.getcwd() gives: ", os.getcwd())
print("os.environ gives: ", os.environ)
print("os.getenv('Home') gives: ", os.getenv('Home'))
print("sys.version gives: ", sys.version)

print("datetime.date.today().year gives: ", datetime.date.today().year)
print("time.strftime("") gives: ", time.strftime("%A %p"))

print(html.escape("This HTML fragment contains a <script>script</script> tag"))
print(html.unescape("I &heats; Python's &lt;standard library&gt"))
