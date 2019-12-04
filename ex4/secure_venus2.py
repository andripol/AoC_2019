def check_consecutives(i,j,k,l,m,n):
    if ((i == j) and (j!=k)) or ((i!=j) and (j == k) and (k!=l)) or ((j!=k) and  (k == l) and (l!=m)) or ((k!=l) and (l == m) and (m!=n)) or ((l != m) and (m == n)):
        return True
    return False

def find_solution():
    counter = 0
    for i in range(1,7):
        for j in range(i,10):
            ij = i*100000 + j*10000
            if (ij < 130000): 
                continue
            if (ij > 670000):
                break
            for k in range(j,10):
                ijk = ij + k*1000
                if (j > k):
                    continue
                if (ijk > 678000): 
                    break
                for l in range(k,10):
                    ijkl = ijk + l*100
                    if (ijkl < 130200): 
                        continue
                    if (ijkl > 678200):
                        break
                    for m in range(l,10):
                        ijklm = ijkl + m*10
                        if ijklm < 130250 : 
                            continue
                        if (ijklm > 678270):
                            break
                        for n in range(m,10):
                            ijklmn = ijklm + n
                            if (ijklmn < 130254): 
                                continue
                            if (ijklmn > 678275):
                                break
                            if (check_consecutives(i,j,k,l,m,n)):
                                counter = counter + 1
    print(counter)
                    

def main():
    find_solution()

if __name__ == "__main__":
    main()
