    sellesson = ClassesIDList.get(sellesson)
    jsondata = {'Data.Mail': username,                  # '.....@std.yildiz.edu.tr'
                'Data.Password': password,              # '.....'
                'RememberMe': 'false'}
    url = "https://online.yildiz.edu.tr/Account/Login"
    response = requests.post(url, data=jsondata)
    ses = response.cookies
    url = "https://online.yildiz.edu.tr/ViewOnlineLessonProgramForStudent/ListAttendance"
    jsondata = {'Data[LessonProgramNo]': sellesson}
    response = requests.post(url, data=jsondata, cookies=response.cookies)
    print("Selected Lesson ID: ", sellesson)
    substr = response.text
    zlid = 0
    for i in range(len(substr)):
        if(substr[i:i+70] == ".EDU.LessonProgram.ViewOnlineLessonProgramAttendanceForStudent.start('"):
            zlid = substr[i+70:i+140-55-9]
            break
    print("Zoom List ID: ", zlid)
    url = "https://online.yildiz.edu.tr/ViewOnlineLessonProgramForStudent/Watch"
    jsondata = {'Data[No]': zlid}
    response = requests.post(url, data=jsondata, cookies=ses)
    substr = response.text
    zoomlink = ""
    for i in range(len(substr)):
        if(substr[i:i+24] == "https://zoom.us/rec/play"):
            zoomlink = substr[i:i+123]
            break
    print(zoomlink)
