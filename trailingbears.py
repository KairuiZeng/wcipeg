for rounds in range(5):
    ax, ay = input().split()
    bx, by = input().split()
    cx, cy = input().split()
    
    midabx = (int(ax) + int(ay)) / 2
    midaby = (int(ay) + int(by)) / 2

    midbcx = (int(bx) + int(cx)) / 2
    midbcy = (int(by) + int(cy)) / 2

    midcax = (int(ax) + int(cx)) / 2
    midcay = (int(ay) + int(cy)) / 2

    if ay == by:
        slope1 = -1 / (int(cy)-int(ay))/(int(cx)-int(ax))
        slope2 = -1 / (int(cy)-int(by))/(int(cx)-int(bx))

        intercept1 = midcay - midcax * slope1
        intercept2 = midbcy - midbcx * slope2

    elif by == cy:
        slope1 = -1 / (int(cy)-int(ay))/(int(cx)-int(ax))
        slope2 = -1 / (int(by)-int(ay))/(int(bx)-int(ax))

        intercept1 = midcay - midcax * slope1
        intercept2 = midaby - midabx * slope2

    else:
        slope1 = -1 / (int(cy)-int(by))/(int(cx)-int(bx))
        slope2 = -1 / (int(by)-int(ay))/(int(bx)-int(ax))

        intercept1 = midbcy - midbcx * slope1
        intercept2 = midaby - midabx * slope2

    xcentre = (intercept2 - bintercept1) / (slope1 - slope2)
    ycentre = slope1 * xcentre + intercept1

    print(str(round(xcentre, 2)) + ' ' + str(round(ycentre, 2)))
