# From the given list calculate total scores.

student_scores = ['Alex| 75 50 90 80 90 70',
                  'Mary| 76 72 71 68 85 69',
                  'John|69 67 68 71 68 67',
                  'Anne|80 69 59 82 71 81',
                  'Mark|79 81 74 71 69 73']


def student_total_scores(stud_scores):
    for item in stud_scores:
        f, s = item.split("|")
        print(item)
        print(f, sum(map(int, s.split())))         


student_total_scores(student_scores)
