"""17. Write a function that takes a list of numbers as input and returns a new list containing 
only the even numbers from the input list. Use list comprehension to solve this problem."""

def even_no(list_obj):
    try:
        even_no=[no for no in list_obj if no%2==0]
        return even_no
    except Exception as e:
        raise e
    





# for checking
if __name__=="__main__":
    print(even_no([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

