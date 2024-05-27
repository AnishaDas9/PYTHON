#function defination 
# def calc_sum(a,b):
#     sum = a+b
#     print(sum)
#     return sum

#     calc_sum(5,2)


# def print_hello():
#     print("hello")

#     print_hello()
#     print_hello()
#     print_hello()
#     print_hello()


#avg of 3 numbers

# def calc_avg(a,b,c):
#     sum = a+b+c
#     avg = sum / 3
#     print(avg)
#     return avg

#     calc_avg(2,3,4)

#practice question******************************


cities = ["delhi","gurgaon" , "noida" , "pune" , "chennai" , "blr"]
def print_len(list):
    print(len(list))
    print_len(cities)


    def print_list(list):
        for item in list:
            print(item, end=" ")

            print_list(cities)
            print()


