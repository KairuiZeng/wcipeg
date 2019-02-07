import math

x = 10
while x != 0:
    dista, distb, vela, velb, anga, angb, time = input().split()
    dista = float(dista)
    distb = float(distb)
    vela = float(vela)
    velb = float(velb)
    anga = float(anga)
    angb = float(angb)
    time = float(time)

    totaldista = dista + vela * time
    totaldistb = distb + velb * time

    horizontal = totaldista * math.cos(math.radians(anga)) - totaldistb * math.cos(math.radians(angb))
    vertical = totaldista * math.sin(math.radians(anga)) - totaldistb * math.sin(math.radians(angb))

    final = math.sqrt(horizontal**2 + vertical**2)
    print("%.2f" % final)
