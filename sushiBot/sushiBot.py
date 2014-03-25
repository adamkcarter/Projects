import ImageGrab
import os
import time
import win32api, win32con
import ImageOps
from numpy import *

#Global Variables
#-----------------
"""
All coordinates assume a screen resolution of 1280x1024. Chrome maximized 
with no bookmarks nor title bar.
x_pad = 237
y_pad = 383
Play area =  x_pad+1, y_pad+1, 877, 863
"""

x_pad = 237
y_pad = 383


def screenGrab():
    box = (x_pad+1,y_pad+1,x_pad + 640, y_pad + 480)
    im = ImageGrab.grab(box)
    #im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG
    return im

def grab():
    box = (x_pad+1,y_pad+1,x_pad + 640, y_pad + 480)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolours())
    a = a.sum()
    print a
    return a

def main():
    pass
 
if __name__ == '__main__':
    main()

def leftClick():
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
	time.sleep(.1)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
	print "Click." #Optional, input for debugging purposes.

def leftDown():
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
	time.sleep(.1)
	print "Left Down"

def leftUp():
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
	time.sleep(.1)
	print "Left Release"

def mousePos(Cord):
	win32api.SetCursorPos((x_pad + Cord[0], y_pad + Cord[1]))

def get_Cords():
	x,y = win32api.GetCursorPos()
	x = x-x_pad
	y = y-y_pad
	print x,y

def start_game():
    #location of first menu
    mousePos((317,210))
    leftClick()
    time.sleep(.1)

    #location of second menu
    mousePos((317,391))
    leftClick()
    time.sleep(.1)

    #location of third menu
    mousePos((576,452))
    leftClick()
    time.sleep(.1)

    #location of fourth menu
    mousePos((335,373))
    leftClick()
    time.sleep(.1)

class Cord:

    f_shrimp = (35,343)
    f_rice = (88,334)
    f_nori = (40,387)
    f_roe = (82, 392)
    f_salmon = (38,440)
    f_unagi = (87, 430)
#-------------------------
    phone = (529,359)
    mat = (216,370)

    menu_toppings = (550,270)

    t_shrimp = (497,231)
    t_nori = (486,281)
    t_roe = (574,281)
    t_salmon = (497,338)
    t_unagi = (572,224)
    t_exit = (557,327)


    menu_rice = (542,291)
    buy_rice = (551,279)

    delivery_norm = (499,300)

    menu_sake = (532, 315)

foodOnHand = {
    'shirmp': 5,
    'rice': 10,
    'roe' : 10,
    'nori' : 10,
    'salmon': 5,
    'unagi': 5
}

sushiTypes = {
    2989:'caliroll',
    2516:'onigiri',
    2523:'gunkan'
}

class Blank: 
    seat_1 = 6434
    seat_2 = 5707
    seat_3 = 10387
    seat_4 = 10459
    seat_5 = 6806
    seat_6 = 7979

def clear_tables():
    mousePos((79,212))
    leftClick()

    mousePos((183,212))
    leftClick()

    mousePos((285,212))
    leftClick()

    mousePos((382,212))
    leftClick()

    mousePos((488,212))
    leftClick()

    mousePos((590,212))
    leftClick()
    time.sleep(1)

def foldMat():
    mousePos(Cord.mat)
    time.sleep(.1)
    leftClick()

def checkFood():
    for i,j in foodOnHand.items():
        if i == 'rice' or i == 'roe' or i == 'nori':
            if j<=3:
                print "%s is low and needs to be replenished" % i
                buyFood(i)
            else:
                print "Nothing is low"
                print "rice: " + str(foodOnHand['rice'])
                print "nori: " + str(foodOnHand['nori'])
                print "roe: " + str(foodOnHand['roe'])

"""
Recipes:
    Onigiri:
        2 Rice, 1 Nori 

    caliroll:
        1 Rice, 1 Nori, 1 Roe 

    Gunkan:
        1 Rice, 1 Nori, 2 Roe

"""

def make_food(food):
    if food == 'caliroll':
        print "Making California Roll"
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_nori)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_roe)
        leftClick()
        time.sleep(1)
        foldMat()
        foodOnHand['rice'] -= 1
        foodOnHand['nori'] -= 1
        foodOnHand['roe'] -= 1
        time.sleep(1.5)

    elif food == 'onigiri':
        print "Making onigiri"
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(.05)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_nori)
        leftClick()
        time.sleep(1)
        foldMat()
        foodOnHand['rice'] -= 2
        foodOnHand['nori'] -= 1
        time.sleep(1.5)

    elif food == 'gunkan':
        print "Making gunkan"
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_nori)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_roe)
        leftClick()
        time.sleep(.05)
        leftClick()
        time.sleep(1)
        foldMat()
        foodOnHand['rice'] -= 1
        foodOnHand['nori'] -= 1
        foodOnHand['roe'] -= 2
        time.sleep(1.5)

    else: "No match found"

