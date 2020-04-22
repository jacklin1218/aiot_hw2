from django.http import HttpResponse, JsonResponse

from django.views.decorators.csrf import csrf_exempt
import json

def helloworld(request):
    return HttpResponse('Hello World!')

@csrf_exempt
def callback(request):
    if request.method == 'POST':
        return HttpResponse('POST')
    else:
        return HttpResponse('GET')

@csrf_exempt
def testPost(request):
    if request.method == 'POST':
        a = request.body.decode('utf-8')
       
        responDict = {}
        responDict['Result'] = ''
        
        dict1 = json.loads(a)

        tmp = dict1['Question'].split(' ')

        if(tmp[1]=='+'):
            tmp1 = int(tmp[0]) + int(tmp[2])
            responDict['Result'] = str(int(tmp1))
        elif(tmp[1]=='-'):
            tmp1 = int(tmp[0]) - int(tmp[2])
            responDict['Result'] = str(int(tmp1))
        elif(tmp[1]=='*'):
            tmp1 = int(tmp[0]) * int(tmp[2])
            responDict['Result'] = str(int(tmp1))
        elif(tmp[1]=='%'):
            tmp1 = int(tmp[0]) % int(tmp[2])
            responDict['Result'] = str(int(tmp1))
        elif(tmp[1]=='|'):
            dict1['Question'] = dict1['Question'].replace('|', '410506139').replace(' ', '')
            responDict['Result'] = dict1['Question']
       

        return JsonResponse(responDict)
    else:
        responDict = {}
        responDict['method'] = 'GET'
        return JsonResponse(responDict)
