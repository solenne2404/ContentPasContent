import gspread
import statistics
import date_test
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
from time import sleep

#Connection on the gSheet
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("Python.json", scope)
client = gspread.authorize(creds)
#Open all sheet
sheet_base = client.open("Formulaire").sheet1
sheet_clean_CDA_1 = client.open("Formulaire").worksheet("CDA_1")
sheet_clean_CDA_2 = client.open("Formulaire").worksheet("CDA_2")
sheet_clean_DWWM_1 = client.open("Formulaire").worksheet("DWWM_1")
sheet_clean_DWWM_2 = client.open("Formulaire").worksheet("DWWM_2")
sheet_clean_average = client.open("Formulaire").worksheet("Moyenne_Global")
sheet_clean_end = client.open("Formulaire").worksheet("Coordonnee")
sheet_clean_display = client.open("Formulaire").worksheet("Affichage")
sheet_clean_quartile = client.open("Formulaire").worksheet("Quartile/moyenne")
#All clean sheet in one list
sheet_table = [sheet_clean_CDA_1, sheet_clean_CDA_2, sheet_clean_DWWM_1, sheet_clean_DWWM_2, sheet_clean_average, sheet_clean_end, sheet_clean_display]
    if line["Formation actuelle"] not in table:
        table[line["Formation actuelle"]] = []

    table[line["Formation actuelle"]].append({
        "Nom": line["Nom (Entièrement en majuscule)"],
        "Prénom": line["Prénom (Entièrement en minuscule)"],
        "Q1": int(line["Comment évaluez-vous les méthodes pédagogique et d'animation proposées cette semaine ?"]),
        "Q2": int(line["Comment évaluez-vous votre progression pendant cette semaine ?"]),
        "Q3": int(line["Comment évaluez-vous l'organisation matérielle de la formation (rythme, planning, horaire) ?"]),
        "Q4": int(line["Comment évaluez-vous les moyens pédagogiques mis à disposition (supports, documentation, ...) ?"]),
        "Q5": int(line["Comment évaluez-vous les échanges dans votre groupe ?"]),
        "Q6": int(line["Comment évaluez-vous la satisfaction de vos attentes personnelles ?"]),
        "Date": line["Horodateur"]
    })