##### ADD REST OF RECIPES Will get screenshots tomorrow

def buyFood(food):
    if food == 'rice':
        mousePos(Cord.phone)
        time.sleep(.1)
        leftClick()
        mousePos(Cord.menu_rice)
        time.sleep(.05)
        leftClick()
        s = screenGrab()
        if s.getpixel(Cord.buy_rice) != (127,127,127):
            print "Rice is avaiable"
            mousePos(Cord.buy_rice)
            time.sleep(.1)
            leftClick()
            mousePos(Cord.delivery_norm)
            time.sleep(.1)
            leftClick()
            foodOnHand['rice'] += 10
            time.sleep(2.5)
        else:
            print "Rice is NOT available"
            mousePos(Cord.t_exit)
            time.sleep(.1)
            leftClick()
            time.sleep(1)
            buyFood(food)

    elif food == 'nori':
        mousePos(Cord.phone)
        time.sleep(.1)
        leftClick()
        mousePos(Cord.menu_toppings)
        time.sleep(.05)
        leftClick()
        s = screenGrab()
        if s.getpixel(Cord.t_nori) != (33,30,11):
            print "Nori is available."
            mousePos(Cord.t_nori)
            time.sleep(.1)
            leftClick()
            mousePos(Cord.delivery_norm)
            time.sleep(.1)
            leftClick()
            foodOnHand['nori'] += 10
            time.sleep(2.5)
        else:
            print "Nori is NOT available."
            mousePos(Cord.t_exit)
            time.sleep(.1)
            leftClick()
            time.sleep(1)
            buyFood(food)

    elif food == 'roe':
        mousePos(Cord.phone)
        time.sleep(.1)
        leftClick()
        mousePos(Cord.menu_toppings)
        time.sleep(.05)
        leftClick()
        s = screenGrab()
        if s.getpixel(Cord.t_roe) != (101,13,13):
            print "Roe is available"
            mousePos(Cord.t_roe)
            time.sleep(.1)
            leftClick()
            mousePos(Cord.delivery_norm)
            time.sleep(.1)
            leftClick()
            foodOnHand['roe'] += 10
            time.sleep(2.5)
        else:
            print 'Roe is NOT available'
            mousePos(cord.t_exit)
            time.sleep(.1)
            leftClick()
            time.sleep(1)
            buyFood(food)

    elif food == 'shirmp':
        mousePos(Cord.phone)
        time.sleep(.1)
        leftClick()
        mousePos(Cord.menu_toppings)
        time.sleep(.1)
        leftClick()
        s=screenGrab()
        if s.getpixel(Cord.t_shrimp) != (127,52,6):
            print "Shrimp is available."
            mousePos(Cord.t_shrimp)
            time.sleep(0.1)
            leftClick()
            mousePos(Cord.delivery_norm)
            time.sleep(2.5)
            leftClick()
            foodOnHand['shrimp']+=5
        else: 
            print "Shirmp is NOT available"
            mousePos(t_exit)
            leftClick()
            time.sleep(2.5)
            buyFood(food)

    elif food == 'salmon':
        mousePos(Cord.phone)
        time.sleep(0.1)
        leftClick()
        time.sleep(0.1)
        mousePos(Cord.menu_toppings)
        time.sleep(0.1)
        leftClick()
        s = screenGrab()
        if s.getpixel(Cord.t_salmon) != (127,71,47):
            print "Salmon is available."
            mousePos(Cord.t_salmon)
            time.sleep(0.1)
            leftClick()
            mousePos(Cord.delivery_norm)
            time.sleep(2.5)
            leftClick()
            foodOnHand['salmon'] += 5
        else:
            print "Salmon is NOT available."
            mousePos(Cord.t_exit)
            time.sleep(2.5)
            leftClick()
            buyFood(food)

    elif food == 'unagi':
        mousePos(Cord.phone)
        time.sleep(0.1)
        leftClick()
        mousePos(Cord.menu_toppings)
        time.sleep(0.1)
        leftClick()
        s=screenGrab()
        if s.getpixel(Cord.t_unagi) != (127,71,47):
            print "Unagi is available."
            mousePos(Cord.t_unagi)
            time.sleep(0.1)
            leftClick()
            mousePos(Cord.delivery_norm)
            time.sleep(2.5)
            leftClick()
            foodOnHand['unagi'] += 5
        else:
            print "Unagi is NOT available"
            mousePos(Cord.t_exit)
            time.sleep(0.1)
            leftClick()
            time.sleep(2.5)
            buyFood(food)
    else:
        print "Unrecognizable food."

