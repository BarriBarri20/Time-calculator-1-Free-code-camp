def add_time(s, d, day=""):
    listOfDays = ["sunday", "monday", "tuesday",  "wednesday", "thursday", "friday" ,"saturday"]
    t, e = s.split()
    h, m = t.split(":")
    h1, m1 = d.split(":")  
    h, h1, m, m1 = int(h), int(h1), int(m), int(m1)
    nd = h1 // 24
    nh = h1 - (h1 // 24)*24
    nm = m1  
    if e == "PM" :
        h+=12
    h += nh
    m += nm
    
    nd += h // 24
    nh = h - (h // 24)*24 + m // 60
    nm = m - (m // 60)*60
 
    if nd == 0 :
        s = ""
    elif nh == 24 :
        s = " ("+str( nd + 1 )+" days later)"

    elif nd == 1 :
        s = " (next day)"
    elif nd > 1 : 
        s = " ("+str(nd)+" days later)"
    if nd > 1 or h1 ==24 and m1 == 0 :
        if day.lower() in listOfDays : 
            dayName = listOfDays[ ( nd + listOfDays.index(day.lower()))%7  ].capitalize()
    elif nd == 1 : 
        if day.lower() in listOfDays : 
            dayName = listOfDays[ ( nd + listOfDays.index(day.lower()) + 1 )%7  ].capitalize()

    else :
        dayName = (day.lower()).capitalize()
        
    if day.lower() in listOfDays :
        if nh == 24 :
            return str(nh - 12) + ":" + str(nm).zfill(2) + " AM," + " "+ dayName + s
        if nh == 12 :
            return str(nh) + ":" + str(nm).zfill(2) + " PM" + s
        if nh >= 12 :
            return str(nh - 12) + ":" + str(nm).zfill(2) + " PM," + " " + dayName + s
        else :
            return str(nh) + ":" + str(nm).zfill(2) + " AM, " + dayName + s
    else : 
        if nh == 24 :
            return str(nh - 12) + ":" + str(nm).zfill(2)  + " AM" + s
        if nh == 12 :
            return str(nh) + ":" + str(nm).zfill(2) + " PM" + s
        if nh > 12 :
            return str(nh - 12) + ":" + str(nm).zfill(2) + " PM" + s
        else :
            return str(nh) + ":" + str(nm).zfill(2) + " AM" + s
