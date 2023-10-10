# OCP automation

## Overview

Welcome to OCP automation – your dedicated platform for precision data extraction from the Portail-OCP website. Our sophisticated system, powered by Python, Django, Selenium, celery , is designed to reduce time and effort in multiple tasks related to data retrieval and more.



# Features

User Authentication:

- Create a secure account to access personalized features.
- Log in securely to monitor and manage your data extraction tasks.
  
Targeted Scraping and Automation:

- Utilize specialized scraping techniques and custom automation scripts to extract specific data from Portail-OCP.
- Real-time updates ensure you stay informed about the progress of your data extraction tasks.

File Format Flexibility:
- Run automation scripts that generate diverse file formats, such as xlsx and more, for convenient data organization and analysis.
- Download these files directly from your user profile.
  
Task Progress Tracking:

- Transparently monitor the progress of your data extraction tasks.
## How It Works

**User Registration:**
- Create your account with ease, ensuring a secure and personalized experience.
**Data Extraction and Automation:**
- Run specific scraping and automation scripts customized for the Portail-OCP website .
- Observe the real-time progress of your data extraction tasks, with detailed task summaries available in your user dashboard.
**Retrieve Targeted Data:**
- Explore the curated results and download the extracted data.
**Save Data and Analyze:**
- Save important data for future use directly from the extraction results.

## Installation

Ensure you have [Python](https://www.python.org/downloads/) installed on your machine.

1. Clone the repository:
   ```bash
   git clone https://github.com/OMARROCHDANI/OCP_AUTOMATION.git
    
2. Create a virtual environment (optional but recommended):
   ```bash
    python -m venv venv

3. Activate the virtual environment:
   ```bash
   venv\Scripts\activate

4. Install dependencies:
    ```bash
    pip install -r requirements.txt

5. Create a superuser account:
    ```bash
    python manage.py createsuperuser

6. Start the development server:
    ```bash
    python manage.py runserver
7. Ensure Redis is installed and running.


8. Start the Celery Worker: 
    ```bash 
    celery -A first_project.celery worker --pool=solo -l info


- Note: Ensure that you have MySQL and Apache running through XAMPP before starting the dev elopment server. The development server will rely on these services for its functionality.
Now, your ProfessionPulse instance is up and running. Open your web browser and navigate to http://localhost:8000 to access the application.

## Acknowledgments

We would like to thank the following libraries and frameworks that have been instrumental in the development of OCP automation:

- [Django](https://www.djangoproject.com/)
- [Selenium](https://www.selenium.dev/)
- [Celery](https://docs.celeryq.dev/en/stable/)
- [Redis](https://redis.io/)

A special thanks to our contributors for their valuable input and support.

   
