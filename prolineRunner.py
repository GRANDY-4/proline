import sys
import interpreter.interpreter as i

if len(sys.argv) > 1:
    filename = sys.argv[1]
    i.run(filename)
