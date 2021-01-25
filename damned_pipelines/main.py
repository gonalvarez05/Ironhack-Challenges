
# imports
from modules import module as mod



#GIT INFO
api_token = '9653fbae4009c65bbe2ccc67b252406089d3741f'
username = 'gonalvarez05'
base_url = 'https://api.github.com/'
key = 'repos/'
owner = 'ta-data-mad/'
repo = 'dataptmad1120/'
search = 'search/issues?q=repo:'+owner+repo+'+type:pr+state:{}'
pulls = 'pulls?page={}&per_page=100&state={}'
commits = 'pulls/{}/commits'
state = 'open'



field_list1 = ['number',
               'title',
               'state',
               'created_at',
               'updated_at',
               'closed_at',
               'html_url',
               'base.repo.full_name',
               'base.ref',
               'head.repo.full_name',
               'head.ref',
               'head.repo.pushed_at']
field_list2 = ['student_name',
               'number',
               'lab_name',
               'state',
               'lab_status',
               'created_at',
               'updated_at',
               'closed_at',
               'html_url',
               'base.repo.full_name',
               'base.ref',
               'head.repo.full_name',
               'head.ref',
               'head.repo.pushed_at']
field_sort1 = ['state',
               'lab_name',
               'student_name']
field_name1 = ['Student Name',
               'PR Number',
               'Lab Name',
               'PR Status',
               'Lab Status',
               'PR Created at',
               'PR Updated at',
               'PR Closed at',
               'PR URL',
               'base repository',
               'base',
               'head repository',
               'compare',
               'Pushed at']

def main ():
    df_pulls = mod.get_pulls(base_url, key, owner, repo, pulls, search, state, username, api_token, field_list1)
    print('creating df...')
    df_status = mod.df_status(df_pulls, base_url, key, owner, repo, commits, username, api_token, field_list2)
    print('create the csv with status...')
    df_csv = mod.create_csv(df_status, field_sort1, field_name1)


if __name__ == '__main__':
    main()
