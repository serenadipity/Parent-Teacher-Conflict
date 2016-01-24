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
    stringer += "<table>\n"
    stringer += "<tr> <th> TIME </th> <th colspan='2'> Name </th> </tr>\n"
    for counter in range(50):
        stringer += "<tr>"
        a = (hour + (minutes + counter * 3) / 60) / 10
        b = (hour + (minutes + counter * 3) / 60) % 10
        c = (minutes + counter * 3) / 10
        d = (minutes + counter * 3) % 10
        stringer += "<td> %d%d:%d%d </td>" % (a, b, c, d)
        addition = "<td></td><td></td>"
        if counter in stuffToWorkWith.keys():
            addition = "<td> %s </td><td> %s </td>" % (stuffToWorkWith[counter][0], stuffToWorkWith[counter][1])
        stringer += addition
        stringer += "</tr>\n"
    stringer += "</table\n"
    return stringer
