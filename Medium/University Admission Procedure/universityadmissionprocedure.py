num_applicants = int(input())
num_to_accept = int(input())
applicants = []
for _ in range(num_applicants):
    first, last, gpa = input().split()
    applicants.append((first + " " + last, float(gpa)))
applicants.sort(key=(lambda a: a[0]))
applicants.sort(key=(lambda a: a[1]), reverse=True)
print("Successful applicants:")
for i in range(num_to_accept):
    print(applicants[i][0])
