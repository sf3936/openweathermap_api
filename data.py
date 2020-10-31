import json


def get_form_data(request):
    city = request.form['cityName']
    try:
        mock = request.form['useMock']
    except:
        mock = False
    return (city, mock)

def load_json(path='mockdata/MockData.json'):
    try:
        with open(path) as file:
            data = json.load(file)
    except:
        data = {}
    return data
