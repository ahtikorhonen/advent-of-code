if __name__ == '__main__':
    with open('day-1/input.txt') as f:
        #read input from textfile
        lines = f.readlines()

    #helper function for converting input to type list[int]
    def map_helper(num):
        if num == '\n':
            return -1
        else:
            return int(num)

    #map calories to int type
    calories = list(map(map_helper, lines))
    
    sub_list = []
    calories_mapped = []

    for num in calories:
        if num != -1:
            sub_list.append(num)
        else:
            calories_mapped.append(sub_list)
            sub_list = []
    
    sum_of_calories = [sum(calories) for calories in calories_mapped]
    # answer to puzzle 1
    max_calories = max(sum_of_calories)
    # answer to puzzle 2
    top_3_calories = sorted(sum_of_calories, reverse=True)[:3]
    sum_top_3_calories = sum(top_3_calories)