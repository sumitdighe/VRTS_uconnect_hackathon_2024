from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests
import json
import pandas as pd
import random



df = pd.read_csv("MainApp/Dataset.csv")


@csrf_exempt
def sample_api_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            instance_memory = data.get('instance_memory')
            avgcpu_usage = data.get('avgcpu_usage')
            vmmemorybucket = data.get('vmmemorybucket')
            vmcorecountbucket = int(data.get('vmcorecountbucket'))
            bucket = data.get('bucket')
            vcpus = data.get('vcpus')
            vmcreated = int(data.get('vmcreated'))
            vmdeleted = int(data.get('vmdeleted'))

            lifetime = max((vmdeleted - vmcreated), 300) / 3600
            corehours = lifetime * vmcorecountbucket

            url1 = "https://tt26xtjlxe.execute-api.ap-south-1.amazonaws.com/endpoint-stage/dev"
            payload1 = f"{instance_memory},{vcpus}"
            headers = {'Content-Type': 'text/csv'}
            response = requests.post(url1, headers=headers, data=payload1)

            url2 = "https://9vgrhqwpz9.execute-api.ap-south-1.amazonaws.com/autoscale-stage/dev"
            payload2 = f"{avgcpu_usage},{vmmemorybucket},{corehours}"
            response2 = requests.post(url2, headers=headers, data=payload2)

            prediction = response.json()["Prediction"][0]
            autoscale = response2.json()["Prediction"][0]

            instance_memory = f"{instance_memory} GiB"
            vcpus = f"{vcpus} vCPUs"
            azure_info, aws_ec2_info = filter(instance_memory, vcpus, bucket)
            data = [
                '0.5', '1.0', '0.75', '2.0', '4.0', '1.75', '8.0', '3.5', '16.0', '7.0', '14.0', '32.0', '28.0', '84.0',
                '64.0', '55.0', '48.0', '56.0', '128.0', '80.0', '3.75',
                '5.25', '15.25', '6.0', '7.5', '10.5', '30.5', '12.0', '15.0', '21.0', '61.0', '24.0', '30.0', '122.0',
                '42.0',
                '72.0', '60.0', '1.7', '17.1', '34.2',
                '68.4', '117.0', '60.5'
            ]
            data2 = ['1', '2', '4', '8', '6', '16', '12', '20', '32', '18', '10', '24']

            random_instance_memory = random.sample(data, 4)
            random_vcpu = random.sample(data2, 4)
            payload2 = f"{random_instance_memory[0]},{random_vcpu[0]}"
            payload3 = f"{random_instance_memory[1]},{random_vcpu[1]}"
            payload4 = f"{random_instance_memory[2]},{random_vcpu[2]}"
            payload5 = f"{random_instance_memory[3]},{random_vcpu[3]}"
            headers = {'Content-Type': 'text/csv'}
            response3 = requests.post(url1, headers=headers, data=payload2)
            response4 = requests.post(url1, headers=headers, data=payload3)
            response5 = requests.post(url1, headers=headers, data=payload4)
            response6 = requests.post(url1, headers=headers, data=payload5)
            prediction2 = response3.json()["Prediction"][0]
            prediction3 = response4.json()["Prediction"][0]
            prediction4 = response5.json()["Prediction"][0]
            prediction5 = response6.json()["Prediction"][0]
            azuregraph2,awsgraph2=graph(f"{random_instance_memory[0]} GiB",f"{random_vcpu[0]} vCPUs","low")
            azuregraph3,awsgraph3=graph(f"{random_instance_memory[1]} GiB",f"{random_vcpu[1]} vCPUs","low")
            azuregraph4,awsgraph4=graph(f"{random_instance_memory[2]} GiB",f"{random_vcpu[2]} vCPUs","low")
            azuregraph5,awsgraph5=graph(f"{random_instance_memory[3]} GiB",f"{random_vcpu[3]} vCPUs","low")
            return JsonResponse({'prediction': prediction,'prediction2': prediction2,'prediction3': prediction3,'prediction4': prediction4,'prediction5': prediction5, 'autoscale': autoscale, 'azure_info': azure_info, 'aws_ec2_info': aws_ec2_info,"azuregraph2":azuregraph2,"awsgraph2":awsgraph2,"azuregraph3":azuregraph3,"awsgraph3":awsgraph3,"azuregraph4":azuregraph4,"awsgraph4":awsgraph4,"azuregraph5":azuregraph5,"awsgraph5":awsgraph5})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)


