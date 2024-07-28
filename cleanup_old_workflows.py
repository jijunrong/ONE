import os
import requests
from datetime import datetime, timedelta

# 配置
REPO = os.getenv('GITHUB_REPOSITORY')
TOKEN = os.getenv('GITHUB_TOKEN')
DAYS_TO_KEEP = 7  # 保留最近30天的工作流运行记录

# 计算删除的截止日期
cutoff_date = datetime.now() - timedelta(days=DAYS_TO_KEEP)

def get_workflow_runs(page=1):
    url = f'https://api.github.com/repos/{REPO}/actions/runs'
    headers = {'Authorization': f'token {TOKEN}'}
    params = {'per_page': 100, 'page': page}
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()

def delete_workflow_run(run_id):
    url = f'https://api.github.com/repos/{REPO}/actions/runs/{run_id}'
    headers = {'Authorization': f'token {TOKEN}'}
    response = requests.delete(url, headers=headers)
    response.raise_for_status()
    return response.status_code == 204

def main():
    page = 1
    while True:
        runs = get_workflow_runs(page)
        if not runs['workflow_runs']:
            break

        for run in runs['workflow_runs']:
            run_date = datetime.strptime(run['created_at'], '%Y-%m-%dT%H:%M:%SZ')
            if run_date < cutoff_date:
                print(f'正在删除创建于 {run_date} 的工作流运行记录 {run["id"]}')
                delete_workflow_run(run['id'])

        page += 1

if __name__ == '__main__':
    main()
