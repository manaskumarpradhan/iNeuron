def user_name_reverse():
    print("enter first name")
    first_name = input()
    print("enter last name")
    last_name = input()
    #reverse the entire string
    first_name_rev=''
    last_name_rev=''
    for i in range(len(first_name)-1,-1,-1):
        first_name_rev = first_name_rev+first_name[i]
    for i in range(len(last_name)-1,-1,-1):
        last_name_rev = last_name_rev+last_name[i]
    print(last_name_rev+' '+ first_name_rev)
    #if want to reverse only the first and last name not the whole string
    #print(last_name+' '+ first_name)

if __name__ == "__main__":
    user_name_reverse()