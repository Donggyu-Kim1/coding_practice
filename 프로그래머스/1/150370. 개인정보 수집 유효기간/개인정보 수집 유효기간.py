def solution(today, terms, privacies):
    def to_days(date):
        year, month, day = map(int, date.split('.'))
        return year * 12 * 28 + month * 28 + day

    def add_months(date, months):
        year, month, day = map(int, date.split('.'))
        month += months
        year += (month - 1) // 12
        month = (month - 1) % 12 + 1
        return f"{year:04d}.{month:02d}.{day:02d}"

    term_dict = {t.split()[0]: int(t.split()[1]) for t in terms}
    today_days = to_days(today)
    
    result = []
    for i, privacy in enumerate(privacies, 1):
        collect_date, term = privacy.split()
        expire_date = add_months(collect_date, term_dict[term])
        if to_days(expire_date) <= today_days:
            result.append(i)
    
    return result