import requests
import json
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
def handler(context, inputs):
    url = f"https://api.mgmt.cloud.vmware.com/iaas/api/integrations?apiVersion=2021-07-15&$count"
    headers = {
        'accept': "application/json",
        'content-type': "application/json",
        'authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InNpZ25pbmdfMiJ9.eyJzdWIiOiJ2bXdhcmUuY29tOmMwNTU0ZDFiLTczNjgtNGRlZS1iMDU0LTMzOTk3ODVmZjM4YyIsImlzcyI6Imh0dHBzOi8vZ2F6LmNzcC12aWRtLXByb2QuY29tIiwiY29udGV4dF9uYW1lIjoiNmE0ZmMxMzEtYTVmNC00NTZkLWJmMjQtY2IwMGUxNTFiYjQ5IiwiYXpwIjoiY3NwX3ByZF9nYXpfaW50ZXJuYWxfY2xpZW50X2lkIiwiYXV0aG9yaXphdGlvbl9kZXRhaWxzIjpbXSwiZG9tYWluIjoidm13YXJlLmNvbSIsImNvbnRleHQiOiJhZmVlNjJhZC1hZTc5LTQ0YzktYmM4OS1mZDJhODUxNDA2ZWIiLCJwZXJtcyI6WyJleHRlcm5hbC9Zdy1IeUJlUXpqQ1hrTDJ3UVNlR3dhdUotbUFfL2NhdGFsb2c6dXNlciIsImV4dGVybmFsLzg3ZTUwZjIxLWMxMTEtNGYxNy04NjQ2LTJhMjlhODgxNjE2MS9ndWFyZHJhaWxzLXNlcnZpY2U6dXNlciIsImNzcDpvcmdfb3duZXIiLCJleHRlcm5hbC84N2U1MGYyMS1jMTExLTRmMTctODY0Ni0yYTI5YTg4MTYxNjEvZ3VhcmRyYWlscy1zZXJ2aWNlOmFkbWluIiwiZXh0ZXJuYWwvdWx2cXRONDE0MWJlQ1Qyb09uYmotd2xrekdnXy9Db2RlU3RyZWFtOnZpZXdlciIsImV4dGVybmFsL2MzY2Q2NTYxLTAwZDgtNDlhZi04MDdlLTI1N2NmNjI2YzBjNC92cm9wczphZG1pbiIsImV4dGVybmFsLzdjSjJuZ1NfaFJDWV9iSWJXdWNNNEtXUXdPb18vaW5zdGFuY2U6NzZhY2QwYjctNDY5Yy00ZmY4LWI4N2ItODY0OWI4YzY0NWI2L2xvZy1pbnRlbGxpZ2VuY2U6YWRtaW4iLCJleHRlcm5hbC9aeTkyNG1FM2R3bjJBU3lWWlIwTm43bHVwZUFfL2F1dG9tYXRpb25zZXJ2aWNlOnVzZXIiLCJleHRlcm5hbC9aeTkyNG1FM2R3bjJBU3lWWlIwTm43bHVwZUFfL2F1dG9tYXRpb25zZXJ2aWNlOmNsb3VkX2FkbWluIiwiZXh0ZXJuYWwvN2NKMm5nU19oUkNZX2JJYld1Y000S1dRd09vXy9sb2ctaW50ZWxsaWdlbmNlOmFkbWluIiwiZXh0ZXJuYWwvOXFqb05hZkRwOVhreXlRTGNMQ0tXUHNBaXIwXy92cm5pOmFkbWluIiwiZXh0ZXJuYWwvWXctSHlCZVF6akNYa0wyd1FTZUd3YXVKLW1BXy9jYXRhbG9nOmFkbWluIiwiZXh0ZXJuYWwvdWx2cXRONDE0MWJlQ1Qyb09uYmotd2xrekdnXy9Db2RlU3RyZWFtOmRldmVsb3BlciIsImV4dGVybmFsL2MzY2Q2NTYxLTAwZDgtNDlhZi04MDdlLTI1N2NmNjI2YzBjNC92cm9wczp1c2VyIl0sImV4cCI6MTY2NjM1NDg0MSwiaWF0IjoxNjY2MzUzMDQxLCJqdGkiOiJTTE5ha082U3VTUkhNWmZaUzVQSHc3dnFsVGciLCJhY2N0Ijoic2V0aGlhbkB2bXdhcmUuY29tIiwidXNlcm5hbWUiOiJzZXRoaWFuIn0.B1UWCHQrJLMtPRub9DTbsjR9vnXVG5257xdvA77OUe9UiZYLnXDhD_3SvDPF2LJ-X-nyTAE9yF-KLR8NwYrBLHCwAEZpYG-sKrqDqEfaBnWJAYPgkx6KuKbjaIsAS56-sAkg_dDmCCFU2UJNzL9TvGw0HcEl5B7Dova3WtXgUqbNEm9NDj954ttjzYkb8-gySwlF0-vZpfsP7OOC_3qzZi9YBeAWvzG25oYsZaLiRn_z5KA5fTM5AhAc46fxPXYillRGzYEMNyXqxSojPiAZveiIxxpzXS-cmGw3pNg3ijWPw2LX0cbunNfOY1PxX2cRXbTAp1F4rYDypt9wiwnbVA'
        }
    result = requests.get(url=url, headers=headers, verify=False)
    if result.status_code == 200:
        data = result.json()
        print(json.dumps(data, indent=4))
