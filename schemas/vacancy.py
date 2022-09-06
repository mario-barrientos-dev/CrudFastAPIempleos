def vacancyUp(aplication)->dict:
         return {
                 "id": str(aplication["_id"]),
                "VacancyId": aplication["VacancyId"],
                "PositionName": aplication["PositionName"],
                "CompanyName": aplication["CompanyName"],
                "Salary": aplication["Salary"],
                "Currency": aplication["Currency"],
                "VacancyLink": aplication["VacancyLink"],
                "RequiredSkills": aplication["RequiredSkills"]
                        
                           
        }

def vacanciesUp(users) -> list:
       return [vacancyUp(aplication) for aplication in users]