# 🧪 Automated Login Testing using Selenium | Prodigy InfoTech Internship – Task 03

## 📌 Overview

This project is part of my internship at **Prodigy InfoTech**. It automates the login functionality of a web application using **Python** and **Selenium WebDriver**.

> ✅ Covers both **positive** and **negative** test cases on the demo site:  
> 🔗 [https://www.saucedemo.com/](https://www.saucedemo.com/)

---

## ⚙️ Technologies Used

- Python
- Selenium WebDriver
- unittest (Python’s built-in testing framework)
- ChromeDriver or WebDriverManager
- PyCharm

---

## 🧪 Test Cases Covered

| Test Case               | Username       | Password       | Expected Output                                  |
|-------------------------|----------------|----------------|--------------------------------------------------|
| ✅ Valid Login           | standard_user  | secret_sauce   | Redirect to inventory page                       |
| ❌ Invalid Credentials   | invalid_user   | wrong_pass     | Show error: "Username and password do not match" |
| ❌ Empty Username        | (empty)        | secret_sauce   | Show error: "Username is required"               |
| ❌ Empty Password        | standard_user  | (empty)        | Show error: "Password is required"               |
| ❌ Empty Fields          | (empty)        | (empty)        | Show error: "Username is required"               |

---

## 📂 Project Structure
├── Task3.py # Main test script  
├── chromedriver.exe # WebDriver (if using manually)  
├── README.md # This file  


---

## 🚀 How to Run

1. Clone this repository:

```bash
git clone https://github.com/your-username/prodigy-task3-login-test.git
cd prodigy-task3-login-test
```
2. Install dependencies:

   ```bash
   pip install selenium webdriver-manager
   ```

3. Run the test suite:

   ```bash
   python -m unittest Task3.py
   ```

## 📷 Sample Output
   All test cases passed successfully!
