def solution(survey, choices):
    # 1
    dict_mbti = {"R": 0, "T": 0, "F": 0, "C": 0, "J": 0, "M": 0, "A": 0, "N": 0}
    survey_elements = ["RT", "TR", "FC", "CF", "MJ", "JM", "AN", "NA"]

    # 2
    for i in range(len(survey)):
        for j in survey_elements:
            if survey[i] == j:
                if 1 <= choices[i] <= 3:
                    dict_mbti[j[0]] += (4 - choices[i])
                elif 5 <= choices[i] <= 7:
                    dict_mbti[j[1]] += (choices[i] - 4)
                else:
                    pass

    # 3
    if dict_mbti['R'] < dict_mbti['T']:
        dict_mbti.pop('R')
    else:
        dict_mbti.pop('T')

    if dict_mbti['C'] < dict_mbti['F']:
        dict_mbti.pop('C')
    else:
        dict_mbti.pop('F')

    if dict_mbti['J'] < dict_mbti['M']:
        dict_mbti.pop('J')
    else:
        dict_mbti.pop('M')

    if dict_mbti['A'] < dict_mbti['N']:
        dict_mbti.pop('A')
    else:
        dict_mbti.pop('N')

    dict_key = list(dict_mbti.keys())
    result = "".join(dict_key)

    return result