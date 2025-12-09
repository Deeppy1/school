jobs = {}
for i in range(2):
    job = input("Enter a Job: ")
    wage = input("Enter the wage: ")
    jobs.update({job:wage})
print(jobs)
search = input("What job do you want? ")
print(search,"pays £"+jobs[search],"per year")