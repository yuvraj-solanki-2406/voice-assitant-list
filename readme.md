# Voice Command Shopping Assistant

## Overview

The **Voice Command Shopping Assistant** is a smart, voice-controlled application that helps users manage their shopping lists effortlessly. It leverages advanced speech recognition and content-based filtering techniques to offer smart suggestions and seamless CRUD (Create, Read, Update, Delete) operations for shopping list management.

---

## Features

### 1. **Voice Input Processing**
- Uses **Chrome Voice Input** for speech recognition.
- Processes user commands such as adding, removing, and updating items in the shopping list.

### 2. **Shopping List Management**
- Fully functional CRUD operations for managing shopping lists.
- Supports voice commands for:
  - Adding items to the list.
  - Removing specific items.
  - Clearing the entire list.
  - Updating item quantities or categories.

### 3. **Category Classification**
- Automatically classifies items into categories (e.g., "Electronics," "Beauty and Personal Care," "Footwear").

### 4. **Smart Suggestions**
- Implements a **content-based filtering** recommendation system using Flipkart sales data.
- Provides item suggestions based on user preferences and shopping history.

---

## Technical Stack

### Backend:
- **Flask**: Web framework for the application.
- **MongoDB**: Database for storing user lists and categories.

### Frontend:
- **HTML5/CSS3**: For user interface design.
- **JavaScript**: For interactive features and Chrome voice input.
- **Bootstrap**: For responsive design.

### Recommendation System:
- **Content-Based Filtering**:
  - Built using sales data from Flipkart.
  - Recommends items similar to those in the user's shopping list.

---

## Installation and Setup

### Prerequisites:
- Python 3.8+
- MongoDB (local or cloud-based, e.g., MongoDB Atlas)
- Chrome browser for voice input functionality

### Steps:
1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/voice-command-shopping-assistant.git
   cd voice-command-shopping-assistant
   ```

2. **Create a virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up MongoDB**:
   - If using a local MongoDB instance, ensure it is running.
   - Update the MongoDB connection string in the application configuration file.

5. **Run the application**:
   ```bash
   python app.py
   ```

6. **Access the app**:
   Open your browser and navigate to `http://127.0.0.1:5000/`.

---

## Usage

### Voice Commands:
- **Add Item**: "Add [item name] to my list."
- **Remove Item**: "Remove [item name] from my list."
- **Clear List**: "Clear my shopping list."
- **Update Item**: "Update [item name] to [new category/quantity]."

### Smart Suggestions:
- View personalized recommendations based on your current shopping list.
- Add suggested items to your list with a single click.

---

## Evaluation Points

1. **Voice Processing**:
   - High accuracy in recognizing user commands.

2. **Command Accuracy**:
   - Handles CRUD operations effectively based on voice input.

3. **List Organization**:
   - Intuitive UI for viewing and managing categorized shopping lists.

4. **Suggestion Relevance**:
   - Recommendations tailored to user preferences using content-based filtering.

---

## Future Enhancements

- Integrate a **machine learning-based recommendation engine** for collaborative filtering.
- Add **multi-language support** for voice commands.
- Enable offline functionality for voice input and list management.
- Provide **email or SMS notifications** for shopping reminders.
