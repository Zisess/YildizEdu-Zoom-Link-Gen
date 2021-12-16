**version:** `basic` (🎉)

## YILDIZ EDU - ..

This application is the basic of automated online-class-joiner(for YıldızEdu) within the right time. <br>
Gets the ZOOM link by scheduled date and time. 

![image](https://user-images.githubusercontent.com/84146574/146395856-01576f52-da40-4979-801d-d230c2f4f217.png)

## POST Details

| Log | In |
| - | - |
| online.yildiz.edu.tr | './Account/Login' |
| REQUEST_METHOD | 'POST' |
| 'Data.Mail' | 'username' |
| 'Data.Password' | 'password' |
| 'RememberMe' | 'false' |

| Method | Description |
--------- | -------- |
[PHI.UI.Transaction.execute('Information', '/Account/Login', null, function (n)](https://online.yildiz.edu.tr/Account/Login) | Log In
[PHI.UI.Transaction.merge('details', '/ViewOnlineLessonProgramForStudent/ListAttendance'](https://online.yildiz.edu.tr/ViewOnlineLessonProgramForStudent/ListAttendance) | Gets the List Of Lessons/Classes
[PHI.UI.Transaction.popuplg('Ders Kayıtları', '/ViewOnlineLessonProgramForStudent/Watch'](https://online.yildiz.edu.tr/ViewOnlineLessonProgramForStudent/Watch) | Classes Records 


## Usage

##### ..//ViewOnlineLessonProgramForStudent/.
```js

LMS.EDU.LessonProgram.ViewOnlineLessonProgramForStudent = {
  start: function (n) {
    PHI.UI.Transaction.init('LMS.EDU.LessonProgram.ViewOnlineLessonProgramForStudent', {
      onLoad: function () {
        LMS.EDU.LessonProgram.ViewOnlineLessonProgramForStudent.view(n)
      },
      actions: [
      ]
    })
  },
  view: function (n) {
    PHI.UI.Transaction.load('/ViewOnlineLessonProgramForStudent/View', {
      Data: {
        No: n
      }
    }, function (t) {
      t.IsSuccess && LMS.EDU.LessonProgram.ViewOnlineLessonProgramForStudent.listAttendance(n);
      PHI.UI.Transaction.hideHeaderAndFooter()
    })
  },
  listAttendance: function (n) {
    PHI.UI.Transaction.merge('details', '/ViewOnlineLessonProgramForStudent/ListAttendance', {
      Data: {
        LessonProgramNo: n
      }
    }, function () {
    })
  },
  attend: function (n, t, i, r) {
    PHI.UI.Transaction.call('/ViewOnlineLessonProgramForStudent/Attend', {
      Data: {
        LessonProgramDetailNo: n,
        LessonProgramNo: t,
        StartTime: i,
        EndTime: r
      }
    }, function (n) {
      PHI.UI.Transaction.isMobileOrTablet() ? window.location.href = n.ScriptBag.RoomTypeId.toUpperCase() == '99A01A60-23B6-491E-902D-739388551E0D' ? n.ScriptBag.StudentJoinUrl + '?session=' + n.ScriptBag.Cookie : n.ScriptBag.StudentJoinUrl : n.ScriptBag.RoomTypeId.toUpperCase() == '99A01A60-23B6-491E-902D-739388551E0D' ? window.open(n.ScriptBag.StudentJoinUrl + '?session=' + n.ScriptBag.Cookie, 'Breeze', 'toolbar=no,menubar=no,width=800,height=600,resizable=yes') : window.open(n.ScriptBag.StudentJoinUrl)
    })
  },
  watch: function (n) {
    PHI.UI.Transaction.popuplg('Ders Kayıtları', '/ViewOnlineLessonProgramForStudent/Watch', {
      Data: {
        No: n
      }
    }, [
    ], function () {
    })
  }
};
```

##### ../Cockpit/ViewCockpit/.

```js

view: function () {
    PHI.UI.Transaction.load('/Cockpit/ViewCockpit', null, function (n) {
      PHI.UI.Transaction.refreshCalendar('event-calendar', 'detail', n.ScriptBag.Events, function (t) {
      
        t.type == 'Lesson Program' && (n.Account.Roles.toUpperCase().includes('4F17F639-335A-4CDF-9DB5-09B67C72D8B6') ?
        LMS.EDU.LessonProgram.ViewOnlineLessonProgramForStudent.start(t.no) : LMS.EDU.LessonProgram.ViewOnlineLessonProgramForInstructor.start(t.no));
        
        t.type == 'Meeting' && LMS.EDU.Meeting.ViewMeeting.start(t.no);
        
        t.type == 'Evaluation' && (n.Account.Roles.toUpperCase().includes('4F17F639-335A-4CDF-9DB5-09B67C72D8B6') ?
        LMS.EDU.Evaluation.ListEvaluationForStudent.start(t.no) : LMS.EDU.Evaluation.ListEvaluation.start(t.no))
        
      });
      PHI.UI.Transaction.hideHeaderAndFooter()
    });
    var n = 300,
    t = setInterval(function () {
      n = n - 1;
      n == 0 && LMS.CORE.Cockpit.ViewCockpit.isNewSession();
      n < 0 && (n = 300)
    }, 1000)
  },

´´´
