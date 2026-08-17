subj1 = int(input("Enter the marks of Subject 1: "))
subj2 = int(input("Enter the marks of Subject 2: "))
subj3 = int(input("Enter the marks of Subject 3: "))
subj4 = int(input("Enter the marks of Subject 4: "))
subj5 = int(input("Enter the marks of Subject 5: "))

def result():
    total = subj1+subj2+subj3+subj4+subj5
    average = total/500
    per = average*100

    print("=================Reults===================")
    print(f"Subject 1 : {subj1}")
    print(f"Subject 2 : {subj2}")
    print(f"Subject 3 : {subj3}")
    print(f"Subject 4 : {subj4}")
    print(f"Subject 5 : {subj5}")
    print(f"Total Marks : {total}")
    print(f"Average : {average}")
    print(f"Percentage : {per}")
    if(per>=80):
        print("Grade A")
    elif(per>=70):
        print("Grade B")
    elif(per>=60):
        print("Grade C")
    elif(per>=40):
        print("Grade D")
    else:
        print("Failed")
        
result()
