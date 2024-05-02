import pickle


def load_or_create_profile():
    try:
        with open('user_profile.pkl', 'rb') as file:
            user_profile = pickle.load(file)
            print("User profile loaded successfully.")
    except FileNotFoundError:
        user_profile = {'search_history': [], 'viewed_items': [], 'liked_items': [], 'disliked_items': []}
        print("New user profile created.")
    return user_profile

# Function to save user profile
def save_profile(user_profile):
    with open('user_profile.pkl', 'wb') as file:
        pickle.dump(user_profile, file)
    print("User profile saved successfully.")

# Function to update user preferences based on interactions
def update_preferences(user_profile, interaction):
    # Example code for updating preferences based on different interactions
    if interaction.startswith('search'):
        user_profile['search_history'].append(interaction)
    elif interaction.startswith('view'):
        user_profile['viewed_items'].append(interaction.split(' ')[-1])
    elif interaction.startswith('like'):
        user_profile['liked_items'].append(interaction.split(' ')[-1])
    elif interaction.startswith('dislike'):
        user_profile['disliked_items'].append(interaction.split(' ')[-1])

# Function to generate personalized response
def personalize_response(user_profile, query):
    # Example code for generating personalized responses based on user profile
    if query.startswith('search'):
        return "I found some items matching your search query. Here are the recommendations..."
    elif query.startswith('view'):
        return "You have viewed the item. Here are more details..."
    elif query.startswith('like'):
        return "The item has been added to your liked items."
    elif query.startswith('dislike'):
        return "The item has been added to your disliked items."
    else:
        return "I'm sorry, I don't understand that command."

# Main function
def main():
    user_profile = load_or_create_profile()

    while True:
        query = input("User: ").lower()
        if query == 'exit':
            save_profile(user_profile)
            break
        elif query.startswith('search') or query.startswith('view') or query.startswith('like') or query.startswith('dislike'):
            update_preferences(user_profile, query)
        else:
            response = personalize_response(user_profile, query)
            print("Assistant:", response)

if __name__ == "__main__":
    main()
