def add_setting(settings, values):
    key, value = values

    if key.lower() in settings:
            return f"Setting '{key.lower()}' already exists! Cannot add a new setting with this name."
    else:
        settings[key.lower()] = value.lower()
        return f"Setting '{key.lower()}' added with value '{value.lower()}' successfully!"
    pass

def update_setting(settings, values):
    if not values[0].lower() in settings:
        return f"Setting '{values[0].lower()}' does not exist! Cannot update a non-existing setting."
    else:
        settings[values[0].lower()] = values[1].lower()
        return f"Setting '{values[0].lower()}' updated to '{values[1].lower()}' successfully!"

def delete_setting(settings, key):
    key = key.lower()
    if key in settings.keys():
        settings.pop(key)
        return f"Setting '{key}' deleted successfully!"
    else:
        return "Setting not found!"

def view_settings(test_settings):
    if not test_settings:
        return "No settings available."
    else: 
        view = "Current User Settings:\n"
        for key, value in test_settings.items():
            view += f"{key.capitalize()}: {value.lower()}\n"
        return view

test_settings = { 'theme': 'Dark', 'notifications': 'enabled', 'size': 'high' }

#print(repr(view_settings(test_settings)))

test_settings = {
    'theme': 'Dark',
    'notifications': 'enabled',
    'size': 'high'
}

print(view_settings(test_settings))

print(add_setting(test_settings, ("language", "English")))
print(view_settings(test_settings))

print(update_setting(test_settings, ("theme", "Light")))
print(view_settings(test_settings))

print(delete_setting(test_settings, "size"))
print(view_settings(test_settings))

