def cal_minutes(queue_jobs, position_of_job):
    # sorted the piorites_jobs
    sorted_job = sorted(queue_jobs, reverse=True)
    minutes = 0
    while len(sorted_job) != 0:
        job = queue_jobs.pop(0)
        if job == sorted_job[0]:
            sorted_job.pop(0)
            minutes += 1
            if position_of_job == 0:
                return minutes
        else:
            queue_jobs.append(job)
        position_of_job -= 1
        if position_of_job < 0:
            position_of_job = len(queue_jobs)-1


number_tests = int(input())
for _ in range(number_tests):
    number_jobs, position_of_job = list(map(int, input().split()))
    queue_jobs = list(map(int, input().split()))
    result = cal_minutes(queue_jobs, position_of_job)
    print(result)
