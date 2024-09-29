# Data-through-excel

A Django-based project that enables users to generate leads and save data through the admin panel, excel sheets, APIs, and provides the ability to download data as PDFs.

## Features

- **Generate Leads:** Efficiently collect and manage leads.
- **Save Data through Admin Panel:** Easily store and update data via the admin interface.
- **Save Data through Excel Sheets:** Bulk data upload and management using excel files.
- **Save Data through APIs:** Seamlessly integrate and send data to third-party APIs.
- **Generate PDF:** Download university and lead data in PDF format for reporting and documentation.

## Requirements

   ```bash
   Django==5.0
   djangorestframework==3.14.0
   djangorestframework-simplejwt==5.2.2
   jazzmin==2.8.1
   pandas==2.0.3
   requests==2.31.0
   reportlab==3.6.12
   ```
To install these dependencies, run:

   ```bash
   pip install -r requirements.txt
   ```
## Installation & Setup
1. Clone the repository:
   
   ```bash
   git clone https://github.com/Prakhar2706/Data-through-excel.git
   ```

2. Navigate to the project directory:
   
   ```bash
   cd Data-through-excel
   ```

3. Create a virtual environment:
   
   ```bash
   python -m venv env
   ```
4. Activate the virtual environment:

   * On Windows:
     
   ```bash
   .\env\Scripts\activate
   ```

   *On macOS/Linux:
   
   ```bash
   source env/bin/activate
   ```
5. Install the dependencies:
   
   ```bash
   pip install -r requirements.txt
   ```
6. Create migrations for your models:

   ```bash
   python manage.py makemigrations
   ```
7. Apply migrations:
   
   ```bash
   python manage.py migrate
   ```
8. Create a superuser:

   ```bash
   python manage.py createsuperuser
   ```
9. Start the development server:
   
   ```bash
   python manage.py runserver
   ```
10. Visit http://127.0.0.1:8000 in your browser to access the app.

11. For admin panel:
    
    ```bash
    http://127.0.0.1:8000/admin
    ```

## Usage
- To generate leads, upload Excel sheets or use the admin panel.
- API endpoints are available for saving data and integrating with third-party services.
- Download PDFs of stored data through the provided endpoint.
