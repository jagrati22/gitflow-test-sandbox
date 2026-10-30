# User Service & Metrics Processing

def validate_user_data(user_data):
    '''
    Validate user_data dictionary for required fields and non-null values.
    Raises ValueError if validation fails.
    '''
    if not isinstance(user_data, dict):
        raise ValueError(\"user_data must be a dictionary\")
    required_fields = [\"id\", \"tier\", \"total_spend\", \"orders_count\"]
    for field in required_fields:
        if field not in user_data:
            raise ValueError(\"Missing required field: \" + field)
        if user_data[field] is None:
            raise ValueError(\"Field '{}' cannot be None\".format(field))
    if not isinstance(user_data[\"tier\"], str):
        raise ValueError(\"Field 'tier' must be a string\")
    if not isinstance(user_data[\"total_spend\"], (int, float)):
        raise ValueError(\"Field 'total_spend' must be a number\")
    if not isinstance(user_data[\"orders_count\"], (int, float)):
        raise ValueError(\"Field 'orders_count' must be a number\")
    if user_data[\"orders_count\"] <= 0:
        raise ValueError(\"Field 'orders_count' must be greater than zero\")
    if user_data[\"id\"] is None:
        raise ValueError(\"Field 'id' cannot be None\")

def calculate_user_discount(user_data):
    # Input validation and guard against null/undefined values
    validate_user_data(user_data)

    tier = user_data[\"tier\"]
    spend = user_data[\"total_spend\"]
    orders_count = user_data[\"orders_count\"]

    # Guard against division by zero (already validated orders_count > 0)
    average_order_value = spend / orders_count

    discount = 0.0
    if tier == \"GOLD\":
        discount = 0.20
    elif tier == \"SILVER\":
        discount = 0.10
    # If tier is other value, discount remains 0.0

    return {\"user_id\": user_data[\"id\"], \"discount_applied\": discount, \"aov\": average_order_value}

def process_transaction(user_data):
    '''
    Process a user transaction with error handling.
    '''
    try:
        print(\"Processing user transaction...\")
        result = calculate_user_discount(user_data)
        print(\"Transaction processed successfully!\")
        return result
    except Exception as e:
        # Log the error (here we simply print it) and re-raise or return an error dict.
        print(f\"Error processing transaction: {e}\")
        raise  # Re-raise the exception for the caller to handle,
               # or alternatively return {\"error\": str(e)}.
