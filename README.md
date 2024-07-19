# Motorbike Spares Sales Record System
## Description
This project is a simple sales record system designed for a motorbike spares shop. It allows users to record daily sales of spare parts and calculate daily totals. The system is implemented in Python and provides both a command-line interface and a web-based interface using Flask.
## Features
- Add sales records with item name, quantity, and price
- Calculate and display daily sales totals
- Data persistence using JSON file storage
- Web interface for easy access and use
- Currency display in Kenya Shillings (KES)
## Prerequisites
Before you begin, ensure you have met the following requirements:
- Python 3.6 or higher installed
- pip (Python package manager) installed
## Installation
1. Clone the repository:
``` console
git clone https://github.com/BilhaNanetia/first-sales.git
cd first-sales
```
2. Install the required dependencies:
``` console
pip install flask
```
## Usage
### Command-line Interface
1. Run the command-line version:
``` console
python sales_record.py
```
2. Follow the on-screen prompts to add sales or get daily totals.
### Web Interface
1. Run the web server:
``` console
python web_sales_record.py
```
2. Open a web browser and navigate to `http://127.0.0.1:5000`
3. Use the web interface to add sales and get daily totals.
4. Restart the server to view changes in the command line
## Data Storage
Sales data is stored in a JSON file named `sales_record.json`. This file is automatically created in the same directory as the Python scripts when you add your first sale.
## Currency
All monetary values are in Kenya Shillings (KES).
## Contributing
Contributions to this project are welcome. Please follow these steps:
1. Fork the repository
2. Create a new branch (`git checkout -b feature/AmazingFeature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
5. Push to the branch (`git push origin feature/AmazingFeature`)
6. Open a Pull Request
## License
This project is licensed under the MIT License. See the `LICENSE` file for details.
## Contact
Feel free to contact me through my email bilhaleposo@gmail.com

Project Link: [https://github.com/BilhaNanetia/first-sales] (https://github.com/BilhaNanetia/first-sales)
