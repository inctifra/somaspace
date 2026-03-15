import random

from faker.providers import BaseProvider


class DegreeCourseProvider(BaseProvider):
    degrees = [
        "Bachelor of Science",
        "Bachelor of Arts",
        "Bachelor of Pharmacy",
        "Bachelor of Nursing",
        "Bachelor of Medicine",
        "Bachelor of Commerce",
        "Bachelor of Education",
        "Diploma",
        "Higher Diploma",
    ]

    fields = [
        "Computer Science",
        "Information Technology",
        "Pharmacy",
        "Nursing",
        "Clinical Medicine",
        "Public Health",
        "Business Administration",
        "Economics",
        "Electrical Engineering",
        "Civil Engineering",
        "Mechanical Engineering",
        "Education",
        "Law",
        "Biotechnology",
    ]

    def degree_course(self):
        degree = random.choice(self.degrees)
        field = random.choice(self.fields)
        return f"{degree} in {field}"
