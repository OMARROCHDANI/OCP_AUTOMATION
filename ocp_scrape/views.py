from django.shortcuts import render
import pandas as pd
from .models import GeneratedFiles
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from io import BytesIO
from django.core.files.base import ContentFile
from django.contrib.auth.decorators import login_required
from .tasks import go_to_sleep
from .tasks import run_script_task

# Create your views here.
def firstFunction(request):
    return render(request, 'ocp_scrape.html', {})
@login_required
def run_script(request):
    user_id = request.user.id
    task2 = run_script_task.delay(user_id)
    return render(request, 'progressindex2.html', {'task_id' : task2.task_id})


def progress(request):
    task = go_to_sleep.delay(1)
    return render(request, 'progressindex.html', {'task_id' : task.task_id})


def run_script_json(request):
    driver = webdriver.Chrome()
    # navigate to a webpage
    driver.get("https://supplier.ocpgroup.ma/#/landing-page/opportunities")
    driver.refresh()
    data = []
    wait = WebDriverWait(driver, 10)
    buttons = driver.find_elements(By.CLASS_NAME, "MuiButton-sizeSmall")
    
    for button in buttons:
        button.click()
        driver.switch_to.window(driver.window_handles[-1])
        informations = driver.find_elements(By.CLASS_NAME, "form_answer")
        var_names = ["Code du dossier", "Titre du dossier", "Description", "Notes", "Catégorie de travaux",
                     "Type de procédure", "Date limite d'affichage", "Organisation Acheteur", "Contact", "Email"]
        info_dict = {}
        for j, information in enumerate(informations):
            info_dict[var_names[j]] = information.text
        data.append(info_dict)
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
    driver.close()
    df = pd.DataFrame(data)
    df = pd.DataFrame(data)
    json_data = df.to_json(orient='records')

    your_model_instance = GeneratedFiles()  # Replace "YourModel" with your actual model name
    your_model_instance.file_field.save('filename.json', ContentFile(json_data))
    your_model_instance.save()

    latest_file = GeneratedFiles.objects.latest('id')
    context = {
        'file': latest_file
    }
    return render(request, 'demo2.html', context)
def run_script_csv(request):
    driver = webdriver.Chrome()
    # navigate to a webpage
    driver.get("https://supplier.ocpgroup.ma/#/landing-page/opportunities")
    driver.refresh()
    data = []
    wait = WebDriverWait(driver, 10)
    buttons = driver.find_elements(By.CLASS_NAME, "MuiButton-sizeSmall")
    
    for button in buttons:
        button.click()
        driver.switch_to.window(driver.window_handles[-1])
        informations = driver.find_elements(By.CLASS_NAME, "form_answer")
        var_names = ["Code du dossier", "Titre du dossier", "Description", "Notes", "Catégorie de travaux",
                     "Type de procédure", "Date limite d'affichage", "Organisation Acheteur", "Contact", "Email"]
        info_dict = {}
        for j, information in enumerate(informations):
            info_dict[var_names[j]] = information.text
        data.append(info_dict)
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
    driver.close()
    
    df = pd.DataFrame(data)
    csv_data = df.to_csv(index=False, encoding='utf-8')

    your_model_instance = GeneratedFiles()  # Replace "CSVFile" with your actual model name
    your_model_instance.file_field.save('filename.csv', ContentFile(csv_data))
    your_model_instance.save()

    latest_file = GeneratedFiles.objects.latest('id')
    context = {
        'file': latest_file
    }
    return render(request, 'demo3.html', context)


   