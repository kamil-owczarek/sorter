import datetime
from configparser import ConfigParser
config=ConfigParser()
config.read('config.ini')

elementsQS=int(config['quicksort']['elements'])
stepQS=int(config['quicksort']['step'])
iterQS=int(config['quicksort']['iter'])

elementsBS=int(config['bubblesort']['elements'])
stepBS=int(config['bubblesort']['step'])
iterBS=int(config['bubblesort']['iter'])


times=[]


def writeBS(list):
    f= open("output_BS.txt","a")
    f.writelines(str(list))
    f.write('\n')
    f.close()

def writeQS(list):
    f= open("output_QS.txt","a")
    f.writelines(str(list))
    f.write('\n')
    f.close()

def bubblesort(list,n):

    for i in range(n):
        for j in range(n-i-1):
            if list[j]>list[j+1]:
               list[j],list[j+1]=list[j+1],list[j]
    return list



def quicksort(list,l=0,r=None):
    if r is None:
        r=len(list)-1
    i,j=l,r
    if(l+r)%2==0:
        mid=(l+r)/2
    else:
        mid=(l+r+1)/2
    pivot=list[int(mid)]
    while i<=j:
        while list[i]<pivot:i+=1
        while list[j]>pivot:j-=1
        if i<=j:
            list[i],list[j]=list[j],list[i]
            i+=1;j-=1
    if l<j:quicksort(list,l,j)
    if r>i:quicksort(list,i,r)




def main():
    ans=True
    while ans:
        print("""
              Wybierz opcje:
          1. Bubble sort
          2. Quick sort
          w. Wyjdź
          """)
        ans=input()
        if ans=="1":
            # bubble
            step = stepQS
            f = open("input.txt", "r")
            data = eval(f.readline())
            f.close()
            print("Sortuje")
            for i in range(0, elementsQS + step, step):
                for x in range(iterQS):
                    start = datetime.datetime.now()
                    bubblesort(data, i)
                    end = (datetime.datetime.now() - start)
                    times.append(int(end.total_seconds() * 1000))
                writeBS(times)
                times.clear()
            print(data)
            print("Posortowane!")
        elif ans=="2":
            #quick
            step = stepQS
            f = open("input.txt", "r")
            data = eval(f.readline())
            f.close()
            print("Sortuje")
            for j in range(0, elementsQS + step, step):
                for i in range(iterQS):
                    start = datetime.datetime.now()
                    quicksort(data, 0, j - 1)
                    end = (datetime.datetime.now() - start)
                    times.append(int(end.total_seconds() * 1000))
                writeQS(times)
                times.clear()
            print(data)
            print("Posortowane!")
        elif ans=="w":
            print("Do zobaczenia")
            break

        elif ans!="":
            print("Brak opcji")

main()


