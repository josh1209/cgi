#!/usr/bin/env python
import cgi
import cgitb

cgitb.enable()

form = cgi.FieldStorage()
operands = form.getlist('operand')

try:
    total = sum(map(int, operands))
    body = f'Your total is: {total}'
except (ValueError, TypeError):
    body = 'Unable to calculate a sum: please provide integer operands.'

print("Content-type: text/plain")
print()
print(body)
