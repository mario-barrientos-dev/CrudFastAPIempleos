def userAplication(aplication)->dict:
         return {
                "id": str(aplication["_id"]),
                "UserId": aplication["UserId"],
                "FirstName": aplication["FirstName"],
                "LastName": aplication["LastName"],
                "Email": aplication["Email"],
                "YearsPreviousExperience": aplication["YearsPreviousExperience"],
                "Skills": aplication["Skills"]
                        
                           
        }

def usersAplications(users) -> list:
       return [userAplication(aplication) for aplication in users]