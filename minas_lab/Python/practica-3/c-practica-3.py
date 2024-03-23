"""
LLEGAR A FIN DE MES

drive = https://drive.google.com/file/d/1iAb1SIzIozvviaw8m5QZ0rqFsP6RswT0/view?usp=sharing

"""


saldoCuentaDeBanco: int = int(input())
gastosEstimados: int = int(input())

if gastosEstimados > saldoCuentaDeBanco and gastosEstimados > 0:
    print("Si llegas a fin de mes")
elif abs(gastosEstimados) > saldoCuentaDeBanco:
    print("No llegas a fin de mes")
else:
    print("Si llegas a fin de mes")
