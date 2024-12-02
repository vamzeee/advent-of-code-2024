################# part 1 ###############

input = open('input.txt').read().strip()

safe_reports = 0

def is_report_safe(report) :
    direction = int(report[1]) - int(report[0])

    for i in range(len(report) - 1) :
        num1 = int(report[i])
        num2 = int(report[i+1])
        if abs(num2 - num1) > 3 or num2 == num1 or (num2 - num1)*direction < 0 :
            return False, i
        
    return True, i

for line in input.splitlines() :
    report = line.split()
    
    if is_report_safe(report)[0] :
        safe_reports = safe_reports + 1

print(safe_reports)


################# part 2 ###############

safe_reports = 0

for line in input.splitlines() :
    report = line.split()

    is_safe, pos = is_report_safe(report)

    if is_safe :
        safe_reports = safe_reports + 1
    else :
        try1 = report.copy()
        try1.pop(pos)
        try2 = report.copy()
        try2.pop(pos+1)
        try3 = report.copy()
        if pos > 0 :
            try3.pop(pos-1)
        if is_report_safe(try1)[0] or is_report_safe(try2)[0] or is_report_safe(try3)[0]:
            safe_reports = safe_reports + 1

print(safe_reports)
