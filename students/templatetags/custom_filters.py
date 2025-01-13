from django import template

register = template.Library()

@register.filter
def add(value,arg) -> int:
    return value+arg

@register.filter
def Total(*args) -> int:
    total :int = 0
    for arg in args:
        total+=arg 
    return total 

@register.filter 
def Percentage(value:int,arg:int)->float:
    return round((value/arg),2)*100

