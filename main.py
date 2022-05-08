import numpy as np
import glob

# https://www.reddit.com/r/learnpython/comments/dkdnj6/luhn_algorithm/

# ascii digits 0 to 9: integer 48 to 57 inclusive

WINDOW = 40

# reference: https://github.com/mmcloughlin/luhn/blob/master/luhn.py#L3
def luhn_count(a):
    dm = (a>47)&(a<58)      #digitmask
    a=a-48
    t = np.divmod(2*a,10)
    a2 = t[0]+t[1]          #a2 doubled and divmod summed

    count=0
    for i in range(len(a)):
        j=i+WINDOW
        # luhn checksum. Note this assumes the check digit is in place.
        odd_sum = np.sum(a[i:j][dm[i:j]][-1::-2])
        even_sum = np.sum(a2[i:j][dm[i:j]][-2::-2])
        count+= int(0==(odd_sum + even_sum)%10)
    return count


def main():
    files = glob.glob('*.txt')
    print('Count,File')
    for file in files:
        with open(file, 'rb') as f:
            a=np.frombuffer(f.read(), dtype=np.uint8)
            print(f"{luhn_count(a)},{file}")

if __name__=="__main__":
    main()
