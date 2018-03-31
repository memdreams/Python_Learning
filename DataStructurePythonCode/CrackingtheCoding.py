"""
'Cracking the Coding Interview' 4th Edition, Exercise Coding
"""


def angleH_M(time):
    """
    Calculate the angle between hour hand and minute hand
    :arg
        time: string. eg. '12:20' 12 is hour, and 20 is minutes.
    """
    # h_angles = [x for x in range(0, 360, 30)] #360*(h%12)/12 + 360*(minutes/60)*(1/12)
    # m_angles = [x for x in range(0, 360, 6)]
    h, m = time.split(':')
    angle = 30*int(h) - 5.5*int(m)
    return angle

# Implementing the permutation algorithm
def merge(c, l):
    results = []
    for str in l:
        for i in range(len(str)+1):
            results.append(str[:i]+c+str[i:])
    return results

def permutations(s):
    if len(s) == 1:
        return [s]
    result = merge(s[-1], permutations(s[:-1]))
    return result


if __name__ == '__main__':
    print(angleH_M('11:30'))
    print(permutations('abdc'))



