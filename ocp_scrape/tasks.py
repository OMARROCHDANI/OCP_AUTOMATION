from celery import shared_task
from celery_progress.backend import ProgressRecorder
from time import sleep
from django.http import FileResponse
from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
from io import BytesIO
import io
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from io import BytesIO
from django.core.files.base import ContentFile
from .models import GeneratedFiles
from django.contrib.auth.models import User

@shared_task(bind=True)
def go_to_sleep(self, duration):
    progress_recorder=ProgressRecorder(self)
    for i in range(10):
        sleep(duration)
        progress_recorder.set_progress(i + 1, 10, f'iteration...{i}')
    return 'Done'


@shared_task(bind=True)
def run_script_task(self,user_id):
    progress_recorder=ProgressRecorder(self)
    user = User.objects.get(id=user_id)

    # create an instance of the Chrome driver
    driver = webdriver.Chrome()
    # navigate to a webpage
    driver.get("https://supplier.ocpgroup.ma/#/landing-page/opportunities")
    driver.refresh()
    data = []
    wait = WebDriverWait(driver, 10)
    buttons = driver.find_elements(By.CLASS_NAME, "MuiButton-sizeSmall")
    i=0
    for button in buttons:
        button.click()
        driver.switch_to.window(driver.window_handles[-1])
        informations = driver.find_elements(By.CLASS_NAME, "form_answer")
        var_names = ["Code du dossier", "Titre du dossier", "Description", "Notes", "Catégorie de travaux", "Type de procédure", "Date limite d'affichage", "Organisation Acheteur", "Contact", "Email"]
        info_dict = {}
        for j, information in enumerate(informations):
            info_dict[var_names[j]] = information.text
        data.append(info_dict)
        driver.close()
        progress_recorder.set_progress( 1+i, len(buttons))
        i=i+1
        driver.switch_to.window(driver.window_handles[0])
    driver.close()
    df = pd.DataFrame(data)
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine='openpyxl')
    df.to_excel(writer, index=False, sheet_name='Sheet1')  # Specify the sheet name if needed
    writer.book.save(output)
    output.seek(0)
    your_model_instance = GeneratedFiles(user=user)  # Replace "YourModel" with your actual model name
    your_model_instance.file_field.save('filename.xlsx', ContentFile(output.read()))
    your_model_instance.save()
    return 'Done' 
#     the old view:
#     df = pd.DataFrame(data)
#     response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
#     response['Content-Disposition'] = 'attachment; filename=data.xlsx'
#     df.to_excel(response, index=False)
#     driver.close()
#     return response 

#  the view that does not renders the template : 
#    processed_data = task2.get()
# df = pd.DataFrame(processed_data)
# response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
# response['Content-Disposition'] = 'attachment; filename=data.xlsx'
# df.to_excel(response, index=False)  
@shared_task(bind=True)
def run_script_task_3(self):
    progress_recorder=ProgressRecorder(self)
    # create an instance of the Chrome driver
    driver = webdriver.Chrome()
    # navigate to a webpage
    driver.get("https://supplier.ocpgroup.ma/#/landing-page/opportunities")
    driver.refresh()
    data = []
    wait = WebDriverWait(driver, 10)
    buttons = driver.find_elements(By.CLASS_NAME, "MuiButton-sizeSmall")
    i=0
    for button in buttons:
        button.click()
        driver.switch_to.window(driver.window_handles[-1])
        informations = driver.find_elements(By.CLASS_NAME, "form_answer")
        var_names = ["Code du dossier", "Titre du dossier", "Description", "Notes", "Catégorie de travaux", "Type de procédure", "Date limite d'affichage", "Organisation Acheteur", "Contact", "Email"]
        info_dict = {}
        for j, information in enumerate(informations):
            info_dict[var_names[j]] = information.text
        data.append(info_dict)
        driver.close()
        progress_recorder.set_progress( 1+i, len(buttons))
        i=i+1
        driver.switch_to.window(driver.window_handles[0])
    driver.close()
    return 'Done'
  
    