def get_seat_one():
    box = (x_pad+26,y_pad+61,x_pad+87,y_pad+75)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print a
    im.save(os.getcwd() + '\\seat_one__' + str(int(time.time())) + '.png', 'PNG')
    return a

def get_seat_two():
    box = (x_pad+127,y_pad+61,x_pad+188,y_pad+75)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print a
    im.save(os.getcwd() + '\\seat_two__' + str(int(time.time())) + '.png', 'PNG')
    return a

def get_seat_three():
    box = (x_pad+228,y_pad+61,x_pad+289,y_pad+75)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print a
    im.save(os.getcwd() + '\\seat_three__' + str(int(time.time())) + '.png', 'PNG')
    return a

def get_seat_four():
    box = (x_pad+329,y_pad+61,x_pad+390,y_pad+75)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print a
    im.save(os.getcwd() + '\\seat_four__' + str(int(time.time())) + '.png', 'PNG')
    return a

def get_seat_five():
    box = (x_pad+430,y_pad+61,x_pad+491,y_pad+75)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print a
    im.save(os.getcwd() + '\\seat_five__' + str(int(time.time())) + '.png', 'PNG')
    return a

def get_seat_six():
    box = (x_pad+531,y_pad+61,x_pad+592,y_pad+75)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print a
    im.save(os.getcwd() + '\\seat_six__' + str(int(time.time())) + '.png', 'PNG')
    return a

def get_all_seats():
    get_seat_one()
    get_seat_two()
    get_seat_three()
    get_seat_four()
    get_seat_five()
    get_seat_six()

def check_bubs():
    checkFood()
    s1 = get_seat_one()
    if s1 != Blank.seat_1:
        if sushiTypes.has_key(s1):
            print "Table 1 is occupied and needs %s" % sushiTypes[s1]
            make_food(sushiTypes[s1])
            checkFood()
        else: 
            print "Seat one is occupied and desires an unknown sushi type, recorded value is %s" % s1
    else: 
        print "Seat 1 is unoccupied."

    clear_tables()

    s2 = get_seat_two()
    if s2 != Blank.seat_2:
        if sushiTypes.has_key(s2):
            print "Seat two is occupied and nees %s" % sushiTypes[s2]
            make_food(sushiTypes[s2])
            checkFood()
        else:
            print "Seat two is occupied and desires an unknown sushi type, recorded value is: %s." % s2
    else:
        print "Seat two is unoccupied."

    clear_tables()

    s3 = get_seat_three()
    if s3 != Blank.seat_3:
        if sushiTypes.has_key(s3):
            print "Seat three is occupied and needs %s" % sushiTypes[s3]
            make_food(sushiTypes[s3])
            checkFood()
        else:
            print "Seat three is occupied and desires an unknown sushi type, recorded value is %s." % s3
    else:
        print "Seat three is unoccupied."

    clear_tables()

    s4 = get_seat_four()
    if s4 != Blank.seat_4:
        if sushiTypes.has_key(s4):
            print "Seat four is occupied and needs %s" % sushiTypes[s4]
            make_food(sushiTypes[s4])
            checkFood()
        else: 
            print "Seat four is occupied and desires an unknown sushi type, recorded value is %s." % s4
    else:
        print 'Seat four is unoccupied.'

    clear_tables()

    s5 = get_seat_five()
    if s5 != Blank.seat_5:
        if sushiTypes.has_key(s5):
            print "Seat five is occupied and needs %s." % sushiTypes[s5]
            make_food(sushiTypes[s5])
            checkFood()
        else: 
            print "Seat five is occupied and desires an unknown sushi type, recorded value is %s" % s5
    else:
        print "Seat five is unoccupied."

    clear_tables()

    s6 = get_seat_six()
    if s6 != Blank.seat_6:
        if sushiTypes.has_key(s6):
            print "Seat six is occupied and needs %s." % sushiTypes[s6]
            make_food(sushiTypes[s6])
            checkFood()
        else:
            print "Seat six is occupied and desires an unknown sushi type, recorded value is %s." % s6
    else:
        print "Seat six is unoccupied"

    clear_tables()

def main():
    start_game()
    for i in range(100):
    #while True:
        check_bubs()
