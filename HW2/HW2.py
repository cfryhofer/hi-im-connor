#Connor Fryhofer 1853826

list_Month = { "january": "1", "february": "2", "march": "3", "april": "4", "may": "5", "june": "6", "july": "7", "august": "8",
               "september": "9", "october": "10", "november": "11", "december": "12"}

input_file=open(HW2/inputDates.txt,'r')

output_file=open(HW2/parsedDates.txt,'w')

for each in input_file:
    if each!="-1":
        lis = each.split()
        if len (lis) >=3:
            Month=lis[0]
            Day=lis[1]
            Year=lis[2]

            if Month.lower() in list_Month:
                comma=Day[-1]
                if comma==',':
                    Day=Day[:len(Day)-1]
                    Number_months=list_Month[Month.lower()]
                    answer=Number_months+"/"+Day+"/"+Year

                    output_file.write (answer)
                    output_file.write("\n")




output_file.close()
input_file.close()




