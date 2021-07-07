def find_mean_score(applicant):
    tests = ((0, 1), (1,), (2, 3), (2,), (0, 2))
    field = applicant[3]
    scores = [int(s) for i, s in enumerate(applicant[1]) if i in tests[field]]
    return sum(scores) / len(scores)


def sort_applicants(applicants):
    applicants.sort(key=(lambda a: a[0]))
    applicants.sort(key=find_mean_score, reverse=True)


def main():
    accepted = [[], [], [], [], []]
    considered = [[], [], [], [], []]
    majors = {"Biotech": 0, "Chemistry": 1, "Engineering": 2,
              "Mathematics": 3, "Physics": 4}
    max_applicants = int(input())
    applicants = []
    with open("applicants.txt", "r") as f:
        for line in f:
            first, last, p, c, m, cs, m1, m2, m3 = line.split()
            name = first + " " + last
            applicants.append([name, (p, c, m, cs), (m1, m2, m3), -1])

    for priority in range(3):
        for applicant in applicants:
            major = applicant[2][priority]
            considered[majors[major]].append(applicant)
            applicant[3] = majors[major]
        for field in range(5):
            sort_applicants(considered[field])
            max_considered = max_applicants - len(accepted[field])
            while len(considered[field]) > max_considered:
                considered[field].pop()
            accepted[field].extend(considered[field])
            for applicant in considered[field]:
                applicants.remove(applicant)
            considered[field].clear()

    for major in majors:
        major_index = majors[major]
        sort_applicants(accepted[major_index])
        with open(major.lower() + ".txt", "w") as out:
            for applicant in accepted[major_index]:
                print(applicant[0], find_mean_score(applicant), file=out)
            print(file=out)


if __name__ == "__main__":
    main()
