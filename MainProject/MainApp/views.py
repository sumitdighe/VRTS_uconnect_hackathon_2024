from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests
import json


@csrf_exempt
def sample_api_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            instance_memory = data.get('instance_memory')
            avgcpu_usage = data.get('avgcpu_usage')
            vmmemorybucket = data.get('vmmemorybucket')
            vcpus = data.get('vcpus')

            if instance_memory and vcpus and avgcpu_usage and vmmemorybucket:
                url1 = "https://tt26xtjlxe.execute-api.ap-south-1.amazonaws.com/endpoint-stage/dev"
                payload = f"{instance_memory},{vcpus}"
                headers = {'Content-Type': 'text/csv'}
                response = requests.post(url1, headers=headers, data=payload)
                prediction = response.json()["Prediction"][0]
                return JsonResponse({'message': prediction})
            else:
                return JsonResponse({'error': 'Both inputs are required'}, status=400)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
