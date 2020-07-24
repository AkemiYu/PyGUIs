from tkinter import *
import requests
import json

root = Tk()
root.title('AQI app')

def lookup():
    try:
        api_req = requests.get('http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=' + zipcode.get() +'&distance=7&API_KEY=06C47C02-D23C-489E-9A4F-1020C19E11F7')
        api = json.loads(api_req.content)
        area = api[0]['ReportingArea']
        quality = api[0]['AQI']
        category = api[0]['Category']['Name']

        if category == 'Good':
            bgColor = '#00e400'
        elif category == 'Moderate':
            bgColor = '#ffff00'
        elif category == 'Unhealthy for Sensitive Groups':
            bgColor = '#ff7e00'
        elif category == 'Unhealthy':
            bgColor = '#ff0000'
        elif category == 'Very Unhealthy':
            bgColor = '#8f3f97'
        else:
            bgColor = '#7e0023'

        label = Label(root, text=f'{area} Air Quality Index: {str(quality)} ({category})', 
                                                font=('Times New Roman', 20), 
                                                background=bgColor)
        label.grid(row=1, column=0, columnspan=2)
    except Exception as e:
        api = 'Error'

zipcode = Entry(root, fg='dimgray')
zipcode.insert(0, 'Enter your zipcode here')
zipcode.grid(row=0, column=0, stick=E)
submit = Button(root, text='Lookup', command=lookup)
submit.grid(row=0, column=1, stick=W)

root.mainloop()
