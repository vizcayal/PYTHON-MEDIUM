DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

def run():
    #all_python_dev = [ empleado["name"] for empleado in DATA if empleado["language"] == "python" ]
    all_python_dev = list(filter(lambda a:a['language']=='python', DATA))
    all_python_dev = list(map(lambda a:a['name'],all_python_dev))
    #all_platzi_workers = [ empleado["name"] for empleado in DATA if empleado["organization"] == "Platzi" ]
    all_platzi_workers = list(filter(lambda a:a["organization"]=='Platzi',DATA))
    all_platzi_workers = list(map(lambda a:a["name"], all_platzi_workers))
    
    #adults = list(filter(lambda worker:worker['age']>18, DATA))
    #adults = list(map(lambda worker:worker['name'], adults))
    adults = [empleado['name'] for empleado in DATA if empleado['age']>18]
    old_people = [empleado['name'] for empleado in DATA if empleado['age']>70]
    print(old_people)


if __name__ == '__main__':
    run()
