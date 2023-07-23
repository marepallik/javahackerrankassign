def cum_multiple(array):
    try:
        if not array or 0 in array:
            raise ValueError("Array should not be empty and should not contain 0.")
        
        cum_multiple = 1
        result_array = []
        
        for num in array:
            cum_multiple *= num
            result_array.append(cum_multiple)
            
        return result_array
    
    except ValueError as e:
        print("Error:", e)
        return None

if __name__ == "__main__":
    arrNum = [5, 3, 4, 2, 0, 8]
    result = cum_multiple(arrNum)

    if result:
        print("Output: arrNum =", result)
