edad = int(input("Edad: "))
tiene_dpi = input("Tiene DPI?: (s/n)").lower()

#AND
if edad >= 18 and tiene_dpi == "s":
    print("Bienvenido, puedes entrar")
elif edad >= 18 and tiene_dpi == "n":
    print("Vale, tienes 18, pero no traes DPI. Te dejaremos entrar")
elif not(edad >= 18 and tiene_dpi == "s"):
    print("No puedes entrar")

