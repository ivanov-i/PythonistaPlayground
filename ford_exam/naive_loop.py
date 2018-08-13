def distinct(lst):
    return len(lst) == len(set(lst))

for d in range(0,10):
    if distinct([d]):
        for o in range(0,10):
            if distinct([d,o]):
                for n in range(0,10):
                    if distinct([d,o,n]):
                        for a in range(0,10):
                            if distinct([d,o,n,a]):
                                for l in range(0,10):
                                    if distinct([d,o,n,a,l]):
                                        for g in range(0,10):
                                            if distinct([d,o,n,a,l,g]):
                                                for e in range(0,10):
                                                    if distinct([d,o,n,a,l,g,e]):
                                                        for r in range(0,10):
                                                            if distinct([d,o,n,a,l,g,e,r]):
                                                                for b in range(0,10):
                                                                    if distinct([d,o,n,a,l,g,e,r,b]):
                                                                        for t in range(0,10):
                                                                            if distinct([d,o,n,a,l,g,e,r,b,t]):
                                                                                donald = ((((((d)*10 + o)*10 + n)*10 + a)*10 + l)*10 + d)
                                                                                gerald = ((((((g)*10 + e)*10 + r)*10 + a)*10 + l)*10 + d)
                                                                                robert = ((((((r)*10 + o)*10 + b)*10 + e)*10 + r)*10 + t)
                                                                                if(donald + gerald == robert):
                                                                                    print([d,o,n,a,l,g,e,r,b,t])
                                                                                    print(donald, '+', gerald, '=', robert)
