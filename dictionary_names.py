# Python program to create a dictionary and add first name and last name values

def main():
    # Create an empty dictionary
    person_info = {}
    
    # Add first name and last name to the dictionary
    person_info['first_name'] = 'John'
    person_info['last_name'] = 'Doe'
    
    # Display the dictionary
    print("Dictionary with name values:")
    print(person_info)
    
    # Alternative way to create dictionary with initial values
    person_info2 = {
        'first_name': 'Jane',
        'last_name': 'Smthgf'
    }
    
    print("\nAnother dictionary created with initial values:")
    print(person_info2)
    
    # Access individual values
    print(f"\nFirst name: {person_info['first_name']}")
    print(f"Last name: {person_info['last_name']}")
    
    # Update values
    person_info['first_name'] = 'Michael'
    person_info['last_name'] = 'Johnson'
    
    print("\nUpdated dictionary:")
    print(person_info)

if __name__ == "__main__":
    main() 