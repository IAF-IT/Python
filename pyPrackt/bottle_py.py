from bottle import route, run, static_file


@route('/')
def home():
    return static_file('index.html', root='.')
 #   return "It is my home page"

@route('/echo/<thing>')
def echo(thing):
   return "Say hello to my little friend: %s!" % thing
run(host='localhost', port=9999)

