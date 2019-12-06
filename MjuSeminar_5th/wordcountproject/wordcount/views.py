from django.shortcuts import render
import operator
def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def result(request):
    full_text = request.GET['fulltext']
    #승기 승기 승기 멋사
    word_list = full_text.split()

    #{승기,승기,승기,멋사}
    word_dictionary = {}

    for word in word_list:
        if word in word_dictionary:
            #word = {승기 사자 승기 멋사}
            #dictionary = {}
            #dictionary = {{key값,key에 있는 숫자값}}
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1
            #dictionary = [{승기,4},{사자,1}]
            #char a[10] = [1,2,3,4,5,6,7,8,9,10]
    max_wordtotal=highest=max(word_dictionary.items(), key = lambda x: x[1])
    max_wordtotal_first_1=highest=max(word_dictionary.items(), key = lambda x: x[1])[0] #최대값
    sortedArr = sorted(word_dictionary.items(), key=operator.itemgetter(1), reverse=True) #내림차순

    return render(request,'result.html',{'fulltext': full_text,'total': len(word_list),'dictionary': word_dictionary.items(),'sortedArr':sortedArr,'max_wordtotal_first_1':max_wordtotal_first_1})
