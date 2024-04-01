lang = pipen()
lang.instructions['HELLO'] = lambda *args: sys.stdout.write('Hello, ' + args[0])
