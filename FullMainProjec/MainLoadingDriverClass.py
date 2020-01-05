from FullMainProjec.ElderCLass import Elder
from FullMainProjec.TrustedPeople import getPermission
from FullMainProjec.YoungPeopleCLass import Young

young = []
elder = []
Young_takingCare_of = dict()


def Registration():
    while True:
        print("**********************************************************************************")
        print("**************************registering *********************************************")

        types, name = input("Enter whether you are young or adult with your name type E for elder and Y for young with "
                            "comma separated").split(",")

        if types == "E":
            for data in elder:
                if data.get_Name() == name:
                    name = data

            if name not in elder:
                print("You are the elder hence get me details of elder")
                name = Elder(name)
                name.set_Age(int(input(" Enter the Age of elder ")))
                name.set_Funds(int(input(" Enter your funds ")))
                elder.append(name)
            else:
                print(" You had already Registered so please wait for finding the suitable rented ")
        if types == "Y":
            for data in young:
                if data.get_Name() == name:
                    name = data
            if name not in young:
                name = Young(name)
                name.set_Age(int(input("Enter the age of the young")))
                young.append(name)
            else:
                if name.No_Of_Elders < 5:
                    displayElder()
                    print("Choose the elder name from the above available list ")
                    nam = input()
                    for data in elder:
                        if data.get_Name() == nam:
                            nam = data
                    if nam not in elder:
                        print("You had typo mistakes  please check it")
                    else:
                        checkElder(nam)
                        permit = getPermission(name)
                        if permit:
                            if Young_takingCare_of.get(name.get_Name()) is None:
                                Young_takingCare_of[name.get_Name()] = [nam.get_Name()]
                            else:
                                Young_takingCare_of[name.get_Name()].append(nam.get_Name())
                            name.No_Of_Elders += 1
                            nam.isAvailable = False
                            # setting the reviews of the elder
                            nam.set_Ratings(int(input("Give the ratings to the hired Young")))
                            nam.set_Reviews_Elder(nam, input("Enter the Review for the elder"))
                            name.set_Rating(int(input("Enter the ratings for the elder")))
                            name.set_Reviews(name, input("Enter the reviews of the Young people"))

        # print("The number of Elders regestered is the ", elder)
        # print("The young peoples registered is the ", young)

        if input("Enter would you like to enter again ") == 'y':
            continue
        else:
            break
        pass


def displayElder():
    print("People available for the rent is the ")
    for data in elder:
        if data.is_Available:
            print("Name : ", data.get_Name())
            print("Ratings: ", data.get_Ratings())
            print("Funds is :", data.get_Funds())


def checkElder(eld):
    if eld in elder:
        print("Discription of the elder is the ")
        print("Name: ", eld.get_Name())
        print("Age: ", eld.get_Age())
        print("Funds: ", eld.get_Funds())
        print("Reviews: ", eld.get_Reviews())
        print("Ratings :", eld.get_Ratings())


def whoIsTakingCare(couple):
    for i, data in Young_takingCare_of.items():
        for items in data:
            if items == couple.get_Name():
                return i


def NumberOfOldPeopleTakingCareOf():
    return Young_takingCare_of


def main():
    print("***************************************************************")
    Registration()

    print("***************************************************************")
    print("*************those who is checking ls ***********************")
    print("all those is taking care of are the ")
    print("for who is taking care of the elder is the ")
    name = input("Enter the elder you want to check ")
    for data in elder:
        if data.get_Name() == name:
            name = data
    else:
        print("No such elder is here ")
    print(whoIsTakingCare(name))

    print("***************************************************************************")
    print("********* all the people who is taking care of  are ************************")

    print("All the number of people that the elder is taking care is the ")
    print(NumberOfOldPeopleTakingCareOf())
    pass


if __name__ == '__main__':
    main()
    pass
