# valores = [1,2,5,4,6,8,9,7,8,88,9,5,5,55,54,54545]
# def maior(*lista):
#     mai = 0
#     print('ANALISANDO VALORES!')
#     for i in lista:
#         print(i,end=' ')
#         if i > mai:
#             mai = i
#     print()
#     print(f'o maior valor e igual a {mai}')
#
#
# maior(*valores)#lembrar de colocar o asterisco *
def maior(*lista):
    mai = 0
    print('ANALISANDO VALORES!')
    for i in lista:
        print(i,end=' ')
        if i > mai :
            mai = i
    print(f'O maior valor e igual a {mai}')


maior(1,0,5,5,6,4,)
maior(9,8,5,2,1,5,)
maior(99,22,88898,656865,5)
maior(12,32,65,98,78,998)
maior(23,15,14,174,258,23659)