#Solution was given athttps://www.justlearnpython.com/docs/exercises/string-exercises/
#But didn't work on my computer
#From credit_str = “xxxx—-xxxx-8888——xxxx” get ‘8888’

credit_str = "xxxx----xxxx-8888 ----xxxx"
new_credit_str = credit_str[credit_str.index('8'):credit_str.index('8') + len('8888')]
 
print(new_credit_str)
 