# Module 8 Assignment: Data Lookup with Dictionaries & Basic Aggregation
# GlobalTech Solutions Customer Management System

# Welcome message
print("=" * 60)
print("GLOBALTECH SOLUTIONS - CUSTOMER MANAGEMENT SYSTEM")
print("=" * 60)

# TODO 1: Create a dictionary of service categories and hourly rates
# Store in variable: services
# Example: services = {"Web Development": 150, "Data Analysis": 175, ...}
# Include at least 5 different services
services = {
    "Web Development": 150,
    "Data Analysis": 175,
    "Healthcare": 210,
    "Education": 200,
    "Accounting": 100,
    }

# TODO 2: Create customer dictionaries
# Each customer should have: company_name, contact_person, email, phone
# Create at least 4 customer dictionaries
# Example: customer1 = {"company_name": "ABC Corp", "contact_person": "John Smith", ...}
customer1 = {
    "company_name": "ABC Corp",
    "contact_person": "John Smith",
    "email": "john@abccorp.com",
    "phone": "067-4167"
    }
customer2 = {
    "company_name": "XYZ INC",
    "contact_person": "Fernando Mendoza",
    "email": "fmendoza@xyz.com",
    "phone": "041-6741"
    }
customer3 = {
    "company_name": "Capsule Corp",
    "contact_person": "Chris Bacon",
    "email": "cbacon@ccorp.com",
    "phone": "123-4567"
    }
customer4 = {
    "company_name": "Based Systems",
    "contact_person": "Cooper Lafave",
    "email": "clafave@basedsystems.com",
    "phone": "765-4321"
    }

# TODO 3: Create a master customers dictionary
# Store in variable: customers
# Use customer IDs as keys and customer dictionaries as values
# Example: customers = {"C001": customer1, "C002": customer2, ...}
customers = {
    "C001": customer1,
    "C002": customer2,
    "C003": customer3,
    "C004": customer4
    }
# TODO 4: Display all customers
print("\nAll Customers:")
print("-" * 60)
# Add your code here to display all customer information
for cid, info in customers.items():
    print(cid, info)
# TODO 5: Look up specific customers
# Use dictionary access to:
# - Get and display customer C002's information (store in c002_info)
# - Get and display customer C003's contact person (store in c003_contact)
# - Try to get customer C999 (doesn't exist) using .get() with a default message (store in c999_info)
c002_info = customers["C002"]
c003_contact = customers["C003"]["contact_person"]
c999_info = customers.get("C999", "Customer not found")

print("\n\nCustomer Lookups:")
print("-" * 60)
# Add your code here
print("C002:", c002_info)
print("C003 Contact:", c003_contact)
print("C999:", c999_info)
# TODO 6: Update customer information
# - Change customer C001's phone number
# - Add a new field "industry" to customer C002
# - Display the updated customer information
customers["C001"]["phone"] = "067-1234"
customers["C002"]["industry"] = "Technology"

print("\n\nUpdating Customer Information:")
print("-" * 60)
# Add your code here
print("Updated C001:", customers["C001"])
print("Updated C002:", customers["C002"])
# TODO 7: Create project dictionaries for each customer
# Each project: {"name": "Project Name", "service": "Service Type", "hours": X, "budget": Y}
# Create a projects dictionary where customer IDs map to lists of projects
# Store in variable: projects
# Example: projects = {"C001": [project1, project2], "C002": [project3], ...}
projects = {
    "C001": [
        {"name": "Website Design", "service": "Web Development", "hours": 150, "budget": 18000},
        {"name": "Data Review", "service": "Data Analysis", "hours": 60, "budget": 10500}
    ],
    "C002": [
        {"name": "Hospital", "service": "Healthcare", "hours": 210, "budget": 18900}
    ],
    "C003": [
        {"name": "Learning Platform", "service": "Education", "hours": 200, "budget": 22000}
    ],
    "C004": [
        {"name": "Financial Tool", "service": "Accounting", "hours": 100, "budget": 7000}
        ]
    }
    
print("\n\nProject Information:")
print("-" * 60)
# Add your code here
for cid, plist in projects.items():
    print(cid, plist)
# TODO 8: Calculate project costs
# For each project, calculate: cost = hourly_rate * hours
# Display each project with its calculated cost

print("\n\nProject Cost Calculations:")
print("-" * 60)
# Add your code here
for cid, plist in projects.items():
    for p in plist:
        rate = services[p["service"]]
        cost = rate * p["hours"]
        print(p["name"], "- Cost:", cost)
# TODO 9: Customer statistics using dictionary methods
# Display:
# - All customer IDs using .keys()
# - All customer companies using .values() and extracting company names
# - Count of total customers using len()
print("\n\nCustomer Statistics:")
print("-" * 60)
# Add your code here
print("Customer IDs:", customers.keys())
companies = [c["company_name"] for c in customers.values()]
print("Customer Companies:", companies)
print("Total Customers:", len(customers))
# TODO 10: Service usage analysis
# Create a dictionary that counts how many projects use each service
# Store in variable: service_counts
# Display the service usage counts
service_counts = {}
for plist in projects.values():
    for p in plist:
        service = p["service"]
        service_counts[service] = service_counts.get(service, 0) + 1

print("\n\nService Usage Analysis:")
print("-" * 60)
# Add your code here
print(service_counts)
# TODO 11: Financial aggregations
# Calculate and display:
# - Total hours across all projects (store in total_hours)
# - Total budget across all projects (store in total_budget)
# - Average project budget (store in avg_budget)
# - Most expensive and least expensive projects (store in max_budget, min_budget)
hours_list = []
budget_list = []

