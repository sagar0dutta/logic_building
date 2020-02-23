
import pyshorteners as sh

link = 'https://www.youtube.com/ayushirawat/videos'

s = sh.Shortener()
x = (s.tinyurl.short(link))

print(x)

# One-liner
#print(pyshorteners.Shortener().tinyurl.short('https://www.youtube.com/ayushirawat/videos'))
