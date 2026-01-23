from functools import wraps


def require_admin(f):
    @wraps(f)
    def wrapper(user_role):
        if not user_role == "admin":
            print("Access Denied")  # return "Access Denied"
            return None

        return f(user_role)

    return wrapper


@require_admin
def check_inventory(role):
    print("Inventory Checked")


# check_inventory() => will return error because no role is provided
check_inventory("admin")
check_inventory("user")

# OUTPUT:
# Inventory Checked
# Access Denied