for plist in projects.values():
    for p in plist:
        hours_list.append(p["hours"])
        budget_list.append(p["budget"])
        
total_hours = sum(hours_list)
total_budget = sum(budget_list)
avg_budget = total_budget / len(budget_list)
max_budget = max(budget_list)
min_budget = min(budget_list)

print("\n\nFinancial Summary:")
print("-" * 60)
# Add your code here
print("Total Hours:", total_hours)
print("Total Budget:", total_budget)
print("Average Budget:", avg_budget)
print("Max Budget:", max_budget)
print("Min Budget:", min_budget)

# TODO 12: Customer summary report
# For each customer, show:
# - Customer details
# - Number of projects
# - Total hours
# - Total budget
print("\n\nCustomer Summary Report:")
print("-" * 60)
for cid, customer in customers.items():

    plist = projects.get(cid, [])

    total_h = sum(p["hours"] for p in plist)
    total_b = sum(p["budget"] for p in plist)
    print(cid, customer["company_name"])
    print("Projects:", len(plist))
    print("Total Hours:", total_h)
    print("Total Budget:", total_b)
    print()

# TODO 13: Create rate adjustments using dictionary comprehension
# Create a new dictionary with all service rates increased by 10%
# Store in variable: adjusted_rates
# Use dictionary comprehension: adjusted_rates = {service: rate * 1.1 for service, rate in services.items()}
adjusted_rates = {service: rate * 1.1 for service, rate in services.items()}
print("\n\nAdjusted Service Rates (10% increase):")
print("-" * 60)
# Add your code here
print(adjusted_rates)
# TODO 14: Filter customers using dictionary comprehension
# Create a dictionary of only customers who have projects
# Store in variable: active_customers
# Hint: Use the projects dictionary to check which customers have projects
active_customers = {cid: cust for cid, cust in customers.items() if cid in projects}
print("\n\nActive Customers (with projects):")
print("-" * 60)
# Add your code here
print(active_customers)
# TODO 15: Create project summaries using dictionary comprehension
# Create a dictionary mapping customer IDs to their total project budgets
# Store in variable: customer_budgets
# Example result: {"C001": 25000, "C002": 15000, ...}
customer_budgets = {cid: sum(p["budget"] for p in plist) for cid, plist in projects.items()}
print("\n\nCustomer Budget Totals:")
print("-" * 60)
# Add your code here
print(customer_budgets)
# TODO 16: Service pricing tiers using dictionary comprehension
# Create a dictionary categorizing services as "Premium" (>= 200), "Standard" (100-199), or "Basic" (< 100)
# Store in variable: service_tiers
# Use conditional expressions in the comprehension
service_tiers = {
    service: "Premium" if rate >= 200 else "Standard" if rate >= 100 else "Basic"
    for service, rate in services.items()
    }
print("\n\nService Pricing Tiers:")
print("-" * 60)
# Add your code here
print(service_tiers)
# TODO 17: Customer validation function
# Create a function validate_customer(customer_dict) that:
# - Checks if all required fields are present (company_name, contact_person, email, phone)
# - Returns True if valid, False otherwise
# - Use conditional logic to verify each field
# Test it on all customers and report results
def validate_customer(customer_dict):

    required = ["company_name", "contact_person", "email", "phone"]

    for field in required:
        if field not in customer_dict:
            return False

    return True

print("\n\nCustomer Validation:")
print("-" * 60)
# Add your code here
for cid, cust in customers.items():
    print(cid, validate_customer(cust))

# TODO 18: Project status tracking with loops and conditionals
# Add a "status" field to each project ("active", "completed", "pending")
# Use a loop to count projects by status
# Store counts in status_counts dictionary
# Display a summary of project statuses
status_counts = {"active": 0, "completed": 0, "pending": 0}

for plist in projects.values():
    for p in plist:

        p["status"] = "active"

        status_counts[p["status"]] += 1
print("\n\nProject Status Summary:")
print("-" * 60)
# Add your code here
print(status_counts)
# TODO 19: Budget analysis function with aggregation
# Create a function analyze_customer_budgets(projects_dict) that:
# - Takes the projects dictionary as input
# - Uses loops to calculate total and average budget per customer
# - Returns a dictionary with customer IDs as keys and budget stats as values
# - Each value should be a dict with 'total', 'average', and 'count' keys
def analyze_customer_budgets(projects_dict):

    results = {}

    for cid, plist in projects_dict.items():

        budgets = [p["budget"] for p in plist]

        total = sum(budgets)
        count = len(budgets)
        average = total / count if count > 0 else 0

        results[cid] = {
            "total": total,
            "average": average,
            "count": count
        }

    return results
print("\n\nDetailed Budget Analysis:")
print("-" * 60)
# Add your code here
budget_analysis = analyze_customer_budgets(projects)

print(budget_analysis)
# TODO 20: Service recommendation system
# Create a function recommend_services(customer_id, customers, projects, services) that:
# - Analyzes the customer's past projects
# - Identifies services they haven't used yet
# - Returns a list of recommended services based on their budget range
# - Use loops, conditionals, and dictionary operations
def recommend_services(customer_id, customers, projects, services):

    used_services = set()

    for p in projects.get(customer_id, []):
        used_services.add(p["service"])

    recommendations = []

    for service in services:
        if service not in used_services:
            recommendations.append(service)

    return recommendations
print("\n\nService Recommendations:")
print("-" * 60)
# Add your code here
for cid in customers:
    rec = recommend_services(cid, customers, projects, services)
    print(cid, "recommended:", rec)