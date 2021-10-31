from student_director import AGradeStudentDirector, BGradeStudentDirector, \
    CGradeStudentDirector, DGradeStudentDirector

if __name__ == '__main__':
    ExcellentStudent = AGradeStudentDirector.construct()
    VeryGoodStudent = BGradeStudentDirector.construct()
    GoodStudent = CGradeStudentDirector.construct()
    BadStudent = DGradeStudentDirector.construct()

    print(ExcellentStudent)
    print(VeryGoodStudent)
    print(GoodStudent)
    print(BadStudent)
