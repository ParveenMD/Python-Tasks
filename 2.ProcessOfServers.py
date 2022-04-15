print("MD Parveen")
import psutil
import csv
import webbrowser
processlist = list()
for process in psutil.process_iter():
    processlist.append(process)
print(processlist)
with open('processlist.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(processlist)
listtostr = ' '.join(map(str, processlist))
with open('processlist.html', 'w') as html_file:
    html_file.write(listtostr)