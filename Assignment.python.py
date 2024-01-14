def calculate_ticket_price(age, day, num_tickets):
    base_price = 10  # Base ticket price

    # Age-based discounts
    if age == "adult":
        discount = 0  # No discount for adults
    elif age == "child":
        discount = 2  # $2 discount for children
    elif age == "senior":
        discount = 1  # $1 discount for seniors

    # Day-based discounts
    if day.lower() in ["saturday", "sunday"]:
        discount += 3  # $3 weekend discount

    # Group discount for more than 5 tickets
    if num_tickets >= 5:
        discount += 4  # $4 group discount

    # Final ticket price after applying discounts
    final_price = max(base_price - discount, 0)
    
    return final_price

# Example usage:
num_tickets = 6
ticket_price = calculate_ticket_price("adult", "Monday", num_tickets)
print(f"The total ticket price for {num_tickets} adults on Monday is ${ticket_price}")

def calculate_total_bill(items, quantities, prices, discount_percentage=0, tax_percentage=0, split_bill=False, num_people=1):
    if len(items) != len(quantities) or len(quantities) != len(prices):
        return "Error: Please provide valid inputs for items, quantities, and prices."

    total_amount = 0

    # Calculate total amount for each item
    for quantity, price in zip(quantities, prices):
        total_amount += quantity * price

    # Apply discount
    discount_amount = total_amount * (discount_percentage / 100)
    total_amount -= discount_amount

    # Apply tax
    tax_amount = total_amount * (tax_percentage / 100)
    total_amount += tax_amount

    # Split the bill among friends
    if split_bill and num_people > 0:
        total_amount /= num_people

    return total_amount

# Example usage:
items = ["Item1", "Item2", "Item3"]
quantities = [2, 1, 3]
prices = [5.99, 10.50, 8.75]
discount_percentage = 10
tax_percentage = 8
split_bill = True
num_people = 3

total_bill_amount = calculate_total_bill(items, quantities, prices, discount_percentage, tax_percentage, split_bill, num_people)
print(f"The total bill amount is: ${total_bill_amount:.2f}")

def analyze_social_media_post(post_text):
    # Sentiment Analysis
    positive_words = ["happy", "excited", "love", "awesome"]
    negative_words = ["sad", "disappointed", "hate", "awful"]

    sentiment_score = sum(post_text.lower().count(word) for word in positive_words) - sum(
        post_text.lower().count(word) for word in negative_words)

    if sentiment_score > 0:
        sentiment = "Positive"
    elif sentiment_score < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    # Keyword Analysis
    words = [word.strip('.,?!') for word in post_text.lower().split()]
    keywords = [word for word in set(words) if len(word) > 3]

    # Emoji Analysis
    emojis = [char for char in post_text if char in "ðððð¢ð ð¡"]

    # Potential Trends (using hashtags as an example)
    hashtags = [word[1:] for word in words if word.startswith("#")]

    analysis_result = {
        "sentiment": sentiment,
        "keywords": keywords,
        "emojis": emojis,
        "hashtags": hashtags
    }

    return analysis_result

# Example usage:
social_media_post = "Excited to try out the new #tech gadgets! ð They are amazing! #innovation"
result = analyze_social_media_post(social_media_post)
print(result)

def estimate_travel_cost(destination, travel_style, duration):
    # Base cost for transportation, accommodation, and activities
    base_transportation_cost = 500  # Placeholder values, replace with actual costs
    base_accommodation_cost = 1000
    base_activities_cost = 300
    
    # Adjustment factors for travel style
    if travel_style == 'budget':
        style_multiplier = 0.8
    elif travel_style == 'luxury':
        style_multiplier = 1.2
    else:
        raise ValueError("Invalid travel style. Choose 'budget' or 'luxury'.")

    # Calculate total cost
    total_cost = (base_transportation_cost + base_accommodation_cost + base_activities_cost) * style_multiplier * duration

    return total_cost

# Example usage:
destination = "Paris"
travel_style = "luxury"
duration = 7
estimated_cost = estimate_travel_cost(destination, travel_style, duration)
print(f"The estimated travel cost for {duration} days in {destination} with a {travel_style} style is ${estimated_cost:.2f}")