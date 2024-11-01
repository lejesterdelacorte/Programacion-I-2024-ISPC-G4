import pickle

def load_user(filename):
    try:
        with open(filename, 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        return {}

def save_user(filename, usuarios):
   
    usuarios_ordenados = dict(sorted(usuarios.items(), key=lambda item: item[1].DNI))
    with open(filename, 'wb') as file:
        pickle.dump(usuarios_ordenados, file)
