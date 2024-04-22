def MealsCountIterative(MealOption1 , MealOption2):
    # DECLARE MealOption : INTEGER
    # DECLARE MoreMeals : BOOLEAN
    MoreMeals = True
    while MoreMeals:
        MealOption = int(input("Enter meal option (1 or 2): "))
        if MealOption == 1:
            MealOption1 += 1
        elif MealOption == 2:
            MealOption2 += 1
        else:
            print(MealOption1 , " " , MealOption2)
            MoreMeals = False
        # ENDIF
    # ENDWHILE
# ENDFUNCTION

def MealsCountRecursive(MealOption1, MealOption2):
    MealOption = int(input("Enter meal option (1 or 2): "))

    if MealOption == 1:
        MealOption1 += 1
    elif MealOption == 2:
        MealOption2 += 1
    else:
        print(MealOption1, MealOption2)
        return

    MealsCountRecursive(MealOption1, MealOption2)

MealOption1 = 0
MealOption2 = 0

MealsCountIterative(MealOption1, MealOption2)
print("------------------------------------")
MealsCountRecursive(MealOption1, MealOption2)