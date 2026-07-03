if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    
    all_scores = []
    for student in students:
        all_scores.append(student[1])
        
    unique_scores = sorted(list(set(all_scores)))
    second_lowest_score = unique_scores[1]

    second_lowest_students = []
    for student in students:
        if student[1] == second_lowest_score:
            second_lowest_students.append(student[0])
            
    second_lowest_students.sort()
    for name in second_lowest_students:
        print(name)
