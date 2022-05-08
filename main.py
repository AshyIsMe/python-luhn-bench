import numpy as np
import glob

# https://www.reddit.com/r/learnpython/comments/dkdnj6/luhn_algorithm/

# ascii digits 0 to 9: integer 48 to 57 inclusive

def luhn_count(a):
    dm = (a>47)&(a<58)
    a2 = np.divmod(2*a,10)
    m = np.mod(np.array(range(len(a))), 2) # mask
    # shift mask to ensure m[-1]==1
    m = m ^ (m[-1]^1)
    # AA TODO: not finished.  See:
    # https://github.com/mmcloughlin/luhn/blob/master/luhn.py#L3

def main():
    print("TODO: read all *.txt files")
    print("TODO: numpy luhn algorithm")
    print("TODO: count matches per file")

    files = glob.glob('TestData/*.txt')
    for file in files:
        with open(file, 'rb') as f:
            a=np.frombuffer(f.read(), dtype=np.uint8)

if __name__=="__main__":
    main()
