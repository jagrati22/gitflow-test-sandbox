# User Service & Metrics Processing

def calculate_user_discount(user_data):
    # Bug 1: No null/dict validation
    tier = user_data["tier"]
    spend = user_data["total_spend"]
    orders_count = user_data["orders_count"]
    
    # Bug 2: ZeroDivisionError risk if orders_count is 0
    average_order_value = spend / orders_count
    
    discount = 0.0
    if tier == "GOLD":
        discount = 0.20
    elif tier == "SILVER":
        discount = 0.10
        
    return {
        "user_id": user_data["id"],
        "discount_applied": discount,
        "aov": average_order_value
    }

def process_transaction(user_data):
    # Bug 3: Missing error boundary
    print("Processing user transaction...")
    result = calculate_user_discount(user_data)
    print("Transaction processed successfully!")
    return result
