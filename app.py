from helper.modules import read_csv, highest_price, average_price, amount_of_ideal_cuts, count_and_list_colors, median_carat_for_premium_cuts, average_carat_by_cut, average_price_by_color

# assigning values to variables using the modules we created to give store in them what the functions return.
data = read_csv('data.csv') # the function 'read_csv()' takes a filename as input and returns the data read from it 
max_price = highest_price(data)  
avg_price = average_price(data)
ideal_cuts = amount_of_ideal_cuts(data) 
color_count, colors = count_and_list_colors(data)
median_carat_premium = median_carat_for_premium_cuts(data)
avg_carat_by_cut = average_carat_by_cut(data)
avg_price_by_color = average_price_by_color(data)

    

if __name__=="__main__":
     print(f'The most expensive diamond costs {max_price}') # Answer 1 
     print(f'The average price of all diamonds is {avg_price}') # Answer 2 
     print(f'The number of cuts in Ideal condition is {ideal_cuts}') # Answer 3 
     print(f'The amount of different colors we have is {color_count} The type of colors we have are {colors}') # Answer 4 
     print(f'The median of carats for the premium cuts is {median_carat_premium}') # Answer 5 
     print(f'The average carat of a diamond by cut is {avg_carat_by_cut}') # Answer 6 
     print(f'The average price by color is {avg_price_by_color}') # Answer 7
    