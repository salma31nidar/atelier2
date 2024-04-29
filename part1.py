import re

def clean_text(text):
    # Define stop words to remove
    stop_words = ["bought", "I", "for", "and", "with", "a", "of", "each", "dollar"]

    # Remove stop words
    cleaned_text = re.sub(r'\b(?:{})\b'.format('|'.join(stop_words)), '', text, flags=re.IGNORECASE)

    # Remove extra whitespaces
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()

    return cleaned_text

def generate_bill(text):
    # Clean the text
    cleaned_text = clean_text(text)

    # Define regex patterns
    price_pattern = r'(\d+(?:,\d+)?)'  # Pattern to match unit price
    quantity_pattern = r'\b(?:one|two|three|four|five|six|seven|eight|nine|ten)\b'  # Pattern to match quantity words
    item_pattern = r'([\w\s]+\w)'  # Pattern to match item names with spaces

    # Find all matches of item names, quantities, and prices
    items = re.findall(item_pattern, cleaned_text)
    quantities = re.findall(quantity_pattern, cleaned_text)
    prices = re.findall(price_pattern, cleaned_text)

    print(quantities)
    print(prices)
    print(items)
    
    # Convert quantity strings to numeric values
    quantity_dict = {
        'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
        'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10
    }
    quantities_numeric = []
    for q in quantities:
        if q.isdigit():
            quantities_numeric.append(int(q))
        else:
            quantities_numeric.append(quantity_dict.get(q))

    # Prepare the bill table
    bill_table = "Product Quantity Unit Price Total Price\n"
    for item, quantity, price in zip(items, quantities_numeric, prices):
        # Replace comma with dot in price
        price = price.replace(',', '.')
        total_price = float(price) * quantity
        # Remove quantity and price from the item name
        item = re.sub(quantity_pattern, '', item).strip()
        item = re.sub(price_pattern, '', item).strip()
        bill_table += f"{item} {quantity} {price} {total_price}\n"

    return bill_table

# Example usage
user_text = "I bought three Samsung smartphones 150 $ each, four kilos of fresh banana for 1,2 dollar a kilogram and one Hamburger with 4,5 dollar"
generated_bill = generate_bill(user_text)
print("Generated Bill:\n", generated_bill)
