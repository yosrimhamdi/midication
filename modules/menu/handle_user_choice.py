import modules.patient as patient
import modules.rendez_vous as rendezvous
import modules.ordonnance as ordo

def add_new_patient():
  ids = input('CIN: ')
  firstname = input('nom: ')
  lastname = input('prenon: ')
  sexe = input('sexe: ')
  age = input('age: ')

  if(ids.isdigit() and age.isdigit() and firstname.isalpha() and lastname.isalpha() and sexe.isalpha()):
    new_patient =  {
      'id': ids,
      'firstname': firstname,
      'lastname': lastname,
      'sexe': sexe,
      'age': age
    }
    patient.add_patient(new_patient)
    print('done')

  else:
    print('wrong input(s)') 


def delete_patient():
  ids = input('donner CIN de patient a supprimer: ')
  if (ids.isdigit()):
    patient.remove_patient(ids)
  else:
    print('wrong CIN')

def is_valid_date(date):
  parts = date.split('/')
  if (len(parts) != 3):
    return False
  else:
      if (parts[0].isdigit() and parts[1].isdigit() and parts[2].isdigit()):
        return True
      else:
        return False

def is_valid_time(time):
  parts = time.split(':')

  if (len(parts) != 2):
    return False
  else:
    if (parts[0].isdigit() and parts[1].isdigit()):
      return True
    else:
      return False

def add_rendezvous():
  ids = input('CIN: ')
  date = input('date jour/mois/annee: ')
  time = input('temp h:min ')

  if(ids.isdigit() and is_valid_date(date) and is_valid_time(time)):
    rendezvous.add_rendezvous({
      'id': ids,
      'date': date,
      'time': time
    })
  else:
    print('wrong input(s)')


def cancel_rendezvous():
  ids = input('donner le CIN de rendezvous a annule: ')

  if (ids.isdigit()):
    rendezvous.cancel_rendezvous(ids)

def modify_rendezvoud():
  ids = input('donner le CIN de rendezvous a modifier: ')
  date = input('donner nouveau date jour/mois/annee: ')
  time = input('donner nouveau temp h:min ')

  if(ids.isdigit() and is_valid_date(date) and is_valid_time(time)):
    rendezvous.modify_rendezvous(ids, {'date': date, 'time': time})
  else:
    print('wrong input(s)')
    
def get_medicines():
  med = []
  num = ''
  while not num.isdigit():
    num = input('enter le nombre des medicaments: ')
  
  for _  in range(0, int(num)):
    med.append({
      'title': input('nom du medicament: '),
      'quantity': input('quantite du medicament: '),
      'duration': input('duration du medicament: ')
    })

  return med



def create_ord():
  ids = input('CIN: ')
  firstname = input('nom: ')
  lastname = input('prenom: ')
  date = input('date jour/mois/annee: ')
  time = input('temp h:min ')

  medicines = get_medicines()

  if(ids.isdigit() and is_valid_date(date) and is_valid_time(time)):
    ordo.create_ord(ids, firstname, lastname, date,time, medicines,1)


def handle_user_choice(choice):
  if (choice.isdigit()):
    if(choice == '1'):
      add_new_patient()
    elif(choice == '2'):
      delete_patient()
    elif(choice == '3'):
      add_rendezvous()
    elif(choice == '4'):
      cancel_rendezvous()
    elif(choice == '5'):
      modify_rendezvoud()
    elif(choice == '6'):
      create_ord()