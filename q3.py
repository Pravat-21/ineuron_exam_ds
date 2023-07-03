"""19. Write a function called ‘calculate_mean’ that takes a list of numbers as input and returns 
the mean (average) of the numbers. The function should calculate the mean using the sum of the numbers 
divided by the total count."""

def calculate_mean(num_list):
    try:
        total_sum=sum(num_list)
        total_count=len(num_list)
        calculated_mean=total_sum/total_count
        return calculated_mean
    except Exception as e:
        raise e
    

if __name__=="__main__":
    output_mean=calculate_mean([10, 15, 20, 25, 30])
    print(output_mean)

