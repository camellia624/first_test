num = []
except_num = []

for i in range(100):
    if i % 2 !=0:
        num.append(i)
    else:
        except_num.append(i)


print(f'num:{num}')
print(f'except_num:{except_num}')