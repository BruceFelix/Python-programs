#From credit_str = “1234-5678-9878-0434” get ‘0’

credit_str = "1234-5678-9878-0434"
 
new_str = credit_str.split("-")[-1][0]
 
print(new_str)
 