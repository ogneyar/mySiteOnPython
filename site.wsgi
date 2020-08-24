"""
Коментарии
вот
так
надо
использовать
"""

z = ""

x = "Hello!"
for char in x:
    z += char + "\n"

z += "\n"

x = 0
while x<=5:
    z += str(x) + "\n"
    x += 1

z += "\n"

for x in range(1, 6):
    z += str(x) + "\n"

z += "\n"

x = 15
if (x<10) or (x>20):
    z += "x is bad"
elif 10<x<20:
    z += "x is good!"
else:
    z += "x is werid"

z += "\n\nHellOfWorld!\n\n"

n = 0

def application(env, start_response):
    global n, z
    n += 1
    response = z + str("%.6d" % n)

    start_response('200 OK', [('Content-Type', 'text/plain')])
    return [bytes(response, 'utf-8')]


#def application(env, start_response):
#    start_response('200 OK', [('Content-Type','text/html')])
#    return [b'<br><br><br><center><h1>HellyWrd</h1></center>']