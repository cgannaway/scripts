def calcbmi():
    name, dob, height, weight = raw_input('''Enter your first name, Date of birth(mm/dd/yy), Height in inches, and weight pounds seperated by spaces: ''').split()
    height, weight = [int(height), int(weight)]
    bmi = (weight*703)/(height*height)
    if bmi >= 30:
        print ("hello %s, your DoB is %s, you are %s inches and %s lbs, and your BMI is %s. You are overweight " % (name, dob, height, weight, bmi))
    else:
        print ("hello %s, your DoB is %s, you are %s inches and %s lbs, and your BMI is %s " % (name, dob, height, weight, bmi))


calcbmi()
