def gradingStudents(grades):
    # Write your code here
    for i, grade in enumerate(grades):
        if grade >= 38:
            mod = grade % 5
            if mod >= 3:
                grade = grade + 5 - mod
        
        grades[i] = grade
        
    return grades
            
