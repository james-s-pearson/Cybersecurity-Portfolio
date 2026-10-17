"""Formatting test: this file is deliberately messy but runs fine.

Format it with <leader>cf (Black). Nothing should change in what it prints.
"""
import sys,os
def add( a,b ):
    return a+b
numbers = [1,2,  3,4]
total=add( numbers[0],numbers[ -1 ] )
config = {  'name':'format_me',"version":1 }
print( 'Total:',total )
print("Config:",config)
