from flask import Flask, render_template, request
import pandas as pd
import matplotlib.pyplot as plt
import joblib
import os
from your_tco_calculator_script import *

app = Flask(__name__)

class ServerWorkload:
    def __init__(self, os, server_count, cores_per_server, ram_gb, auto_scaling, iops, network_gb, backup_dedupe_ratio,latency,workloadType):
        self.os = os
        # self.license_type = license_type
        self.server_count = server_count
        self.cores_per_server = cores_per_server
        self.ram_gb = ram_gb
        # self.optimize_by = optimize_by
        # self.gpu = gpu
        self.auto_scaling = auto_scaling
        self.iops = iops
        self.network_gb = network_gb
        self.backup_dedupe_ratio = backup_dedupe_ratio
        self.latency=latency
        self.workloadType=workloadType

class StorageCosts:
    def __init__(self, total_storage_gb, annual_support_percent):
        self.total_storage_gb = total_storage_gb
        self.annual_support_percent = annual_support_percent

class LaborCosts:
    def __init__(self, servers_per_admin, hourly_rate):
        self.servers_per_admin = servers_per_admin
        self.hourly_rate = hourly_rate

def collect_server_workload():
    os = request.form['os']
    # license_type = request.form['license']
    server_count = int(request.form['serverCount'])
    cores_per_server = int(request.form['coresPerServer'])
    ram_gb = int(request.form['ramGB'])
    # optimize_by = request.form['optimizeBy']
    # gpu = request.form['gpu']
    auto_scaling = request.form['autoScaling'] == 'Yes'
    iops = int(request.form['iops'])
    network_gb = int(request.form['networkGB'])
    backup_dedupe_ratio = float(request.form['backupDedupeRatio'])
    latency = int(request.form['latency'])
    workloadType = str(request.form['workloadType'])
    return ServerWorkload(os, server_count, cores_per_server, ram_gb, auto_scaling, iops, network_gb, backup_dedupe_ratio,latency,workloadType)

def collect_storage_costs():
    total_storage_gb = float(request.form['totalStorageGB'])
    annual_support_percent = float(request.form['annualSupportPercent'])
    return StorageCosts(total_storage_gb, annual_support_percent)

def collect_labor_costs():
    servers_per_admin = int(request.form['serversPerAdmin'])
    hourly_rate = float(request.form['hourlyRate'])
    return LaborCosts(servers_per_admin, hourly_rate)

def estimate_server_cost(server_workload, is_cloud):
    cost_per_core = 20
    cost_per_gb_ram = 0.6
    scaling_factor = 1

    core_cost = server_workload.cores_per_server * cost_per_core
    ram_cost = server_workload.ram_gb * cost_per_gb_ram

    total_cost = (core_cost + ram_cost) * server_workload.server_count * scaling_factor

    return total_cost


def estimate_cloud_server_cost(server_workload, cloud_provider):
    cloud_cost_factors = {
        'AWS': {'cost_per_core': 10, 'cost_per_gb_ram': 0.4, 'scaling_factor': 1.2},
        'Azure': {'cost_per_core': 15, 'cost_per_gb_ram': 0.3, 'scaling_factor': 1.15},
        'GCP': {'cost_per_core': 20, 'cost_per_gb_ram': 0.5, 'scaling_factor': 1.1}
    }

    if server_workload.auto_scaling:
        scaling_factor = cloud_cost_factors[cloud_provider]['scaling_factor']
    else:
        scaling_factor = 1

    core_cost = server_workload.cores_per_server * cloud_cost_factors[cloud_provider]['cost_per_core']
    ram_cost = server_workload.ram_gb * cloud_cost_factors[cloud_provider]['cost_per_gb_ram']

    total_cost = (core_cost + ram_cost) * server_workload.server_count * scaling_factor

    return total_cost

def estimate_storage_cost(storage_costs, is_cloud):
    if is_cloud:
        cost_per_gb = 0.2
    else:
        cost_per_gb = 0.5

    total_cost = storage_costs.total_storage_gb * cost_per_gb
    total_cost += total_cost * (storage_costs.annual_support_percent / 100)
    return total_cost

def estimate_labor_cost(labor_costs, server_workload,is_cloud):
    if is_cloud:
        labor_costs.hourly_rate *= 0.2
    total_admins = server_workload.server_count / labor_costs.servers_per_admin
    annual_salary = labor_costs.hourly_rate * 40 *50
    total_cost = total_admins * annual_salary
    return total_cost

import pandas as pd
import matplotlib.pyplot as plt

def generate_report(cost_details, environment):
    df = pd.DataFrame(list(cost_details.items()), columns=['Cost Component', f'Amount ({environment})'])
    print(f"Detailed Cost Report for {environment}:")
    print(df)

    fig, ax = plt.subplots()
    ax.pie(df[f'Amount ({environment})'], labels=df['Cost Component'], autopct='%1.1f%%', startangle=90)
    ax.axis('equal')
    plt.title(f'Cost Breakdown ({environment})')
    plt.show()


