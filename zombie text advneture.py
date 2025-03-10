import os, random, time

keys = False
crowbar = False
m4 = False
loop = True
garage_counter = 0

def randinteger(number):
  integer = random.randint(1, number)
  return integer
  
#serial 1
def bedroom():
  while loop == True:
    os.system('clear')
    print('Adventure Game')
    print('LOCATION: Bedroom')
    print('')
    print('You are in the bedroom, you look around the room and have to option to go to the kitchen.')
    print('1. GOTO kitchen')
    bedroom_input = input('> ')
    if bedroom_input == '1':
      menu(2)
    else:
      print('Please input that again')
      time.sleep(1)
      continue
      
#serial 2
def kitchen():
  while loop == True:
    os.system('clear')
    print('Adventure Game')
    print('LOCATION: Kitchen')
    print('')
    print('You have arrived in the kitchen, you hear strange noises outside and decide to investigate later, you have the option to return to the bedroom, hide to the cabinet or go through the backdoor into the backyard.')
    print('1. GOBACKTO Bedroom')
    print('2. GOTO Cabinet')
    print('3. GOTO Backdoor')
    kitchen_input = input('> ')
    if kitchen_input == '1':
      menu(1)
    elif kitchen_input == '2':
      menu(3)
    elif kitchen_input == '3':
      menu(4)
    else:
      print('Please input that again')
      time.sleep(1)
      continue

#serial 3
def cabinet():
  global keys, crowbar
  while loop == True:
    keys = False
    crowbar = False
    os.system('clear')
    print('Adventure Game')
    print('LOCATION: Cabinet')
    print('')
    print('You are hiding in cabinet, you wait for 10 minutes and then you hear \033[1;31mbanging\033[0m on the cabinet door and you open the cabinet door to see bloodied hands reaching for you. Your vision starts to fade and the last thing you see is a human that looks \033[1;31mUNDEAD\033[0m.')
    print('\033[0;31m--FATALITY--\033[0m')
    time.sleep(4)
    input('Press \033[0;32m[ENTER]\033[0m to exit')
    menu(0)

#serial 4
def backyard():
  while loop == True:
    os.system('clear')
    print('Adventure Game')
    print('LOCATION: Backyard')
    print('')
    print('You have arrived in the backyard, there are three ways to go, you can either go back to the kitchen, go into the shed or head into the frontyard by a passage.')
    print('1. GOBACKTO Kitchen')
    print('2. GOTO Shed')
    print('3. GOTO Frontyard')
    backyard_input = input('> ')
    if backyard_input == '1':
      menu(2)
    elif backyard_input == '2':
      menu(5)
    elif backyard_input == '3':
      menu(6)
    else:
      print('Please input that again')
      time.sleep(1)
      continue
      
#serial 5
def shed():
  global keys, crowbar
  while loop == True:
    if keys == False:
      os.system('clear')
      print('Adventure Game')
      print('LOCATION: Shed')
      print('')
      print('You have arrived in the shed, around you are two items, a crowbar and car keys. You can either go back to the backyard or pick up the items.')
      print('1. GOBACKTO Backyard')
      print('2. PICKUP Crowbar, Keys')
      shed_input = input('> ')
      if shed_input == '1':
        menu(4)
      elif shed_input == '2':
        keys = True
        crowbar = True
        os.system('clear')
        print('Adventure Game')
        print('LOCATION: Shed')
        print('')
        print('You are in the shed, you can go to the backyard now.')
        print('1. GOBACKTO Backyard')
        shed_input = input('> ')
        if shed_input == '1':
          menu(4)
        else:
          print('Please input that again')
          time.sleep(1)
          continue
      else:
        print('Please input that again')
        time.sleep(1)
        continue
    elif keys == True or crowbar == True:
      os.system('clear')
      print('Adventure Game')
      print('LOCATION: Shed')
      print('')
      print('You are in the shed, you can go to the backyard now.')
      print('1. GOBACKTO Backyard')
      shed_input = input('> ')
      if shed_input == '1':
        menu(4)
      else:
        print('Please input that again')
        time.sleep(1)
        continue

