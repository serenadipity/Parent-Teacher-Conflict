from re import search

def valid_data(username, password, repeat_password, email, users):
    usernames = []
    emails = []
    for user in users:
        usernames.append(user[0])
        emails.append(user[1])
    if username in usernames:
        return [False, "Username is already taken."]
    if email in emails:
        return [False, "Email is already used."]
    if password != repeat_password:
        return [False, "Passwords do not match."]
    if len(password) < 8:
        return [False, "Your password must be at least 8 characters."]
    if not (bool(search(r'\d', password)) and bool(search('[a-z]', password)) and bool(search('[A-Z]', password)) and bool(search(r'[!@#$%^*]', password))):
        return [False, "Your password must include a lowercase letter, an uppercase letter, a number, and at least of one the following symbols: '!@#$%^*'."]
    return [True, "Your information has been validated."]


#[[PID, TIME, SECTION #, F, L]]
def createSchedule(listOfThings):
    if not(listOfThings and listOfThings[0]):
        return ""
    hour = 5
    minutes = 30
    if listOfThings[0][1] == 'afternoon':
        hour = 1
        minutes = 0
    stuffToWorkWith = {}
    for alist in listOfThings:
        stuffToWorkWith[alist[2]] = alist[3:]
    stringer = ""
    stringer += "<table id='inner'>\n"
    stringer += "<tr> <th id='inner_row'> TIME </th> <th id='inner_row'> Name </th> </tr>\n"
    for counter in range(50):
        stringer += "<tr>"
        a = (hour + (minutes + counter * 3) / 60) / 10
        b = (hour + (minutes + counter * 3) / 60) % 10
        c = (minutes + counter * 3) % 60 / 10
        d = (minutes + counter * 3) % 60 % 10
        stringer += "<td id='inner_row'> %d%d:%d%d </td>" % (a, b, c, d)
        addition = "<td id='inner_row'></td>"
        if counter in stuffToWorkWith.keys():
            addition = "<td id='inner_row'> %s %s </td>" % (stuffToWorkWith[counter][0], stuffToWorkWith[counter][1])
        stringer += addition
        stringer += "</tr>\n"
    stringer += "</table\n"
    return stringer


def thingToDo(dictOfThings, date, time):
    TID = dictOfThings.keys()
    cleanData = {}

    if not (dictOfThings and dictOfThings.keys()):
        return ""
    
    hour = 5
    minutes = 30
    if time == 'afternoon':
        hour = 1
        minutes = 0
    stringer = "<form><table id='inner'>\n"
    stringer += '<input type="hidden" name="time" value="%s">\n' % (time)
    stringer += '<input type="hidden" name="date" value="%s">\n' % (date)
    stringer += "<tr> <th id='inner_row'> TIME </th> <th id='inner_row'> N/A </th>"
    for key in TID:
        stringer += "<th> %s %s </th>" % (dictOfThings[key][0], dictOfThings[key][1])
        stuffToWorkWith = {}
        for alist in dictOfThings[key][3:]:
            stuffToWorkWith[alist[2]] = alist[3:]
        cleanData[key] = stuffToWorkWith
    stringer += "</tr>"
    for counter in range(50):
        stringer+= "<tr>"
        a = (hour + (minutes + counter * 3) / 60) / 10
        b = (hour + (minutes + counter * 3) / 60) % 10
        c = (minutes + counter * 3) % 60 / 10
        d = (minutes + counter * 3) % 60 % 10
        stringer += "<td id='inner_row'> %d%d:%d%d </td>" % (a, b, c, d)
        addition = "<td id='inner_row'> <input type='radio' name='%s' value='-1' checked> </td>" % (counter)
        for key in TID:
            if counter in cleanData[key].keys():
                addition += "<td id='inner_row'> %s %s </td>" % (cleanData[key][counter][0], cleanData[key][counter][0])
            else:
                addition += "<td id='inner_row'><input type='radio' name='%s' value='%s'></td>" % (counter, key)
        stringer += addition + "</tr>\n"
    stringer += "</table> <input type='submit' value='Schedule'> </form>"
    return stringer