from joblib import load
def predict_deployment_cu(input_data):
    model = load('model.pkl')
    predicted_deployment = model.predict(input_data)
    return predicted_deployment[0]


import requests
from dateutil.parser import parse 

def get_all_exchange_rates_erapi(src):
    url = f"https://open.er-api.com/v6/latest/{src}"
    data = requests.get(url).json()
    if data["result"] == "success":
        last_updated_datetime = parse(data["time_last_update_utc"])
        exchange_rates = data["rates"]
    return last_updated_datetime, exchange_rates


def convert_currency(amount, from_currency, to_currency):
    _, exchange_rates = get_all_exchange_rates_erapi(from_currency)
    return exchange_rates[to_currency] * amount

def get_currency_from_country(country):
    country_to_currency = {
        'United States': 'USD',
        'Germany': 'EUR',
        'India': 'INR',
    }
    return country_to_currency.get(country, 'USD')

def display_costs_in_local_currency(user_country,total_cost, base_currency='USD'):
    user_currency = get_currency_from_country(user_country)
    if base_currency != user_currency:
        converted_cost = convert_currency(total_cost, base_currency, user_currency)
        return converted_cost
    else:
        return total_cost

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        server_workload = collect_server_workload()
        storage_costs = collect_storage_costs()
        labor_costs = collect_labor_costs()
        country = input("Please enter your country: ")
        cloud_providers = ['AWS', 'Azure', 'GCP']
        cost_projections = {}
        on_premises_server_cost = estimate_server_cost(server_workload, is_cloud=False)
        on_premises_server_cost = display_costs_in_local_currency(country,on_premises_server_cost)
        on_premises_storage_cost = estimate_storage_cost(storage_costs, is_cloud=False)
        on_premises_storage_cost = display_costs_in_local_currency(country,on_premises_storage_cost)

        on_premise_labor_cost = estimate_labor_cost(labor_costs, server_workload,is_cloud=False)
        on_premise_labor_cost = display_costs_in_local_currency(country,on_premise_labor_cost)

        for provider in cloud_providers:
            cloud_server_cost = estimate_cloud_server_cost(server_workload, provider)
            cloud_server_cost = display_costs_in_local_currency(country,cloud_server_cost)
            cloud_storage_cost = estimate_storage_cost(storage_costs, is_cloud=True)
            cloud_storage_cost = display_costs_in_local_currency(country,cloud_storage_cost)
            cloud_labor_cost = estimate_labor_cost(labor_costs, server_workload, is_cloud=True)  # Assuming labor cost is same for both
            cloud_labor_cost = display_costs_in_local_currency(country,cloud_labor_cost)
            cloud_total = cloud_server_cost + cloud_storage_cost + cloud_labor_cost
            cloud_total = display_costs_in_local_currency(country,cloud_total)
            cost_projections[provider] = cloud_total
            cloud_details = {'Server Cost': cloud_server_cost, 'Storage Cost': cloud_storage_cost, 'Labor Cost': cloud_labor_cost}

            print(f"Estimated annual cost for {provider}: {cloud_total:.2f}")
            generate_report(cloud_details, provider)

        on_premises_total = on_premises_server_cost + on_premises_storage_cost + on_premise_labor_cost
        on_premise_total = display_costs_in_local_currency(country,on_premises_total)
        cost_projections['On-Premises'] = on_premises_total
        on_premises_details = {'Server Cost': on_premises_server_cost, 'Storage Cost': on_premises_storage_cost, 'Labor Cost': on_premise_labor_cost}

        print(f"Estimated annual on-premises cost: {on_premises_total:.2f}")
        generate_report(on_premises_details, 'On-Premises')
    # project_costs_over_time(server_workload, storage_costs, labor_costs, cost_projections, 10)
        input_for_prediction = {
        'IOPS': [server_workload.iops],
        'Compute': [f"{server_workload.cores_per_server} vCPUs"],
        'NetworkReq': [f"{server_workload.network_gb} Gbps"],
        'BackupDedupeRatio': [server_workload.backup_dedupe_ratio],
        'Storage': [storage_costs.total_storage_gb],
        'RAM': [f"{server_workload.ram_gb} GB"],
        'Latency': [server_workload.latency],
        'WorkloadType': [server_workload.workloadType]
        }
        input_df = pd.DataFrame(input_for_prediction)
        predicted_deployment = predict_deployment_cu(input_df)
        # print(f"Predicted DeploymentCU: {predicted_deployment}")
        return render_template('result.html', tco_result="Your TCO calculation is complete!",cost_details=cost_projections)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