#serial 6
def frontyard():
  global keys, crowbar
  while loop == True:
    os.system('clear')
    print('Adventure Game')
    print('LOCATION: Frontyard')
    print('')
    if keys == False or crowbar == False:
      print('You have arrived in the frontyard, you can go back to the backyard but cannot access the street or garage, it looks like you need a crowbar to progress further. ')
      print('1. GOBACKTO Backyard')
      frontyard_input = input('> ')
      if frontyard_input == '1':
        menu(4)
      else:
        print('Please input that again')
        time.sleep(1)
        continue
    if keys == True or crowbar == True:
      print('You have arrived in the frontyard, you can either go back to the backyard, use the crowbar to break the fence and get onto the street or use the crowbar to break through one of the walls of the garage and enter the garage.')
    print('1. GOBACKTO Backyard')
    print('2. GOTO Street')
    print('3. GOTO Garage')
    frontyard_keys_input = input('> ')
    if frontyard_keys_input == '1':
      menu(4)
    elif frontyard_keys_input == '2':
      menu(7)
    elif frontyard_keys_input == '3':
      menu(8)

#serial 7
def street():
  global keys, crowbar
  while loop == True:
    keys = False
    crowbar = False
    os.system('clear')
    print('Adventure Game')
    print('LOCATION: Cabinet')
    print('')
    print('You break through the frontyard fence and walk on to the street and immediately you see people that look \033[1;31mUNDEAD\033[0m, you are surounded by the \033[1;31mUNDEAD\033[0m and they claw and rip at your skin, you fall to the ground in \033[1;31mAGONY\033[0m and as your vision starts to go blank you are suddenly reanimated but are not in control of your own \033[4mBODY\033[0m.')
    print('\033[0;31m--FATALITY--\033[0m')
    time.sleep(4)
    input('Press \033[0;32m[ENTER]\033[0m to exit')
    menu(0)

#serial 8
def garage():
  global keys, crowbar
  while loop == True:
    os.system('clear')
    print('Adventure Game')
    print('LOCATION: Garage')
    print('')
    print('You break open the wall to the garage with the crowbar and walk into the garage. Inside the garage on your left you see a partly damaged M1A2 main battle tank and on your right you see a 79 series landcruiser. You can either go back to the frontyard or either enter the tank or car.')
    print('1. Frontyard')
    print('2. Tank')
    print('3. Landcruiser')
    garage_input = input('> ')
    if garage_input == '1':
      menu(6)
    elif garage_input == '2':
      menu(9)
    elif garage_input == '3':
      menu(10)

#serial 9
def tank():
  global m4
  while loop == True:
    os.system('clear')
    print('Adventure Game')
    print('LOCATION: Tank')
    print('')
    print('You open the hatch into the tank and jump in, you fumble around and find the key hole, you contemplate putting the key in, and think about returning to the garage. You also notice a suppressed M4 carbine assualt rifle sitting next to you.')
    print('1. GOBACKTO Garage')
    print('2. START Tank')
    print('3. PICKUP M4')
    tank_input = input('> ')
    if tank_input == '1':
      menu(8)
    elif tank_input == '2':
      print('PlaceHolder')
    elif tank_input == '3':
      m4 = True
      os.system('clear')
      print('Adventure Game')
      print('LOCATION: Tank')
      print('')
      print('You are in the tank, you can go back into the garage or start the tank up.')
      print('1. GOBACKTO Garage')
      print('2. START Tank')
      tank_input = input('> ')
      if tank_input == '1':
        menu(8)
        

def menu(serial):
  if serial == 0:
    os.system('clear')
    print('Adventure Game')
    print('1. PLAY')
    menu_input = input('> ')
    if menu_input == '1':
      bedroom()
  elif serial == 1:
    bedroom()
  elif serial == 2:
    kitchen()
  elif serial == 3:
    cabinet()
  elif serial == 4:
    backyard()
  elif serial == 5:
    shed()
  elif serial == 6:
    frontyard()
  elif serial == 7:
    street()
  elif serial == 8:
    garage()
  elif serial == 9:
    tank()
  elif serial == 10:
    ute()

menu(0)