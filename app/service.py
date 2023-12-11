from fastapi import HTTPException, status
from httpx import AsyncClient
from model import Git
from database import connection

HEADERS = dict()
HEADERS["Accept"] = "application/vnd.github+json"
HEADERS["X-GitHub-Api-Version"] = "2022-11-28"

async def get_commits(git: Git):
    url = f"https://api.github.com/repos/{git.owner}/{git.repo}/commits"

    headers = HEADERS.copy()
    headers["Authorization"] = f"Bearer {git.token}"

    print(headers)

    async with AsyncClient() as c:
        response = await c.get(url=url, headers=headers)
        if response.status_code == status.HTTP_200_OK:
            return dict(
                is_success=True,
                status_code=response.status_code,
                message="GitHub API request successful.",
                data=response.json()
            )
        else:
            return dict(
                is_success=False,
                status_code=response.status_code,
                message="GitHub API request failed.",
                data=None
            )
        
async def get_pulls(git: Git):
    url = f"https://api.github.com/repos/{git.owner}/{git.repo}/pulls"

    headers = HEADERS.copy()
    headers["Authorization"] = f"Bearer {git.token}"

    async with AsyncClient() as c:
        response = await c.get(url=url, headers=headers)
        if response.status_code == status.HTTP_200_OK:
            return dict(
                is_success=True,
                status_code=response.status_code,
                message="GitHub API request successful.",
                data=response.json()
            )
        else:
            return dict(
                is_success=False,
                status_code=response.status_code,
                message="GitHub API request failed.",
                data=None
            )
        
async def get_issues(git: Git):
    url = f"https://api.github.com/repos/{git.owner}/{git.repo}/issues"

    headers = HEADERS.copy()
    headers["Authorization"] = f"Bearer {git.token}"

    async with AsyncClient() as c:
        response = await c.get(url=url, headers=headers)
        if response.status_code == status.HTTP_200_OK:
            return dict(
                is_success=True,
                status_code=response.status_code,
                message="GitHub API request successful.",
                data=response.json()
            )
        else:
            return dict(
                is_success=False,
                status_code=response.status_code,
                message="GitHub API request failed.",
                data=None
            )
        
async def save_commits(git: Git):
    try:
        await connection.connect()
        response = await get_commits(git)
        if response["is_success"] == True:
            pass
        else:
            return response
    except Exception as e:
        return dict(
            is_success=False,
            status_code= status.HTTP_500_INTERNAL_SERVER_ERROR,
            message=str(e),
            data=None
        )
    finally:
        await connection.disconnect()

async def save_pulls(git: Git):
    try:
        await connection.connect()
        response = await get_pulls(git)
        if response["is_success"] == True:
            pass
        else:
            return response
    except Exception as e:
        return dict(
            is_success=False,
            status_code= status.HTTP_500_INTERNAL_SERVER_ERROR,
            message=str(e),
            data=None
        )
    finally:
        await connection.disconnect()

async def save_issues(git: Git):
    try:
        await connection.connect()
        response = await get_issues(git)
        if response["is_success"] == True:
            pass
        else:
            return response
    except Exception as e:
        return dict(
            is_success=False,
            status_code= status.HTTP_500_INTERNAL_SERVER_ERROR,
            message=str(e),
            data=None
        )
    finally:
        await connection.disconnect()