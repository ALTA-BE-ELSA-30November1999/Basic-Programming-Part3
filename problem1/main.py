# input
student_score = 80

# Process: Your Solution Code Here
if student_score > 100 :
    print ("Invalid Nilai")
else :
    if student_score < 34 :
        print ("Nilai D")
    elif 35 <= student_score <= 49 :
        print ("Nilai C")
    elif 50 <= student_score <= 64 :
        print ("Nilai B")
    elif 65 <= student_score <= 79 :
        print ("Nilai B+")
    else :
        print ("Nilai A")

# Output "Nilai A"