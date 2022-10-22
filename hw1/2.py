# w, h = 4.5, 7.9
w,h = list(map(float, input().replace('\n','').split(' ')))
print('area=%.2f' %(w*h))
print('Perimeter=', 2*(w+h))
