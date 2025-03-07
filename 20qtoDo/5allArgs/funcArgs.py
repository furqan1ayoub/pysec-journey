def allArgs(name, age=15, *rollNos, **Studentdetails):
    print(f"Your Name is {name} & Your Age is {age}")
    print(f"Total Roll-Nos in class - ", rollNos)
    print(f"Class Details -", Studentdetails)

# Example call to the function
allArgs("furqan", 15, 55, 52, 51, 50, className="10th", section="Pink", school="Rp")