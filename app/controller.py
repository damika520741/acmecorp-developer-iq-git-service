from fastapi import APIRouter
from model import Git
import service

router = APIRouter()

@router.get("/commits")
async def get_commits(git: Git):
    return await service.get_commits(git)

@router.get("/pulls")
async def get_pulls(git: Git):
    return await service.get_pulls(git)

@router.get("/issues")
async def get_issues(git: Git):
    return await service.get_issues(git)

@router.post("/save/commits")
async def save_commits(git: Git):
    return await service.save_commits(git)

@router.post("/save/pulls")
async def save_pulls(git: Git):
    return await service.save_pulls(git)

@router.post("/save/issues")
async def save_issues(git: Git):
    return await service.save_issues(git)