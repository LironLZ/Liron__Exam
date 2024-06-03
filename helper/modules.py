import csv

def read_csv(filename):
    data = []  # Initializes an empty list called data to store the rows from the CSV file
    try:
        with open(filename, 'r') as csvfile:  # opens the CSV file in read mode and ensures it closes after reading
            reader = csv.DictReader(csvfile)  # creates a DictReader object to read the CSV file
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except Exception as e: # assigns a caught exception object to a variable named e
        print(f"Error: {e}")
        return None
    return data

def highest_price(data):
    max_price = 0
    for row in data:
        price = float(row['price'])
        if price > max_price:
            max_price = price
    return max_price

def average_price(data):
    total_price = 0
    try:
        for row in data:
            price = float(row['price'])
            total_price += price
        avg_price = total_price / len(data)
    except ZeroDivisionError:  # a specific type of exception that catches an attempt to divide a number by 0
        print("Error: Empty dataset.")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None
    return avg_price

def amount_of_ideal_cuts(data):
    total_ideal = 0  
    for row in data:
        if row['cut'] == 'Ideal':  
            total_ideal += 1  
    return total_ideal

def count_and_list_colors(data):
    colors = set()  # a set handles duplicates, so each color will be stored in the set once.
    for row in data:
        colors.add(row['color'])  
    return len(colors), list(colors)  

def median_carat_for_premium_cuts(data):
    premium_carats = []  
    for row in data:
        if row['cut'] == 'Premium':  
            premium_carats.append(float(row['carat'])) 
    premium_carats.sort()  
    n = len(premium_carats)
    if n % 2 == 0:
        median = (premium_carats[n // 2 - 1] + premium_carats[n // 2]) / 2  # Calculate median for even number of elements
    else:
        median = premium_carats[n // 2]  # Calculate median for odd number of elements
    return median

def average_carat_by_cut(data):
    cut_carats = {}  
    cut_counts = {}  
    for row in data:
        cut = row['cut']
        carat = float(row['carat'])
        if cut in cut_carats:
            cut_carats[cut] += carat  
            cut_counts[cut] += 1  
        else:
            cut_carats[cut] = carat  
            cut_counts[cut] = 1  
    averages = {cut: cut_carats[cut] / cut_counts[cut] for cut in cut_carats}  
    return averages

def average_price_by_color(data):
    color_prices = {}  
    color_counts = {}  
    for row in data:
        color = row['color']
        price = float(row['price'])
        if color in color_prices:
            color_prices[color] += price  
            color_counts[color] += 1  
        else:
            color_prices[color] = price  # Initialize total price for the color
            color_counts[color] = 1  # Initialize count of diamonds for the color
    averages = {color: color_prices[color] / color_counts[color] for color in color_prices}  
    return averages
