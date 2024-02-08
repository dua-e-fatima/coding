# Initialize shopping list variables
items = ["Apple", "Banana", "Milk"]
quantities = [2, 3, 1]
prices = [1.5, 0.75, 2.0]

# Calculate total cost
total_cost = sum([quantities[i] * prices[i] for i in range(len(items))])

# Set budget
budget = 10.0

# Check if there's enough budget
if total_cost <= budget:
    print("You have enough budget for your shopping!")
else:
    print("Oops! You exceeded your budget. Remove some items or increase your budget.")
    
   # Define variables for task names and durations
task1_name = "Coding"
task1_duration = 2.5  # in hours

task2_name = "Meetings"
task2_duration = 1.5  # in hours

task3_name = "Exercise"
task3_duration = 1.0  # in hours

# Calculate total time spent on each task
total_task1_time = task1_duration
total_task2_time = task2_duration
total_task3_time = task3_duration

# Print total time spent on each task
print(f"Total time spent on {task1_name}: {total_task1_time} hours")
print(f"Total time spent on {task2_name}: {total_task2_time} hours")
print(f"Total time spent on {task3_name}: {total_task3_time} hours")

# Identify areas for improvement
max_time_task = max(total_task1_time, total_task2_time, total_task3_time)
min_time_task = min(total_task1_time, total_task2_time, total_task3_time)

if max_time_task - min_time_task >= 2.0:
    print("There is a significant difference in time spent on tasks. Consider balancing your workload.")
else:
    print("Your time distribution is relatively balanced. Good job!") 
    
    # Movie information
movie_title = "Inception"
movie_genre = "Sci-Fi"
movie_rating = 8.8
movie_release_year = 2010

# User preferences
user_genre = "Sci-Fi"
user_rating = 8.0
user_release_year = 2010

# Recommend movie based on preferences
if (
    movie_genre == user_genre
    and movie_rating >= user_rating
    and movie_release_year >= user_release_year
):
    print(f"Recommended movie: {movie_title}")
else:
    print("No matching movies found.")
    
    # Recipe Ingredients and Quantities for 4 servings
original_servings = 4

ingredient1_name = "Flour"
ingredient1_quantity = 1  # cups

ingredient2_name = "Salt"
ingredient2_quantity = 0.5  # teaspoons

ingredient3_name = "Water"
ingredient3_quantity = 2  # cups

# Number of Servings Input
desired_servings = int(input("Enter the number of servings: "))

# Calculate Adjustment Factor
adjustment_factor = desired_servings / original_servings

# Calculate Adjusted Ingredient Quantities
adjusted_ingredient1_quantity = ingredient1_quantity * adjustment_factor
adjusted_ingredient2_quantity = ingredient2_quantity * adjustment_factor
adjusted_ingredient3_quantity = ingredient3_quantity * adjustment_factor

# Display Original and Adjusted Quantities
print(f"Original quantities for {original_servings} servings:")
print(f"{ingredient1_name}: {ingredient1_quantity} cups")
print(f"{ingredient2_name}: {ingredient2_quantity} teaspoons")
print(f"{ingredient3_name}: {ingredient3_quantity} cups")

print("\nAdjusted quantities:")
print(f"For {desired_servings} servings:")
print(f"{ingredient1_name}: {adjusted_ingredient1_quantity:.2f} cups")
print(f"{ingredient2_name}: {adjusted_ingredient2_quantity:.2f} teaspoons")
print(f"{ingredient3_name}: {adjusted_ingredient3_quantity:.2f} cups")

