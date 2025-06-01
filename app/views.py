from django.shortcuts import render, redirect
from .forms import UploadForm
from .models import FichierNotes
import pandas as pd

def home(request):
    context = {}
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            fichier_obj = form.save()
            df = pd.read_excel(fichier_obj.fichier.path)
            context['df'] = df.to_html(classes='table table-striped', index=False)
    else:
        form = UploadForm()
    context['form'] = form
    return render(request, 'app/home.html', context)


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def envoyer_messages(request):
    dernier_fichier = FichierNotes.objects.last()
    df = pd.read_excel(dernier_fichier.fichier.path)

    driver = webdriver.Chrome()  # Assure-toi que ChromeDriver est installé
    driver.get("https://web.whatsapp.com")
    input("Scanne le QR code et appuie sur Entrée...")

    for index, row in df.iterrows():
        numero = row['Numéro']
        nom = row['Prénom'] + ' ' + row['Nom']
        note = row['Note']
        msg = f"Bonjour {nom},\nVotre note est {note}/20. Cordialement."

        driver.get(f"https://wa.me/{numero}?text={msg}")
        time.sleep(5)

        try:
            bouton = driver.find_element(By.XPATH, '//a[contains(@href, "send")]')
            bouton.click()
            time.sleep(5)
        except Exception as e:
            print(f"Erreur pour {nom} : {e}")

    driver.quit()
    return redirect('home')
