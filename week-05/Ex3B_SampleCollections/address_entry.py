# 1. Define Dictionary
contact_info = {
    "name" : "Sarah John",
    "address" : "Pike Creek",
    "city" : "Wilmington",
    "state" : "Delaware",
    "zip" : "19801"
}

# 2. Print formatted mailing address
print(f"""{contact_info["name"]}
{contact_info["address"]}, {contact_info["city"]}
{contact_info["state"]}, {contact_info["zip"]}""")

# 3. Remove name key:value
del contact_info["name"]

# 4. New variable for full_name
full_name = {
    "first name" : "Sarah",
    "last name" : "John"
}

# 5. Use .update() to add honorific
full_name.update({"honorific" : "Ms."})

# 6. Use .update() to add full_name
contact_info.update({"full_name" : full_name})

# 7. Print formatted address again
print(f"""{contact_info["full_name"]["honorific"]} {contact_info["full_name"]["first name"]} {contact_info["full_name"]["last name"]}
{contact_info["address"]}, {contact_info["city"]}
{contact_info["state"]}, {contact_info["zip"]}""")

