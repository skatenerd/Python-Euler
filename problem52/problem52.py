##fun stuff with MAP and FOLD;
##What is the first number,N, where [N,2N,...,6N] have digits which
##are permutations of one another


def are_perms(frst,sec):
    #takes two integers.
    #returns TRUE if the digits
    #in frst are a permutation of the digits in sec
    
    frst_dict=get_dict_from_num(frst)
    sec_dict=get_dict_from_num(sec)
    return frst_dict==sec_dict


def are_perms(numbers):
    #takes a list of integers.
    #returns TRUE if all of the integers'
    #digits are permutations of each other
    
    digits_dict_list=map(get_dict_from_num, numbers)
    master_dict=reduce(equals_for_fold,digits_dict_list)
    if(master_dict):
        return True
    else:
        return False

def equals_for_fold(a,b):
    #used as an argument to Fold
    #when checking if a list is full of equivalent thingss
    if a==b:
        return a
    else:
        return False



def get_dict_from_num(x):
    #takes an integer, and returns a dictionary describing
    #the digits contained in base 10 representation

    rtn_val={}
    while x>0:
        cur_num=x % 10
        if cur_num not in rtn_val.keys():
            rtn_val[cur_num]=0
        rtn_val[cur_num]+=1
        x/=10
    return rtn_val


found=False
i=1

while found==False:
    i+=1
    to_check=map(lambda x: x * i, xrange(1,7))
    #print to_check
    if are_perms(to_check):
        found=True
        print i
    
