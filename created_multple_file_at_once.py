import os

# List of template file names to be created
templates = [
    "base.html",
    "home.html",
    "about.html",
    "login.html",
    "register.html",
    "dashboard.html",
    "product.html",
    "cart.html",
    "checkout.html",
    "404.html",
    "500.html",
    "search.html",
    "contact.html",
    "profile.html",
    "orders.html",
    "faq.html"
]

templates_dir = "templates"
os.makedirs(templates_dir, exist_ok=True)


for template in templates:
    file_path = os.path.join(templates_dir, template)
    with open(file_path, "w") as file:
        file.write(f"<!-- {template} content goes here -->")
        print(f"Created: {file_path}")

print("All template files have been created!")
