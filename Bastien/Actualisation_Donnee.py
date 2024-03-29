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
                Q1_answer = line["Q1"]
                Q2_answer = line["Q2"]
                Q3_answer = line["Q3"]
                Q4_answer = line["Q4"]
                Q5_answer = line["Q5"]
                Q6_answer = line["Q6"]
                Q1[Q1_answer-1] += 1
                Q2[Q2_answer-1] += 1
                Q3[Q3_answer-1] += 1
                Q4[Q4_answer-1] += 1
                Q5[Q5_answer-1] += 1
                Q6[Q6_answer-1] += 1

                line_check += 1
            else :
                line_check += 1
        average_qu3.append(int(line["Q3"]))
        average_qu4.append(int(line["Q4"]))
        average_qu5.append(int(line["Q5"]))
        average_qu6.append(int(line["Q6"]))
    sleep(5)
    sheet_table[5].update_cell(2,column_end,line_check-1)
    sleep(1)
    column_end += 1

    #put return of the line list
    line_display = line_number[change_display]
    #put each list answer in a new list (list in list)
    question_list = [Q1,Q2,Q3,Q4,Q5,Q6]
    for row in question_list:
        #put return of the column list
        column_display = column[change_display]
        result = []
        average_display = []
        #increment variable
        inc = 1
        for elem in row :
            sheet_table[6].update_cell(line_display,column_display,elem)
            sleep(1)
            #while loop
            out = 0
            while out != elem :
                result.append(inc)
                out +=1
            inc += 1
            column_display += 1
        average_display = round(statistics.mean(result),1)
        quart = statistics.quantiles(result)
        sheet_clean_quartile.update_cell(line_quantile[nbr_line_quant],col_quantile[nbr_col_quant],round(quart[0], 1))
        sleep(1)
        nbr_col_quant += 1
        sheet_clean_quartile.update_cell(line_quantile[nbr_line_quant],col_quantile[nbr_col_quant],round(quart[2], 1))
        sleep(1)
        nbr_col_quant += 1
        sheet_clean_quartile.update_cell(line_quantile[nbr_line_quant],col_quantile[nbr_col_quant],average_display)
        sleep(1)
        line_display += 1
        nbr_col_quant += 1
        nbr_line_quant += 1
        if nbr_col_quant == 36 :
            nbr_col_quant = 0
    change_display += 1
    class_change += 1
average = [statistics.mean(average_qu3), statistics.mean(average_qu4), statistics.mean(average_qu5), statistics.mean(average_qu6)]
while average_change == 1 :
    if not sheet_table[4].row_values(line_average) :
        sleep(1)
        col_glo = 1
        while col_glo<8:
            sheet_table[4].update_cell(line_average,col_glo, "Moyenne")
            sleep(1)
            col_glo += 1
            sheet_table[4].update_cell(line_average,col_glo, average[data_average_list])
            sleep(1)
            data_average_list += 1
            col_glo += 1
        average_change = 0
    else :
        line_average += 1
while end_sheet == 1:
    if not sheet_base.row_values(2) :
        sheet_base.delete_row(2)
    else :
        end_sheet = 0
