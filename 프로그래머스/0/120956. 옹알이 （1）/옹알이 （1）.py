def solution(babbling):
    can_say = ['aya', 'ye', 'woo', 'ma']
    count = 0
    
    for word in babbling:
        while any(sound in word for sound in can_say):
            for sound in can_say:
                word = word.replace(sound, ' ')
        if word.strip() == '':
            count += 1
    
    return count

            