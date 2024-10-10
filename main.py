#Variables globales 
fullname = ""
#Funciones
def run(name: str, surname: str) -> str:
    # TODO
    global fullname
    #Variable local
    fullname = surname + " " + name 
    return fullname

#Codigo principal
# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
    print(f"{fullname}")