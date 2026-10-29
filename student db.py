
import mysql.connector
from datetime import datetime


class student:
    def __init__(self):
        try:
            self.connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Angel@1234",
                database="student_db"
            )
            print("Connection successful!")

        except Exception as e:
            print(e)
            self.connection = None


    def post(self, **kwargs):
        try:
            if self.connection is None:
                return

            self.cursor = self.connection.cursor()

            query = """
                INSERT INTO student (name, course, phone, city)
                VALUES (%s, %s, %s, %s)
            """

            values = (
                kwargs["name"],
                kwargs["course"],
                kwargs["phone"],
                kwargs["city"]
            )

            self.cursor.execute(query, values)
            self.connection.commit()

            print("Student details added successfully!")

        except Exception as e:
            print(e)

        finally:
            if hasattr(self, "cursor"):
                self.cursor.close()

    def get(self):
        try:
            if self.connection is None:
                return

            self.cursor = self.connection.cursor()
            self.cursor.execute("SELECT * FROM student")

            records = self.cursor.fetchall()

            for record in records:
                print(record)

        except Exception as e:
            print(e)

        finally:
            if hasattr(self, "cursor"):
                self.cursor.close()


    def get_object(self, id):
        try:
            if self.connection is None:
                return None

            self.cursor = self.connection.cursor()
            query = "SELECT * FROM student WHERE id = %s"

            self.cursor.execute(query, (id,))
            record = self.cursor.fetchone()

            print(record)
            return record

        except Exception as e:
            print(e)
            return None

        finally:
            if hasattr(self, "cursor"):
                self.cursor.close()


    def put(self, id, **kwargs):
        try:
            if self.connection is None:
                return

            if not kwargs:
                print("Enter details to update.")
                return

            allowed_columns = {"name", "course", "phone", "city"}

            for key in kwargs:
                if key not in allowed_columns:
                    raise ValueError(f"Invalid column: {key}")

            self.cursor = self.connection.cursor()

            columns = ", ".join(
                f"{key} = %s" for key in kwargs
            )

            values = list(kwargs.values())
            values.append(id)

            query = f"UPDATE student SET {columns} WHERE id = %s"

            self.cursor.execute(query, values)
            self.connection.commit()

            if self.cursor.rowcount > 0:
                print("Student details updated successfully!")
            else:
                print("Student not found or no changes made.")

        except Exception as e:
            print(e)

        finally:
            if hasattr(self, "cursor"):
                self.cursor.close()


    def delete(self, id):
        try:
            if self.connection is None:
                return

            self.cursor = self.connection.cursor()

            query = "DELETE FROM student WHERE id = %s"
            self.cursor.execute(query, (id,))
            self.connection.commit()

            if self.cursor.rowcount > 0:
                print("Student deleted successfully!")
            else:
                print("Student not found!")

        except Exception as e:
            print(e)

        finally:
            if hasattr(self, "cursor"):
                self.cursor.close()


    def close(self):
        if self.connection is not None and self.connection.is_connected():
            self.connection.close()
            print("Database connection closed!")


obj = student()

if obj.connection is not None:


    obj.post(
        name="Suraj",
        course="Data Analytics",
        phone="987645632",
        city="Kochi"
    )

    obj.post(
        name="Anu",
        course="Software Testing",
        phone="214567345",
        city="Kollam"
    )

    obj.post(
        name="Priya",
        course="Software Testing",
        phone="773458654",
        city="Pala"
    )

    obj.post(
        name="Paru",
        course="Python",
        phone="9845634567",
        city="Pala"
    )

    obj.post(
        name="Lila",
        course="Python",
        phone="234345578",
        city="Ponkunnam"
    )


    print("\nAll students:")
    obj.get()


    print("\nSingle student:")
    obj.get_object(1)


    obj.put(1, city="Thiruvananthapuram", course="Python")


    obj.delete(1)

    obj.close()
