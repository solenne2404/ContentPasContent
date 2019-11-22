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
#All class's name
class_name = ["CDA 1","CDA 2","DWWM 1","DWWM 2"]
#All useable's key
line_name = ["Nom","Prénom","Q1","Q2","Q3","Q4","Q5","Q6","Date"]

#List for having the average for all class'
average_qu3 = []
average_qu4 = []
average_qu5 = []
average_qu6 = []

#line/column for sheet_clean_number
column = [2,12,2,12]
line_number = [2,2,10,10]
col_quantile = [2,4,6,2,4,6,2,4,6,2,4,6,2,4,6,2,4,6,9,11,13,9,11,13,9,11,13,9,11,13,9,11,13,9,11,13 ]
line_quantile = [2,4,6,8,10,12,2,4,6,8,10,12,15,17,19,21,23,25,15,17,19,21,23,25]


#variable for deleting row in sheet_base
end_sheet = 1

#use for change the class name
class_change = 0

#change average number for all class'
data_average_list = 0

#use for change column in sheet_clean_end
column_end = 2

#change line/column for all class' average
line_average = 2
column_average = 2

#change the return of line/column list
change_display = 0

#while loop
average_change = 1

#Import all answers
value = sheet_base.get_all_records()

nbr_col_quant = 0
nbr_line_quant = 0

table = {}

for line in value:

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

while class_change < len(class_name):
    #check line for writing data
    line_check = 2
    #list for puting some answer (number of 1, number of 2...) for each question
    Q1 = [0, 0, 0, 0, 0]
    Q2 = [0, 0, 0, 0, 0]
    Q3 = [0, 0, 0, 0, 0]
    Q4 = [0, 0, 0, 0, 0]
    Q5 = [0, 0, 0, 0, 0]
    Q6 = [0, 0, 0, 0, 0]

    for line in table[class_name[class_change]]:
        #while loop
        y = 0

        #defined column for writing
        column_writing = 2
        while y < 8 :
            if not sheet_table[class_change].row_values(line_check):
                date_hours = line[line_name[8]].split(" ")
                just_date = date_hours[0].split("/")
                day,month,year = int(just_date[0]), int(just_date[1]), int(just_date[2])
                date_conversion = date_test.date(year,month,day)
                week_number = date_test.date.isocalendar(date_conversion)
                sheet_table[class_change].update_cell(line_check,1, week_number[1])
                sleep(1)
                while y < 8 :
                    sheet_table[class_change].update_cell(line_check,column_writing, line[line_name[y]])
                    sleep(1)
                    y += 1
                    column_writing += 1
                line_check += 1
            else :
                line_check += 1
    class_change += 1