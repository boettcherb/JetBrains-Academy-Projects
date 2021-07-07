accepted = [[], [], [], [], []]
considered = [[], [], [], [], []]
majors = {"Biotech": 0, "Chemistry": 1, "Engineering": 2,
          "Mathematics": 3, "Physics": 4}
          
max_applicants = int(input())
applicants = []
with open("applicants.txt", "r") as f:
    for line in f:
        first, last, gpa, m1, m2, m3 = line.split()
        name = first + " " + last
        applicants.append((name, float(gpa), [m1, m2, m3]))

for priority in range(3):
    for applicant in applicants:
        major = applicant[2][priority]
        considered[majors[major]].append(applicant)
    for field in range(5):
        considered[field].sort(key=(lambda a: a[0]))
        considered[field].sort(key=(lambda a: a[1]), reverse=True)
        max_considered = max_applicants - len(accepted[field])
        while len(considered[field]) > max_considered:
            considered[field].pop()
        accepted[field].extend(considered[field])
        for applicant in considered[field]:
            applicants.remove(applicant)
        considered[field].clear()

for major in majors:
    major_index = majors[major]
    accepted[major_index].sort(key=(lambda a: a[0]))
    accepted[major_index].sort(key=(lambda a: a[1]), reverse=True)
    print(major)
    for applicant in accepted[major_index]:
        print(applicant[0], applicant[1])
    print()
