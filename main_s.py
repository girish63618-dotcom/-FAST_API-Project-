from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
app = FastAPI()

students ={
"S001" :{"name":"RavI", "marks":85, "grade":"A"},
"S002" :{"name":"Priya", "marks":75, "grade":"B"},
"S003" :{"name":"arjun", "marks":91, "grade":"A+"}
}

#input schema
class marksSubmission(BaseModel):
    student_id : str
    marks : int
    subject : str

@app.get("/{student_id}")
def get_student(student_id: str):

    if student_id not in students:
        raise HTTPException(
             status_code=404,
             detail=f"student with id {student_id} does not exists"
        )
    return students[student_id]

@app.post("/submit-marks")
def submit_marks(submission:marksSubmission):

    #error 1 student does not exists
    if submission.student_id not in students:
         raise HTTPException(
                     status_code=404,
                     detail=f"student with id {studen_id} does not exists"
                )

 #error 2 valid range 0 -200
    if submission.marks < 0 or submission.marks >100:
     raise HTTPException(
                 status_code=400,
                 detail={
                     "error":"marks must be between  0 and 100",
                     "marks_received":submission.marks,
                     "fix":"enter a valid value  between 0 and 109"
                 }
    )


    #error 3 subject name empty
    if submission.subject.strip()=="":
        raise HTTPException(
                             status_code=404,
                             detail=f"subject name cannot be empty"
        )

    student[submission.student_id]["marks"] = submission.marks
    return {
        "message":"marks submitted successfully",
        "student":students[submission.student_id]["name"],
        "subject":submission.subject,
        "marks":submit_marks,
    }
     
