import mysql.connector
from mysql import connector
class student:
    def __init__(self):
        self.connection=connector.connect(
        host="localhost",
        user="root",
        password="Angel@1234",
        database="student_db"
        )

        print("connection successfullly----")

    def post(self, **kwargs):
        try:
            self.cursor = self.connection.cursor()
            query = "insert into student(name,course,phone,city)values(%s,%s,%s,%s)"
            values = [v for v in kwargs.values()]
            self.cursor.execute(query, values)
            self.connection.commit()
            print("student details added successfully----")
        except Exception as e:
            print(e)
obj=student()
obj.post(name="suraj",course="data analytics",phone="987645632",city="kochi")
obj.post(name="anu",course="software testing",phone="214567345",city="kallor")
obj.post(name="priya",course="software testing",phone="73458654",city="pala")
obj.post(name="paru",course="python",phone="98456345267",city="pala")
obj.post(name="lila",course="python",phone="234345578",city="ponkunnma")
