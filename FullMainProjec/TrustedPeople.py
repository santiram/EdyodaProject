def checking(young):
    print("****************************************************************")
    print("***************checking****************************")
    print("The name of the young those who want to take care of your parents is the ")
    print(young.get_Name())
    young.get_Reviews()
    print("The number of adult he is taking care is the ", young.No_Of_Elders)
    print("The ratings of th adult is the ", young.get_Ratings())
    print("Please Enter the permission in yes or no ")
    if input().strip() == 'yes':
        return True
    else:
        return False


def getPermission(young):
    return checking(young)
