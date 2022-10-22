cookies, sugear, butter, flour = 0.0, 0.0, 0.0, 0.0

COOKIES_RECIPE, SUGAR_RECIPE, BUTTER_RECIPE, FLOUR_RECIPE=48.0, 1.5, 1.0, 2.75

cookies=float(input("Enter the number of cookies:"))
sugar=(cookies*	SUGAR_RECIPE)/COOKIES_RECIPE
butter=(cookies*BUTTER_RECIPE)/COOKIES_RECIPE
flour=(cookies*FLOUR_RECIPE)/COOKIES_RECIPE

print("To make",cookies,"cookies,you will need:")
print(format(sugar,'2f'),"cups of sugar")
print(format(butter,'2f'),"cups of butter")
print(format(flour,'2f'),"cups of flour")