def filter(instance_memory, vcpus, user_budget):
    budget_range = {
        'low': (0, 0.0694),
        'medium': (0.0694, 0.1388),
        'high': (0.1388, 0.1736),
        'very high': (0.1736, float('inf'))
    }

    def filter_data(instance_memory, vcpus, service_provider):
        filtered_df = df[(df['Instance_Memory'] == instance_memory) &
                         (df['vCPUs'] == vcpus) &
                         (df['Service_Provider'] == service_provider)]
        filtered_df = filtered_df.dropna()
        return filtered_df

    def find_min_on_demand(data):
        if data.empty:
            return None
        else:
            on_demand_column = data['On_Demand']
            if on_demand_column.isna().all():
                return None
            else:
                on_demand_column = pd.to_numeric(on_demand_column.str.replace('$', '').str.replace(' hourly', ''),
                                                 errors='coerce')
                min_index = on_demand_column.idxmin()
                return data.loc[min_index].to_dict()

    service_provider = "Microsoft Azure"
    service_provider2 = "Amazon EC2"

    filtered_data = filter_data(instance_memory, vcpus, service_provider)
    filtered_data2 = filter_data(instance_memory, vcpus, service_provider2)

    min_on_demand = find_min_on_demand(filtered_data)
    min_on_demand2 = find_min_on_demand(filtered_data2)

    classified_costs = {}

    if min_on_demand is not None:
        classified_costs[service_provider] = (min_on_demand, user_budget)

    if min_on_demand2 is not None:
        classified_costs[service_provider2] = (min_on_demand2, user_budget)

    azure_info = {}
    aws_ec2_info = {}

    for provider, (package, budget_range) in classified_costs.items():
        if budget_range == user_budget:
            if provider == "Microsoft Azure":
                azure_info["Microsoft_Azure"] = package
            elif provider == "Amazon EC2":
                aws_ec2_info["Amazon_EC2"] = package
    return azure_info, aws_ec2_info

def graph(instance_memory, vcpus, user_budget):
    budget_range = {
        'low': (0, 0.0694),
        'medium': (0.0694, 0.1388),
        'high': (0.1388, 0.1736),
        'very high': (0.1736, float('inf'))
    }

    def filter_data2(instance_memory, vcpus, service_provider):
        filtered_df = df[(df['Instance_Memory'] == instance_memory) |
                         (df['vCPUs'] == vcpus) &
                         (df['Service_Provider'] == service_provider)]
        filtered_df = filtered_df.dropna()
        return filtered_df

    def find_min_on_demand2(data):
        if data.empty:
            return None
        else:
            data['On_Demand'] = pd.to_numeric(data['On_Demand'].str.replace('$', '').str.replace(' hourly', ''),
                                              errors='coerce')
            min_index = data['On_Demand'].idxmin()
            return data.loc[min_index].to_dict()

    service_provider = "Microsoft Azure"
    service_provider2 = "Amazon EC2"

    filtered_data = filter_data2(instance_memory, vcpus, service_provider)
    filtered_data2 =filter_data2(instance_memory, vcpus, service_provider2)

    min_on_demand = find_min_on_demand2(filtered_data)
    min_on_demand2 = find_min_on_demand2(filtered_data2)

    classified_costs = {}

    if min_on_demand is not None:
        classified_costs[service_provider] = (min_on_demand, user_budget)

    if min_on_demand2 is not None:
        classified_costs[service_provider2] = (min_on_demand2, user_budget)

    azure_info = {}
    aws_ec2_info = {}

    for provider, (package, budget_range) in classified_costs.items():
        if budget_range == user_budget:
            if provider == "Microsoft Azure":
                azure_info["Microsoft_Azure"] = package
            elif provider == "Amazon EC2":
                aws_ec2_info["Amazon_EC2"] = package
    return azure_info, aws_ec2_info
