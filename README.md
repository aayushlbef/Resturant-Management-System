# Restaurant Management System

## Description
This is a 1st Semester Python Project developed for "Delicious Restaurant," located in Kuala Lumpur. The restaurant offers a comfortable dining experience by providing a variety of food menus across various cuisine types. The goal of this project is to design and develop a system to streamline and manage the daily operations of the restaurant.

## Project Overview
The system is a role-based management application that allows different users (Administrator, Manager, Chef, and Customer) to interact with the restaurant's operations through a command-line interface. It uses text files for persistent data storage.

## User Roles and Features

### 1. Administrator
- **Staff Management**: Add, edit, and delete Manager and Chef accounts.
- **Sales Reporting**: View detailed sales reports filtered by month or by specific chefs.
- **Customer Feedback**: Monitor and view feedback submitted by customers.
- **Profile Management**: Update personal account details.

### 2. Manager
- **Customer Management**: Manage customer accounts (Add/Edit/Delete).
- **Menu Management**: Control the food menu, including adding new items, updating pricing, and deleting dishes across different categories.
- **Inventory Oversight**: View the list of ingredients requested by the chefs.
- **Profile Management**: Update personal account details.

### 3. Chef
- **Order Management**: View pending orders and mark them as completed once prepared.
- **Order History**: Review all past orders placed by customers.
- **Ingredient Requests**: Manage the inventory by adding, editing, or deleting requested ingredients.
- **Profile Management**: Update personal account details.

### 4. Customer
- **Food Ordering**: Browse the menu by category and place orders with specified quantities.
- **Payment System**: A simulated payment process to confirm and finalize orders.
- **Order Tracking**: View the status of their current pending orders and order history.
- **Feedback**: Submit feedback directly to the administrator.
- **Profile Management**: Update personal account details and register new accounts.

## Technical Implementation
- **Language**: Python
- **Storage**: Text-based flat files (`.txt`) located in the `txt_files/` directory, using dictionary-like string representations for data.
- **Modular Structure**: 
  - `main.py`: Entry point of the application.
  - `py_files/`: Contains logic for each role (`administrator.py`, `manager.py`, `chef.py`, `customer.py`), shared `functions.py`, `login_register.py`, and `validation.py`.
  - `txt_files/`: Database for users, menu, ingredients, order history, and feedback.

## Installation and Usage
1. Ensure you have Python 3.x installed.
2. Clone the repository.
3. Run the application:
   ```bash
   python main.py
   ```
4. Select your role from the login page and enter the required credentials to access the respective panel.
