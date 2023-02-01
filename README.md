# Time_management_mac_test
POST
/admin/user/    ----> Registeration 
  body -> {
              "username":"_______",
              "password":"_______"
          }
          
POST
/admin/login/
  body -> {
              "username":"_______",
              "password":"_______"
          }
          
POST
/faculty/user/    --> Registeration
  body -> {
              "username":"________",
              "password":"________"
          }
POST
/faculty/login/
   body -> {
              "username":"________",
              "password":"________"
          }
          
          
POST
/admin/branch/  -----> Registeration  Token required
    body  -> {
                "name":"______",
                "place":"_____"
            }
            
            
POST 
/admin/branch_manager/<id>/  ---> branch manager assign (id=id of branch, name=name of employee)
    body  -> {
                "name":"______"
            }
            
            
POST
/admin/batch/  --> creating batch to branch name = name of the batch id = id of the branch
    body  ->{
            "id":"_______",
            "name":"_______"
            }
            
            
POST
/admin/course/   -----> Creating course name = name of the course

      body -> {
                  "name":"______"
              }


PUT
/admin/branch/ -----> assinging course to branch

    body -> {
                "branch_id":"____________",
                "course_id":"____________"
            }


POST
/admin/subject/
      body --> {
                  "name":"_______"
              }
              
              
PUT
/admin/course/
    body -->{
                "subject_id":"_________________________",
                "course_id":"__________________________"
            }
            
            
POST
/admin/topic/
      body -->{
                  "name":"______"
              }


PUT
/admin/subject/
      body -->{
                  "topic_id":"___________________________",
                  "subject_id":"__________________________"
              }
              
              
POST
/admin/subtopic/
    body -->{
                "name":"subt1"
            }
            
            
PUT
/admin/topic/
    body -->{
                "topic_id":"_____________________________",
                "subtopic_id":"____________________________"
            }
            
            
GET
/admin/fac/ ---> LIst the faculty for verify


PUT
/admin/facverify/<id>/ ---> Verify the Faculty id= id of the faculty

DELETE
/admin/facreject/<id>/  --> Reject Verify Request


POST
/admin/addfac/ --> admin add faculty
    body-->{
              "username":"________",
              "password":"_________"
          }



    
